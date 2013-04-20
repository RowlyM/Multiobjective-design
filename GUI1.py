# -*- coding: utf-8 -*-
"""

@author: Rowly Mudzhiba

"""
######################## modules ##################################################
import numpy as np
import matplotlib.pyplot as plt 
import objectives as obj
import pareto
import MODminifunc as func

from operator import itemgetter
from scipy import signal
from scipy import linalg
from EulerODE import Euler
from Optimizer import Optimize
from Sys_setup_window import sys_setup
from matplotlib.lines import Line2D
from matplotlib.artist import Artist
from matplotlib.mlab import dist_point_to_segment
from matplotlib.widgets import Button, RadioButtons
from matplotlib.patches import Polygon

###################### Default System parameters #####################################
Gp_n = [.125]     
Gp_d = [1,3,3,1]
SP = 1.                   # Set Point            
tfinal = 100        # simulation period
dt = .1
DT = 0       # Dead time (s)  
t = np.arange(0, tfinal, dt)
entries = len(t)

SP_input = 'step'           # Choose Set point input by typing 'step' or 'ramp'
step_time  = 0.
ramp_time = 5.
u = func.Step(t,step_time,SP)           
SP_info = [SP_input,step_time, ramp_time,SP]


#################### Initializing plots #############################################
#Kc Vs ti parameters
fig=plt.figure()
ax1 = fig.add_subplot(231)
plt.axis([0,60, 0,60])
ax1.plot(None,None)

kc = []
ti = []
td = []
plt.ylabel(r'$K_C$',fontsize = 'large')
plt.xlabel(r'$\tau_I$',fontsize = 'large')
# Kc vs td parameters
ax2= fig.add_subplot(232, sharey = ax1)
plt.axis([0,10, 0,60])
plt.ylabel(r'$K_C$',fontsize = 'large')
plt.xlabel(r'$\tau_D$',fontsize = 'large')
#ax2.text(4,SP,'drag along the axis ',fontsize = 16,color = 'red')

#plot3
ax3= fig.add_subplot(233)
plt.ylabel('risetime (s)',fontsize = 'large')
plt.xlabel('overshoot ratio',fontsize = 'large')
Mop_points = (None,None)
por = []
tpr = []
ISE = []
IAE = []
ITAE = []

tr = []
xd = []
yd = []
y = []
xs = []
polyx, ployy = [], [] 
#plot4
ax4 = fig.add_subplot(212)
plt.ylabel('y',fontsize = 12)
plt.xlabel('time (s)',fontsize = 12)
plt.axis([0,tfinal, 0,SP*2]) ### 
ax4.text(4,SP,'Click on the ti vs kc plot to obtain the time response',fontsize = 16,color = 'red')
Y =[]

points = [0]
ppline = []
SSoffset_out = [0]
UNSTABLE_out = [0]
goodpoints_out = [0]
idx_out = [0]
Bidx_out = [0]
por_out = [0]
ISE_out, IAE_out, ITAE_out = [0],[0],[0]
tr_out = [0]
xd_out = [0]
yd_out = [0]
Bxd_out, Byd_out =[0], [0]


##################################### Plotting functions ############################### 
def redraw_ax1():
    kc1,ti1= np.array(kc),np.array(ti)
    ax1 = fig.add_subplot(231)
    line1 = ax1.plot(ti1[SSoffset_out],kc1[SSoffset_out],'g+') 
    line2 = ax1.plot(ti1[UNSTABLE_out],kc1[UNSTABLE_out], 'r+') # adds ustables points
    line3 = ax1.plot(ti1[goodpoints_out], kc1[goodpoints_out], 'wo',picker = 5,) # adds good points
    line4 = ax1.plot(ti1[idx_out], kc1[idx_out],'bo') # from pareto.data
#        plt.figlegend((line1,line2,line3,line4,),('S/SOffset','Unstable','Stable points','Pareto points'),'upper right',borderaxespad=0.)
    ax1.axis([0,60, 0,60])
    plt.ylabel(r'$K_C$',fontsize = 'large')
    plt.xlabel(r'$\tau_I$',fontsize = 'large')
 
def redraw_ax3():
    ax3= fig.add_subplot(233)
    pline = ax3.plot(por_out, tr_out, 'wo',picker = 5,)
    ax3.plot(*Mop_points, color='red',linewidth = 2.5)
    ppline.append(pline)
    ax3.plot(xd_out, yd_out, 'bo-')
#    ax3.axis([-0.2,1, None,None])
    plt.ylabel('risetime (s)',fontsize = 'large')
    plt.xlabel('overshoot ratio',fontsize = 'large')
def redraw_ax3_ISE():
    ax3= fig.add_subplot(233)
    pline = ax3.plot(ISE_out, tr_out, 'wo',picker = 5,)
    ppline.append(pline)
    ax3.plot(Bxd_out, Byd_out, 'bo-')
    plt.ylabel('risetime (s)',fontsize = 'large')
    plt.xlabel('ISE',fontsize = 'large') 
def redraw_ax4():
    ax4 = fig.add_subplot(212)
    ax4.plot(t,Y[-1],tpr[-1],((por[-1] + 1)*SP),'ro',linewidth = 2.0)
    ax4.axhline(y=SP,color ='black',linestyle ='--')
    rr = np.linspace(0,SP)
    yy = [tr[-1]]*len(rr)
    ax4.plot(yy,rr,'k--')
    plt.ylabel('y',fontsize = 12)
    plt.xlabel('time (s)',fontsize = 12)    
    plt.axis([0,tfinal, 0,SP*2]) 
    
#################################### Handles clicks on objective plot(ax3) ##############################     
class Pareto_window:

    def __init__(self):
        self.clickcount = 0
        
        self.selected,  = ax3.plot(None, None, 'o', ms=12, alpha=0.4,
                                      color='yellow', visible=False)
        self.correspond, = ax1.plot(None, None,'o',ms = 13,alpha = 0.5,color = 'yellow',visible= False)
          
      
    def pareto_point( self, event):
        
        if ax3.contains(event.mouseevent)[0] == True:
            NW = len(event.ind)
            if not NW: return True
            x = event.mouseevent.xdata
            y = event.mouseevent.ydata
            radius = np.hypot(x-por[event.ind], y-tr[event.ind])
            minind = radius.argmin()
            pstn = event.ind[minind]
            self.clickcount = pstn
            self.redraw()

    def redraw(self):
        
        kc1,ti1= np.array(kc),np.array(ti)
        if self.clickcount is None: return
        pstn = self.clickcount
        self.selected.set_visible(True)
        self.selected.set_data(por[pstn], tr[pstn])
        self.correspond.set_visible(True)
        goodpoints = np.array(goodpoints_out)[0]
        self.correspond.set_data([(ti1[goodpoints])[pstn]],[(kc1[goodpoints])[pstn]])
        yt = Y[pstn]
        ax4 = fig.add_subplot(212)
        ax4.cla()
        plt.ylabel('y',fontsize = 12)
        plt.xlabel('time (s)',fontsize = 12)
        ax4.plot(t,yt,tpr[pstn],((por[pstn] + 1)*SP),'ro')
        ax4.axhline(y=SP,color ='black',linestyle ='--')
        rr = np.linspace(0,SP)
        yy = [tr[pstn]]*len(rr)
        ax4.plot(yy,rr,'k--')
        fig.canvas.draw()
        self.pareto_point()
           
Pclick = Pareto_window() 
   
fig.canvas.mpl_connect('pick_event',Pclick.pareto_point ) 

############################ Draws and enables dragging points on 'kc vs td' plot(ax2) ###################################
class PolygonInteractor:
    """
    An polygon editor.

    Key-bindings

      't' toggle vertex markers on and off.  When vertex markers are on,
          you can move them, delete them

      'd' delete the vertex under point

      'i' insert a vertex at point.  You must be within epsilon of the
          line connecting two existing vertices

    """

    showverts = True
    epsilon = 5  # max pixel distance to count as a vertex hit

    def __init__(self, ax, poly):
    
        if poly.figure is None:
            raise RuntimeError('You must first add the polygon to a figure or canvas before defining the interactor')
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly
        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y, marker='o', markerfacecolor='r', animated=True)
        self.ax.add_line(self.line)
        
        cid = self.poly.add_callback(self.poly_changed)
        self._ind = None # the active vert

        canvas.mpl_connect('draw_event', self.draw_callback)
        canvas.mpl_connect('button_press_event', self.button_press_callback)
        canvas.mpl_connect('key_press_event', self.key_press_callback)
        canvas.mpl_connect('button_release_event', self.button_release_callback)
        canvas.mpl_connect('motion_notify_event', self.motion_notify_callback)
        self.canvas = canvas


    def draw_callback(self, event):
        self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)
        self.canvas.blit(self.ax.bbox)

    def poly_changed(self, poly):
        if self.ax.contains(event)[0] == True:
            'this method is called whenever the polygon object is called'
            # only copy the artist props to the line (except visibility)
            vis = self.line.get_visible()
            Artist.update_from(self.line, poly)
            self.line.set_visible(vis)  # don't use the poly visibility state


    def get_ind_under_point(self, event):
        if self.ax.contains(event)[0] == True:
            'get the index of the vertex under point if within epsilon tolerance'
    
            # display coords
            xy = np.asarray(self.poly.xy)
            xyt = self.poly.get_transform().transform(xy)
            xt, yt = xyt[:, 0], xyt[:, 1]
            d = np.sqrt((xt-event.x)**2 + (yt-event.y)**2)
            indseq = np.nonzero(np.equal(d, np.amin(d)))[0]
            ind = indseq[0]
    
            if d[ind]>=self.epsilon:
                ind = None
    
            return ind

    def button_press_callback(self, event):
        if self.ax.contains(event)[0] == True:
            'whenever a mouse button is pressed'
            if not self.showverts: return
            if event.inaxes==None: return
            if event.button != 1: return
            self._ind = self.get_ind_under_point(event)

    def button_release_callback(self, event):
        if self.ax.contains(event)[0] == True:
            'whenever a mouse button is released'
            if not self.showverts: return
            if event.button != 1: return
            self._ind = None
            

    def key_press_callback(self, event):
        if self.ax.contains(event)[0] == True:
            'whenever a key is pressed'
            if not event.inaxes: return
            if event.key=='t':
                self.showverts = not self.showverts
                self.line.set_visible(self.showverts)
                if not self.showverts: self._ind = None
            elif event.key=='d':
                ind = self.get_ind_under_point(event)
                if ind is not None:
                    self.poly.xy = [tup for i,tup in enumerate(self.poly.xy) if i!=ind]
                    self.line.set_data(zip(*self.poly.xy))
            elif event.key=='i':
                xys = self.poly.get_transform().transform(self.poly.xy)
                p = event.x, event.y # display coords
                for i in range(len(xys)-1):
                    s0 = xys[i]
                    s1 = xys[i+1]
                    d = dist_point_to_segment(p, s0, s1)
                    if d<=self.epsilon:
                        self.poly.xy = np.array(
                            list(self.poly.xy[:i]) +
                            [(event.xdata, event.ydata)] +
                            list(self.poly.xy[i:]))
                        self.line.set_data(zip(*self.poly.xy))
                        break
        self.canvas.draw()


    def motion_notify_callback(self, event):
        if self.ax.contains(event)[0] == True:
            'on mouse movement'
            if not self.showverts: return
            if self._ind is None: return
            if event.inaxes is None: return
            if event.button != 1: return
            x,y = event.xdata, event.ydata
            self.poly.xy[self._ind] = x,kc[self._ind]
            self.line.set_data(zip(*self.poly.xy))
            self.canvas.restore_region(self.background)
            self.ax.draw_artist(self.poly)
            self.ax.draw_artist(self.line)
            self.canvas.blit(self.ax.bbox)
            td[self._ind] = event.xdata
            polyx[:], ployy[:] = zip(*self.poly.xy)
            self.ax.cla()

################################ Handles clicking on the 'kc and ti' plot(ax1) ##############################      
class Parameter_window:
    def __init__(self):
          self.ax1 = redraw_ax1
          self.ax3 = redraw_ax3
          self.ax4 = redraw_ax4
          self.fig = fig
          self.l2 = 0
          self.selectedtc, = ax1.plot(None,None,'o',ms = 13,alpha = 0.5,color = 'orange',visible= False)
          self.correspondtc,=ax2.plot(None, None, 'o', ms=12, alpha=0.4,
                                      color='orange', visible=False)

    def pick( self, event):
        if ax1.contains(event)[0] == True:
            # Clearing all plots
            ax1.cla()
            ax3.cla()
            ax4.cla()
            if ax1.contains(event)[0] == True:
                plot1_x = event.xdata
                plot1_y = event.ydata
                self.Stability_evaluation( plot1_x, plot1_y)
            
     
    def Stability_evaluation( self, p1, p2):
        global t,u,entries
        t = np.arange(0, tfinal, dt)
        entries = len(t)
        u = func.Step(t,step_time,SP) 
        kc.append( p2)
        ti.append( p1)
        td.append(0)
#        print GP_n,Gp_d,tfinal,dt,DT,SP,step_time,ramp_time,SP_input
        polyx.append(0)
        ployy.append(kc[-1])
        poly = Polygon(list(zip(polyx, ployy)), animated=True)
        ax2.add_patch(poly)
        p = PolygonInteractor(ax2, poly)
        print GP_n,Gp_d,tfinal,dt,DT,SP,step_time,ramp_time,SP_input
        Gc_n = [kc[-1]*ti[-1]*td[-1],(kc[-1]*ti[-1]),kc[-1]]
        Gc_d = [ti[-1],0]
        OL_TF_n = np.polymul( Gp_n, Gc_n)
        OL_TF_d = np.polymul( Gc_d, Gp_d)
        CL_TF_n = OL_TF_n
        CL_TF_d = np.polyadd( OL_TF_d, OL_TF_n)
        (A,B,C,D) =signal.tf2ss( OL_TF_n, OL_TF_d)
        (A_CL,B_CL,C_CL,D_CL) =signal.tf2ss( CL_TF_n, CL_TF_d)
        rootsA = np.array( linalg.eigvals( A_CL))
        if (rootsA.real < 0).all():
            sim_results = Euler(A,B,C,D,t,u,DT)
            Y.append(sim_results)
        else:
            show_popup('system is unstable')
            Y.append(np.NaN)
            kc[-1] = np.NaN
            ti[-1] = np.NaN
            
        self.Data_distillation(Y,kc,ti,por,tpr,tr,ISE,IAE,ITAE)  
        
   
    def Data_distillation(self,Y,kc,ti,por,tpr,tr,ISE,IAE,ITAE):
        num = np.shape(Y)[0]
        por1,tpr1 = obj.overshoot(t,Y,num,entries,SP)
        por.append(por1[-1])
        tpr.append(tpr1[-1])
        tr1= obj.risetime(t,Y,num,entries,SP)
        ISE1 = obj.ISE(t,Y,num,entries,SP)
        ISE.append(ISE1[-1])
        IAE1 = obj.IAE(t,Y,num,entries,SP)
        IAE.append(IAE1[-1])
        ITAE1 = obj.ITAE(t,Y,num,entries,SP)
        ITAE.append(ITAE1[-1])
        tr.append(tr1[-1])
        SSoffset = np.isneginf(por)
        SSoffset_out[0] = SSoffset
        UNSTABLE = np.isnan(por)
        UNSTABLE_out[0] = UNSTABLE
        
        goodpoints = ~(np.isnan(tr) | np.isnan(por) | np.isneginf(por))

        goodpoints_out[0] = goodpoints
        z = len(kc)
        idx = np.arange(0,z)
        tr = np.array(tr)[goodpoints]
        por = np.array(por)[goodpoints]
        por_out[0], tr_out[0]  = por, tr
        tpr = np.array(tpr)[goodpoints]

        ISE = np.array(ISE)[goodpoints]
        IAE = np.array(IAE)[goodpoints]
        ITAE = np.array(ITAE)[goodpoints]
        ISE_out[0], IAE_out[0], ITAE_out[0] = ISE, IAE, ITAE 
        idx = idx[goodpoints]
        
        Y = np.array(Y)[goodpoints]
        # Pareto for differents objectives
        # risetime vs overshoot ratio         
        p = pareto.domset([itemgetter(1), itemgetter(2)], zip(idx, por, tr))
        front = p.data
        idx, xd, yd = map(np.array, zip(*front))
        idx_out[0], xd_out[0], yd_out[0] = idx, xd, yd
        sortidx = np.argsort(xd)
        xd = xd[sortidx]
        yd = yd[sortidx]
        # risetime vs ISE
        B = pareto.domset([itemgetter(1), itemgetter(2)], zip(idx, ISE, tr)) 
        Bfront = B.data
        Bidx, Bxd, Byd = map(np.array, zip(*Bfront))
        Bidx_out[0], Bxd_out[0], Byd_out[0] = Bidx, Bxd, Byd
        sortidx = np.argsort(Bxd)
        Bxd = Bxd[sortidx]
        Byd = Byd[sortidx]
        self.re_draw()
        

    def re_draw(self):
        
        self.ax1()
        # Objective plot (ax3)
        self.ax3()
        
        # Systems response plot (ax4)
        self.ax4()
        fig.canvas.draw() 

click = Parameter_window()
fig.canvas.mpl_connect('button_press_event',click.pick )

######################################### Buttons ######################################################
# System change button 
def step_window(self):
    global GP_n,Gp_d,tfinal,dt,DT,SP,step_time,ramp_time,SP_input
    GP_n,Gp_d,tfinal,dt,DT,SP,step_time,ramp_time,SP_input = sys_setup()

System = plt.axes([0.25, .92, 0.1, 0.05])
sysbutton = Button(System, 'System Setup')
sysbutton.on_clicked(step_window)

# Initial point generation
def Point_gen(self):
    return
#    global kc,ti,td
#    kc,ti,td  = func.RPG(20,3) 
#    redraw_ax3()
#    fig.canvas.draw()
#
Ppoints = plt.axes([0.125, .92, 0.1, 0.05])
pointbutton = Button(Ppoints, 'Generate')
pointbutton.on_clicked(Point_gen)
     
# Mopsocd Button
def Opt(self):
     global Mop_points
     Mop_points = Optimize(tfinal, dt, Gp_n, Gp_d, SP, DT,u)
     redraw_ax3()
     fig.canvas.draw()
     
Mopsocd = plt.axes([0.75, .92, 0.1, 0.05])
Mop_button = Button(Mopsocd, 'Mopso-cd')
Mop_button.on_clicked(Opt)
    

# Objective radio button
axcolor = 'lightgreen'
rax = plt.axes([0.91, 0.6, 0.07, 0.15])
radio = RadioButtons(rax, ('RT vs OSR', 'ISE','IAE','ITAE'))
def colorfunc(label):
    if label == 'RT vs OSR':
        redraw_ax1()
        redraw_ax3()
        redraw_ax4()
    if label == 'ISE':
        redraw_ax3_ISE()
        redraw_ax1()
        redraw_ax4()
    plt.draw()
radio.on_clicked(colorfunc)
    
plt.show()