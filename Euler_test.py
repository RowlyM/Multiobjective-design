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


from scipy import linalg
from scipy import signal

Gp_n = [1]       
Gp_d = [1,1]
Gc_n = [15]
Gc_d = [1]
OL_Gp_n = Gp_n
OL_Gp_d = Gp_d 
OL_TF_n = polymul(OL_Gp_n,Gc_n)
OL_TF_d = polymul(Gc_d,OL_Gp_d)
CL_TF_n = OL_TF_n
CL_TF_d = polyadd(OL_TF_d,OL_TF_n)
(A,B,C,D) =signal.tf2ss(CL_TF_n,CL_TF_d) 

SP = 1
#print A,B,C,D
y = lambda(t):-C[0]/A[0]*(1-e**(A[0]*t))

def dydt(SV):    
   return  (C[0]+A[0]*SV) 
   
SS = 0
dt = 0.001
Et = arange(0, 5, dt)
Ey = zeros(len(Et))

for i in range(0,len(Et)):
    SS = SS + dt*(dydt(SS))
    Ey[i] = SS
    
def dydt(SV):  
   return  (C[0]+A[0]*SV)
  
SS = 0
SSd = 0
DT = dt*40
SSt = zeros(len(Et))
Eyd = zeros(len(Et))

for k in range(0,len(Et)):

    SS = SS + dt*(dydt(SSd))
    Eyd[k] = SS
    SSt[k] = SS
    if Et[k]>DT:
        Eyd[k] = interp(Et[k]-DT,Et , SSt)
    else:
        Eyd[k]=0
        
    SSd = Eyd[k] 
##    

#Gp_n = [1]       
#Gp_d = [1,8,5]
#
#(A,B,C,D) =signal.tf2ss(Gp_n,Gp_d )
#print A,B,C,D
#
#def ddegrad(s,c,t):
#    alag = 0
#    if t<=(TD):
#        g = 0
#    else:  
#        if t>(TD):
#            alag = p.pastvalue(0,t-(TD),0)
##            print alag
#        g = c[1]+s[0]*c[0]+(1-alag) 
##        print g
#    return array([g])
#    
#def ddesthist(g, s, c, t):
#    return (s, g)        
##    
#ode_eg = p.dde()
#    
    
#    # Setting up constants
#if len(A[0,:])>len(C[0,:]):
#    C = zeros(len(A[0,:]))
#    for i in range(0,len(C[0,:])):
#        C[i] = C[0,i]
#    
#cons = zeros((2,len(A[0,:])))
##print cons
#
#    
#for i in range(0,2):
#    for j in range(0,len(A[0,:])):
#        if i == 0:
#            cons[i,j] = A[0,j]
#        else:
#            cons[i,j] = C[0,j]
            
#print cons        
#odecons = [A[0],C[0]]
##print odecons
#ini_values =[0]
#odeist = [0,0,0,0,0,0]
##if len(A[0,:])==1:
##    n = 1
##else:
##    n = len(A[0,:])*2-1
##print n
#
#ode_eg.initproblem(no_vars=1, no_cons=len(odecons), nlag=1, nsw=0,
#                       t0=0.0, t1=Et[-1],
#                       initstate=odeist, c=odecons, otimes=Et,
#                       grad=ddegrad, storehistory=ddesthist)
#    
#odestsc = array([0])
#    
#ode_eg.initsolver(tol=1*10**(-8), hbsize=1000,
#                      dt=Et[1], 
#                      statescale=odestsc)
#    
#ode_eg.solve()
##print ode_eg.data
#print Ey  
plt.plot(Et,Ey,Et,y(Et),Et,Eyd)
#plt.plot(Et,y(Et),Et,Ey,ode_eg.data[:,0],ode_eg.data[:,1])
plt.show()  