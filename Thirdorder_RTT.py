# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 21:02:02 2013

@author: Nokukhanya Khwela
         Modified by Rowly Mudzhiba
"""

import numpy as np
from scipy import linalg
from scipy import signal
from plotgraphs import * 
import MODminifunc as func
from Tuners import*
from DDEfunction import DDE

 
# Process Transfer function 
Gp_n = [0.125]       
Gp_d = [1,3,3,1]
                          
# Simulation Settings                          
SP = 4                    # Set Point            
tfinal = 100              # simulation period
dt = 0.1
DT =.5                     # Dead time (s)  
t = np.arange(0, tfinal, dt)
entries = len(t)
num =100              # number of tuning constant sets
x = np.zeros((entries,num))
x2 = np.zeros((entries,num))
por = np.zeros(num)             # What are these two variables?
tr = np.zeros(num)
[k_c,t_i,t_d]  = func.RPG(num,3)     # Random Parameter Generator
                                    # Options: 1= P, 2 = PI, 3 = PID

# Different Ysp inputs
#u = func.Ramp(t,dt,5,SP)             # Choose either of them by commenting the other
u = func.Step(t,SP)

  
# coefficients of the transfer function Gp = kp/(s^3 + As^2 + Bs +C)
A =3
B = 3
C = 1                 # Old process coefficients used in the initial project
kp =0.125 
SP = SP
kcst = np.arange(0,60,dt)

# Relatiopnship btwn kc and Ti obtained through the direct substitution method
tist =kp*kcst*A**2/(((A*B) - C - (kp*kcst))*(C + (kp*kcst)))


kczn ,tizn,tdzn = ZN(Gp_n,Gp_d,t,SP,'PID',dt,DT) # Ziegler-Nichols settings via function ZN
kcch ,tich,tdch = Cohen_Coon(Gp_n,Gp_d,t,SP,'PID',dt,DT)  

## System responce
for k in range(0,num):
    if k==num-1:
        kc = kczn           # Inserting Ziegler-Nicholas parameters
        ti = tizn
        td = tdzn
        
    elif k == num-2:        # Inserting Cohen-Coon parameters
        kc = kcch
        ti = tich
        td = tdch
    else:    
        kc =k_c[k]
        ti = t_i[k]
        td = t_d[k]
        

    if ti == 0:
        Gc_d = 1
        Gc_n = [kc*ti*td,(kc*ti),kc] 
        
    else:    
        Gc_n = [kc*ti*td,(kc*ti),kc]            #New code
        Gc_d = [ti,0] 
        
                                          # The controller and process TFs are entered here                                           # because the process selection interface hasnt been 
                                            # designed.
    OL_TF_n = np.polymul(Gp_n,Gc_n)
    OL_TF_d = np.polymul(Gc_d,Gp_d)
    CL_TF_n = OL_TF_n
    CL_TF_d = np.polyadd(OL_TF_d,OL_TF_n)
    (A,B,C,D) =signal.tf2ss(OL_TF_n,OL_TF_d)      # Open Loop Transfer Function is converted to State Space
    (A_CL,B_CL,C_CL,D_CL) =signal.tf2ss(CL_TF_n,CL_TF_d) # Closed Loop Transfer Function is converted to State Space


    rootsA = np.array(linalg.eigvals(A_CL))
    
#    step_response = signal.lsim((A,B,C,D),u,t,X0=None,interp=1)[1]
    step_responseDDE = DDE(A,B,C,D,t,u,DT,SP)
   
    if (rootsA.real < 0).all():
        for i in range(0,entries):          # Stabilty of the Closed Loop is checked 
#            X = step_response
            X2 = step_responseDDE
#            x[i,k] = X[i]
            x2[i,k] = X2[i]
    else:
#        x[:,k] = np.NaN
        x2[:,k] = np.NaN
#        
    
    k_c[k] = kc
    t_i[k] = ti
    
kc = k_c
ti = t_i
x = x2.T
#x = x.T
#plt.plot(t,x)
#plt.show()

fig = plotgraphs(kc,ti,x,num,entries,t,tfinal,dt,SP,kcst,tist)