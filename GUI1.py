# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:20:51 2013

@author: Rowly
"""
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter
import objectives as obj
import pareto
from scipy import signal
from scipy import linalg
from EulerODE import Euler
import MODminifunc as func
#import matplotlib.backend_bases as bb
Gp_n = [1]       
Gp_d = [1,5,6]
SP = 2.                   # Set Point            
tfinal = 100        # simulation period
dt = .1
DT = 1       # Dead time (s)  
t = np.arange(0, tfinal, dt)
entries = len(t)

SP_input = 'step'           # Choose Set point input by typing 'step' or 'ramp'
step_time  = 0
ramp_time = 5.
#u = func.Ramp(t,ramp_time,SP)
u = func.Step(t,step_time,SP)           
SP_info = [SP_input,step_time, ramp_time,SP]

#plot1
fig=plt.figure()
ax1 = fig.add_subplot(2,2,1)
plt.axis([0,20, 0,30])
ax1.plot(None,None)
plot1_x =[]
plot1_y =[]
kc = []
ti = []
td = [0]
plt.xlabel(r'$K_C$',fontsize = 'large')
plt.ylabel(r'$\tau_I$',fontsize = 'large')

#plot2
ax2= fig.add_subplot(2,2,2)
plt.axis([-0.2,1, 0,40])
plt.ylabel('risetime (s)',fontsize = 'large')
plt.xlabel('overshoot ratio',fontsize = 'large')
por = []

tpr = []
tr = []
#plot3
ax3 = fig.add_subplot(2,1,2)
plt.ylabel('y',fontsize = 12)
plt.xlabel('time (s)',fontsize = 12)
plt.axis([0,tfinal, 0,SP*2]) ### 
ax3.text(0.02,SP,'Click on the ti vs kc plot to obtain the time response',fontsize = 13,color = 'red')
Y =[]

class Parameter_window():
    def pick( self, event):
        plot1_x.append( event.xdata)
        plot1_y.append( event.ydata)
        self.Stability_evaluation( plot1_x[-1], plot1_y[-1])
        
    def Stability_evaluation( self, p1, p2):
        kc.append( p1)
        ti.append( p2)
        Gc_n = [kc[-1]*ti[-1]*td[-1],(kc[-1]*ti[-1]),kc[-1]]
        Gc_d = [ti[-1],0]
        OL_TF_n = np.polymul( Gp_n, Gc_n)
        OL_TF_d = np.polymul( Gc_d, Gp_d)
        CL_TF_n = OL_TF_n
        CL_TF_d = np.polyadd( OL_TF_d, OL_TF_n)
        (A,B,C,D) =signal.tf2ss( OL_TF_n, OL_TF_d)
        (A_CL,B_CL,C_CL,D_CL) =signal.tf2ss( CL_TF_n, CL_TF_d)
        rootsA = np.array( linalg.eigvals( A_CL))
#        print rootsA
        if (rootsA.real < 0).all():
            sim_results = Euler(A,B,C,D,t,u,DT)
            Y.append(sim_results)
        else:
            print 'unstable point'
            Y.append(np.NaN)
            kc[-1] = np.NaN
            ti[-1] = np.NaN
        self.Data_distillation(Y,kc,ti,por,tpr,tr)  
   
    def Data_distillation(self,Y,kc,ti,por,tpr,tr):
        num = np.shape(Y)[0]
        por1,tpr1 = obj.overshoot(t,Y,num,entries,SP)

        por.append(por1[-1])
        tpr.append(tpr1[-1])

        tr1= obj.risetime(t,Y,num,entries,SP)
        tr.append(tr1[-1])
        SSoffset = ~np.isneginf(por)
        UNSTABLE = ~np.isnan(por)
        goodpoints = ~(np.isnan(tr) | np.isnan(por) | np.isneginf(por))
#        print goodpoints
        z = len(kc)
        idx = np.arange(0,z)
        tr = np.array(tr)[goodpoints]
        por = np.array(por)[goodpoints]
        tpr = np.array(tpr)[goodpoints]

#        ISE = ISE[goodpoints]
        idx = idx[goodpoints]
        Y= np.array(Y)[goodpoints]            
        p = pareto.domset([itemgetter(1), itemgetter(2)], zip(idx, por, tr))
        
        front = p.data
        idx, xd, yd = map(np.array, zip(*front))
        sortidx = np.argsort(xd)
        xd = xd[sortidx]
        yd = yd[sortidx]
        self.re_draw(Y,kc,ti,xd,yd,por,tr,goodpoints,SSoffset,idx)
        
         
        
    def re_draw(self,Y,kc,ti,xd,yd,por,tr,goodpoints,SSoffset,idx):
        kc,ti= np.array(kc),np.array(ti)
        ax1.cla()
        ax2.cla()
        ax3.cla()
        ax1.plot(kc[~SSoffset],ti[~SSoffset],'g+') 
        ax1.plot(kc[goodpoints], ti[goodpoints], 'wo',picker = 5,) # adds good points
        ax1.plot(kc[idx], ti[idx],'bo') # from pareto.data
        ax1.axis([0,20, 0,30])
        ax2.plot(por, tr, 'wo',picker = 5,)
        ax2.plot(xd, yd, 'bo-')
        ax2.axis([-0.2,1, 0,40])
        plt.ylabel('risetime (s)',fontsize = 'large')
        plt.xlabel('overshoot ratio',fontsize = 'large')
        ax3.plot(t,Y[-1],linewidth = 2.0)
        plt.ylabel('y',fontsize = 12)
        plt.xlabel('time (s)',fontsize = 12)
        fig.canvas.draw()   
           
click = Parameter_window()

fig.canvas.mpl_connect('button_press_event',click.pick )  

plt.show()