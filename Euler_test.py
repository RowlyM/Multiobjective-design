# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\Rowly\.spyder2\.temp.py
"""

import matplotlib.pyplot as plt

from scipy import *
from numpy import*
import PyDDE.pydde as p
import matplotlib.pyplot as plt
from scipy import signal



Gp_n = [1]       
Gp_d = [1,1]
Gc_n = [3]
Gc_d = [1]
OL_TF_n = polymul(Gp_n,Gc_n)
OL_TF_d = polymul(Gc_d,Gp_d)

(A,B,C,D) =signal.tf2ss(OL_TF_n,OL_TF_d) 

SP = 2
print A,B,C,D
y = lambda(t):-C[0]*SP/A[0]*(1-e**(A[0]*t))

def dydt(SV):    
   return  (A[0]*SV+(SP)) 
   
dt = 0.001
SS = 0
Et = arange(0,10, dt)
Ey = zeros(len(Et))

for i in range(0,len(Et)):
    SS = SS + dt*(dydt(SS))
    Ey[i] = C[0]*SS
    
def dydtd(SV,SVd):
   return  (A[0]*SV+B[0]*(SP-SVd))
  
SS = 0
SSd = 0
DT =.5
SSt = zeros(len(Et))
Eyd = zeros(len(Et))

for k in range(0,len(Et)):
    SS = SS + dt*(dydtd(SS,SSd))
    Eyd[k] = SS*C[0]
    SSt[k] = SS*C[0]
    if DT == 0:
        print 
        SSd = SSt[k]
    else:
        if Et[k]<=DT:
            Eyd[k]=0
        elif (Et[k]>DT):
            Eyd[k] = interp(Et[k]-DT,Et,SSt)
        SSd = Eyd[k] 
def ddegrad(s,c,t):
    grad = SP*c[1]+s[0]*c[0]
    return array([grad])

def ddegradd(s,c,t):
    if DT == 0:
       g = (SP-s[0])*c[1]+s[0]*c[0]
    else:
        if t<=(DT):
            g = 0
        else: 
            if t>(DT):
                alag = p.pastvalue(0,t-(DT),0)
            g =(SP-alag)*c[1]+s[0]*c[0]
    return array([g]) 
    
def ddesthist(g, s, c, t):
    return (s, g)
    
def ddesthistd(g, s, c, t):
    return (s, g)      

ode_eg = p.dde()
ode_egd = p.dde()
odeist = [0]  
odecons = [A[0],C[0]]
print odecons
ode_eg.initproblem(no_vars=1, no_cons=len(odecons), nlag=1, nsw=0,
                       t0=0.0, t1=Et[-1],
                       initstate=odeist, c=odecons, otimes=Et,
                       grad=ddegrad, storehistory=ddesthist)
    
odestsc = array([0])
  
ode_eg.initproblem(no_vars=1, no_cons=len(odecons), nlag=1, nsw=0,
                       t0=0.0, t1=Et[-1],
                       initstate=odeist, c=odecons, otimes=Et,
                       grad=ddegrad, storehistory=ddesthist)
                       
ode_egd.initproblem(no_vars=1, no_cons=len(odecons), nlag=1, nsw=0,
                       t0=0.0, t1=Et[-1],
                       initstate=odeist, c=odecons, otimes=Et,
                       grad=ddegradd, storehistory=ddesthistd)
#    
ode_eg.initsolver(tol=1*10**(-8), hbsize=1000,
                      dt=Et[1], 
                      statescale=odestsc)
                      
ode_egd.initsolver(tol=1*10**(-8), hbsize=1000,
                      dt=Et[1], 
                      statescale=odestsc)
ode_eg.solve()
ode_egd.solve()
#print ode_eg.data
plt.figure('Euler')
plt.plot(Et,Ey,Et,y(Et),Et,Eyd)
plt.figure('PyDDE')
plt.plot(ode_eg.data[:,0],ode_eg.data[:,1],ode_eg.data[:,0],ode_egd.data[:,1])
plt.show()  