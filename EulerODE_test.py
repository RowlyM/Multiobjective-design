# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 11:13:54 2013

@author: Rowly
"""
import numpy as np
from scipy import signal
from scipy import interp
from MODminifunc import mirror
import matplotlib.pyplot as plt

Gp_n = [4,2,4]       
Gp_d = [1,3,3,1]
Gc_n = [1]
Gc_d = [1]
OL_TF_n = np.polymul(Gp_n, Gc_n)
OL_TF_d = np.polymul(Gc_d,Gp_d)
SP =2.
(A,B,C,D) =signal.tf2ss(OL_TF_n, OL_TF_d)
print A,B,C,D
cons = np.zeros((2,len(A)))
A = mirror(A[0])
C =  mirror(C[0])         

NODEs = len(A[0:])
def dydt(SV,SVm):
    NODEs = len(A[0:])    
    ODEs = np.zeros(NODEs) 
    for s in range(0,NODEs):
        if s<(NODEs-1):
            ODEs[s] = SV[s+1]
            
        elif s == (NODEs-1):
            ODEs[s] = (SP-SVm)+np.dot(SV,A)
    return (ODEs)
    
SS = np.zeros(NODEs) 
SVm = 0.
dt = 0.001
DT = 0 
Et = np.arange(0,10, dt)
Ey = np.zeros(len(Et))
SV_save = np.zeros(len(Et))

for i in range(0,len(Et)):
    SS = SS + dt*np.array((dydt(SS,SVm)))
    Ey[i] = np.dot(C,SS)
    SV_save[i] = Ey[i]
    
    if DT == 0:
        Ey[i] = SV_save[i]
    else:
        if Et[i]<= DT:
            Ey[i] =0
        elif (Et[i]>DT):
            Ey[i]= interp(Et[i]-DT,Et,SV_save)
    SVm = Ey[i]
        
plt.plot(Et,Ey)   
plt.show()    
    
   
    
    
    