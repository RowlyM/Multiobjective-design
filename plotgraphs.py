# -*- coding: utf-8 -*-
# accept x matrix(num,entries) where entries : values from one set of tuning consts

def plotgraphs(kc,ti,x,num,entries,t,tfinal,dt,SP,kcst,tist):
    import numpy as np
    import matplotlib.pyplot as plt
    from operator import itemgetter
    import pareto
# calulates the overshoot ratio
    def overshoot(x,num,SP,entries,t):
        tpr = np.zeros(num)
        por = np.zeros(num)
        for u in range(0,num):
            if (x[:][u]== None):
                por[u]= None
                tpr[u] = None
            else:
                por[u] = ((np.max(x[:][u]))- SP)/SP
                for g in range(0,entries):
                    if x[u][g] ==np.max(x[:,u]):
                        tpr[u] = t[g]
                       
                    if por[u] < 0:
                        por[u] = np.NINF
                        tpr[u] = np.NINF
        return {'por':por ,'tpr':tpr}
    por2 = overshoot(x,num,SP,entries,t)
    por = por2['por']
    tpr = por2['tpr']
    
 # calculates the risetime
    def risetime(x,num,entries,SP,t): 
        tr = np.zeros(num)
        for j in range(0,num):
            if (np.isnan(x[j][:])).all()== True:
                tr[j] = None 
            else:
                for k in range(0, entries-1):    
                    if np.sign(SP - x[j][k])!= np.sign(SP - x[j][k+1]): # added a equals sign
                        if np.sign(SP - x[j][k])==0:                 
                            tr[j] = t[k]
                        else :
                            tr[j] = np.interp(SP,[x[j][k],x[j][k+1]],[t[k],t[k+1]])
                        break
        return tr
    tr= risetime(x,num,entries,SP,t)
    SSoffset = ~np.isneginf(por)
    UNSTABLE =~np.isnan(por)  
         
#   Added more objectives to the project

# plots the graphs
    goodpoints = ~(np.isnan(tr)| np.isnan(por)|np.isneginf(por))
    idx = np.arange(0,num)
    tr = tr[goodpoints]
    por = por[goodpoints]
    tpr = tpr[goodpoints]
    idx = idx[goodpoints]
    x = x[goodpoints]
    zns = len(por)
    p = pareto.domset([itemgetter(1), itemgetter(2)], zip(idx, por, tr))
   
    front = p.data
    idx, xd, yd = map(np.array, zip(*front))
    sortidx = np.argsort(xd)
    xd = xd[sortidx]
    yd = yd[sortidx]  
    fig = plt.figure()
    fig.set_facecolor('white')
    font = {'family' : 'cambria', 
        'weight' : 'normal', 
        'size'   : 14} 
 
    plt.matplotlib.rc('font', **font)
    
    ax1 = fig.add_subplot(2,2,1)
    linea = ax1.plot(kc[~UNSTABLE],ti[~UNSTABLE], 'w.')
#    lineb = ax1.plot(kcst,tist,'k-')
    
    linee = ax1.plot(kc[~SSoffset],ti[~SSoffset],'g+')
    line1, = ax1.plot(kc[goodpoints], ti[goodpoints], 'wo',picker = 5,)
    linec = ax1.plot(kc[idx], ti[idx],'ro')
    lined = ax1.plot(kc[num-2],ti[num-2],'ks') # Ziegler Nichos settings
    lineco = ax1.plot(kc[num-1],ti[num-1],'gs') # Cohen coon settings
    linetl = ax1.plot(kc[num-3],ti[num-3],'ms') # tyreas n Luyben settings
    plt.xlabel(r'$K_C$',fontsize = 'large')
    plt.ylabel(r'$\tau_I$',fontsize = 'large')
    ax2= fig.add_subplot(2,2,2)
    line2, =ax2.plot(por, tr, 'wo',picker = 5,)
    
    line222=ax2.plot(xd, yd, 'ro-')
    line22 = ax2.plot(por[zns-2],tr[zns-2],'ks')
    linecc2 = ax2.plot(por[zns-1],tr[zns-1],'gs') # cohen coon settings
#    plt.setp((linea,lineb,linee,line1),linewidth = 2.0)
#    plt.figlegend((linea,lineb,linec,lined,lineco,linetl,linee,line1),('Unstable','Stabilty limit','Pareto points','Z&N settings','Cohen Coon','Tyreus & Luyben','S/S offset','Stable'),'upper right',borderaxespad=0.)
    plt.axis([-0.2,1, 0,40])
    plt.ylabel('risetime (s)',fontsize = 'large')
    plt.xlabel('overshoot ratio',fontsize = 'large')
    ax3 = fig.add_subplot(2,1,2)
    plt.ylabel('x',fontsize = 12)
    plt.xlabel('time (s)',fontsize = 12)
    plt.axis([0,tfinal, 0,SP*2]) ### 
    ax3.text(0.02,0.5,'Click on the overshoot vs risetime plot to obtain the time response',fontsize = 13,color = 'red')
     
# graphical interaction 
    class timeresponse:
        def __init__(self):
            self.lastind = 0
            
            self.selected,  = ax2.plot([por[0]], [tr[0]], 'o', ms=12, alpha=0.4,
                                          color='yellow', visible=False)
            self.correspond, = ax1.plot([(kc[goodpoints])[0]],[(ti[goodpoints])[0]],'o',ms = 13,alpha = 0.5,color = 'yellow',visible= False)
            
        def onpick(self,event):
            if event.artist!=line2:
                self.correspond.set_visible(False)
                self.selected.set_visible(False)
                return True
            NW = len(event.ind)
            if not NW: return True
        
            x = event.mouseevent.xdata
            y = event.mouseevent.ydata
            radius = np.hypot(x-por[event.ind], y-tr[event.ind])
            minind = radius.argmin()
            
            pstn = event.ind[minind]
            self.lastind = pstn
            
            self.update()
       
        def update(self):
            if self.lastind is None: return
            pstn = self.lastind
            self.selected.set_visible(True)
            self.selected.set_data(por[pstn], tr[pstn])
            self.correspond.set_visible(True)
            self.correspond.set_data([(kc[goodpoints])[pstn]],[(ti[goodpoints])[pstn]])
            t = np.arange(0, tfinal, dt)
            yt = x[pstn]
            ax3.cla()
            plt.ylabel('y',fontsize = 12)
            plt.xlabel('time (s)',fontsize = 12)
            plt.axis([0,tfinal, 0,SP*2]) #####Change of response graph y-axis
            ax3.plot(t,yt,tpr[pstn],((por[pstn] + 1)*SP),'ro')
            ax3.axhline(y=SP,color ='black',linestyle ='--')
            rr = np.linspace(0,SP)
            yy = [tr[pstn]]*len(rr)
            ax3.plot(yy,rr,'k--')
            fig.canvas.draw()
            return True
            
    time = timeresponse()
    fig.canvas.mpl_connect('pick_event', time.onpick)
    
    
    class kctiinteract(timeresponse):
          def __init__(self):
              self.l2 = 0
              self.selectedtc, = ax1.plot([(kc[goodpoints])[0]],[(ti[goodpoints])[0]],'o',ms = 13,alpha = 0.5,color = 'orange',visible= False)
              self.correspondtc,=ax2.plot([por[0]], [tr[0]], 'o', ms=12, alpha=0.4,
                                          color='orange', visible=False)
          def onpick(self,event):
              if event.artist!=line1:
                  self.correspondtc.set_visible(False)
                  self.selectedtc.set_visible(False)                  
                  return True
              NW2 = len(event.ind)
              if not NW2: return True
              x = event.mouseevent.xdata
              y = event.mouseevent.ydata
              r2 = np.hypot(x-(kc[goodpoints])[event.ind], y-(ti[goodpoints])[event.ind])
              m2 = r2.argmin()
              p2 = event.ind[m2]
              self.l2 = p2
              self.update()
          def update(self):
            if self.l2 is None: return
            p2 = self.l2
            self.selectedtc.set_visible(True)
            self.selectedtc.set_data([(kc[goodpoints])[p2]],[(ti[goodpoints])[p2]])
            self.correspondtc.set_visible(True)
            self.correspondtc.set_data(por[p2], tr[p2])
            t = np.arange(0, tfinal, dt)
            yt = x[p2]
            ax3.cla()
            plt.ylabel('x')
            plt.xlabel('time (s)')
            plt.axis([0,tfinal, 0,SP*2]) #######
            ax3.plot(t,yt,tpr[p2],((por[p2] + 1)*SP),'ro',linewidth = 2.0)
            ax3.axhline(y=SP,color ='black',linestyle ='--')
            rr = np.linspace(0,SP) ##########
            yy = [tr[p2]]*len(rr)
            ax3.plot(yy,rr,'k--')
         
            fig.canvas.draw()
            return True
    tim = kctiinteract()
    fig.canvas.mpl_connect('pick_event', tim.onpick)
    plt.show()

