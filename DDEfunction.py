# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:12:13 2013

@author: Rowly
"""

#from scipy import *
import numpy as np
import PyDDE.pydde as p
#import matplotlib.pyplot as plt


from scipy import linalg
from scipy import signal
#from plotgraphs import * 
#import MODminifunc as func
#from Tuners import*
#Gp_n = [1]       
#Gp_d = [1,3,3,8]
def DDE(Tf_n,Tf_d,t,TD,u):
    (A,B,C,D) =signal.tf2ss(Tf_n,Tf_d)
#    print A
    def ddegrad(s,c,t):
            NOFDE = len(A[0,:])
            lag = np.zeros(NOFDE)
            if (t>TD):
                for l in np.arange(0, NOFDE):
                    lag[l] = np.array(p.pastvalue(l,t-TD,0))
            gradvec= np.zeros(NOFDE)
            print lag
            if NOFDE == 1:
                gradvec[0] = c[-1]+c[0]*lag[0]
#                print 'First order'
    
            else:    
                for i in np.arange(0,NOFDE):
#                    print 'gradvec loop'
                    if i == 0:
                        gradvec[i] = s[i] 
                    elif i == NOFDE-1:
                         
                         last_entry = np.zeros(NOFDE+1)
                         rc = NOFDE+1
                         for k in np.arange(0,len(last_entry)):
#                             print 'Last entry loop'
                             if k == 0:
                                 last_entry[k] = c[-1]
                             elif k > 0:
    #                             print lag[k-1],s[k-1]
                                 last_entry[k] = c[k-1]*lag[k-1]
                             rc -=1
                             a = sum(last_entry)
#                             print 'Last entry successfully calculated'
                         gradvec[i] = a
#            print 'exiting grad'             
            return np.array(gradvec)
    def ddesthist(g, s, c, t):
        return (s, g)        
        
    ode_eg = p.dde()
        
        
        # Setting up constants
    cons = np.zeros(len(A[0,:])+1)
        
    for i in range(0,len(A[0,:])+1):
                if i<len(A[0,:]):
                    cons[i] = A[0,i]
                    
                elif i ==(len(A[0,:])):
                    cons[i] = C[0,-1]
        
    odecons = np.array(cons)
#    print odecons
    ini_values = np.zeros(len(A[0]))
    odeist = np.array(ini_values)
    n = len(A[0])
    
    ode_eg.initproblem(no_vars=n, no_cons=len(odecons), nlag=1, nsw=0,
                           t0=0.0, t1=t[-1],
                           initstate=odeist, c=odecons, otimes=t,
                           grad=ddegrad,storehistory=ddesthist)
        
    odestsc = np.array([0,0])
        
    ode_eg.initsolver(tol=1*10**(-8), hbsize=1000,
                          dt=t[1], 
                          statescale=odestsc)
        
    ode_eg.solve()
    yDDE = 1*(ode_eg.data[:,-1])
#    plt.plot(ode_eg.data[:,0],ode_eg.data[:,1:])
#    plt.show()   
#    print yDDE
    return yDDE
#print ode_eg.data