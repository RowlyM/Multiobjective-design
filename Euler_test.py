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


SP_input = 'step'
Ramp_time = 2.
Gp_n = [4,2,4]       
Gp_d = [1,3,3,1]
Gc_n = [4]
Gc_d = [1]
OL_TF_n = polymul(Gp_n, Gc_n)
OL_TF_d = polymul(Gc_d,Gp_d)

(A,B,C,D) =signal.tf2ss(OL_TF_n, OL_TF_d)
counter = 0
SP = 2
print A,B,C,D
y = lambda(t):SP*((1./6 + 4./3*e**(-3*t)-2*e**(-2*t)))+1

def dydt(SV,SV1): 
#   print SP,A[0,0]*SV[0],A[0,1]*SV[1] 
   return  (SV[1],SV[2],(SP-SV1)+A[0,2]*SV[0]+A[0,1]*SV[1]+A[0,0]*SV[2]) 
#   
dt = .001
SS = [0,0,0]
SV1 = 0
Et = arange(0,10, dt)
Ey = zeros(len(Et))
#
for i in range(0,len(Et)):
    SS = SS + dt*array((dydt(SS,SV1)))
    Ey[i] = C[0,2]*SS[0]+C[0,1]*SS[1]+C[0,2]*SS[2]
    SV1 = Ey[i]
#def dydtd(SV,SVd):
#   return  (SV[1],SV[2],(SP-SVd)+A[0,2]*SV[0]+A[0,1]*SV[1]+A[0,0]*SV[2])
#  
#SS = 0
#SSd = 0
#DT =0
#SSt = zeros(len(Et))
#Eyd = zeros(len(Et))
#
#for k in range(0,len(Et)):
#    SS = SS + dt*(dydtd(SS,SSd))
#    Eyd[k] = SS*C[0]
#    SSt[k] = SS*C[0]
#    if DT == 0:
#        SSd = SSt[k]
#    else:
#        if Et[k]<=DT:
#            Eyd[k]=0
#        elif (Et[k]>DT):
#            Eyd[k] = interp(Et[k]-DT,Et,SSt)
#        SSd = Eyd[k] 
#def ddegrad(s,c,t):
#    grad = SP*c[1]+s[0]*c[0]
#    return array([grad])
#
#def ddegradd(s,c,t):
##    print 'im in'
#    if SP_input == 'step':
#        if t == 0:
#            Ysp = 0
#        else:
#            Ysp = SP
#    elif SP_input == 'ramp':
#        if t < Ramp_time:
#            Ysp = (SP/Ramp_time)*t
#            print (SP/Ramp_time) 
#        else:
#            Ysp = SP
##            print Ysp
##    print Ysp        
#    if DT == 0:
##       print 'im in here'
#       g = (Ysp-s[0])*c[1]+s[0]*c[0]
#    else:
#        if t<=(DT):
#            g = 0
#        else: 
#            if t>(DT):
#                alag = p.pastvalue(0,t-(DT),0)
#            g =(Ysp-alag)*c[1]+s[0]*c[0]
#
#    return array([g]) 
#    
#def ddesthist(g, s, c, t ):
#    return (s, g)
#    
#def ddesthistd(g, s, c, t):
#    return (s, g)      
#
#ode_eg = p.dde()
#ode_egd = p.dde()
#odeist = [0]  
#odecons = [A[0],C[0]]
#print odecons
#
#ode_eg.initproblem(no_vars=1, no_cons=len(odecons), nlag=1, nsw=0,
#                       t0=0.0, t1=Et[-1],
#                       initstate=odeist, c=odecons, otimes=Et,
#                       grad=ddegrad, storehistory=ddesthist)
#    
#odestsc = array([0])
#  
#ode_eg.initproblem(no_vars=1, no_cons=len(odecons), nlag=1, nsw=0,
#                       t0=0.0, t1=Et[-1],
#                       initstate=odeist, c=odecons, otimes=Et,
#                       grad=ddegrad, storehistory=ddesthist)
#                       
#ode_egd.initproblem(no_vars=1, no_cons=len(odecons), nlag=1, nsw=0,
#                       t0=0.0, t1=Et[-1],
#                       initstate=odeist, c=odecons, otimes=Et,
#                       grad=ddegradd, storehistory=ddesthistd)
##    
#ode_eg.initsolver(tol=1*10**(-8), hbsize=1000,
#                      dt=Et[1], 
#                      statescale=odestsc)
#                      
#ode_egd.initsolver(tol=1*10**(-8), hbsize=1000,
#                      dt=Et[1], 
#                      statescale=odestsc)
#ode_eg.solve()
#ode_egd.solve()
#print ode_eg.data
plt.figure('Euler')
#plt.plot(Et,y(Et),Et,Ey)
plt.plot(Et,Ey)
#plt.figure('PyDDE')
#plt.plot(ode_eg.data[:,0],ode_eg.data[:,1],ode_eg.data[:,0],ode_egd.data[:,1])
plt.show()  