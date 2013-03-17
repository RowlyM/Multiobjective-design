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
#from DDEfunction import DDE
from EulerODE import Euler
from scipy import*
# Process Transfer function 
Gp_n = [1]       
Gp_d = [1,5,6]
                          
# Simulation Settings                          
SP = 2.                   # Set Point            
tfinal = 100        # simulation period
dt = .1
DT =1          # Dead time (s)  
t = np.arange(0, tfinal, dt)
entries = len(t)
num =100           # number of tuning constant sets
y = np.zeros((entries,num))
por = np.zeros(num)             # What are these two variables?
tr = np.zeros(num)

# Controller choice
Contr_type = 'PID'               # Choose controller by typing 'P' , 'PI' or 'PID'
if Contr_type == 'P':
    Controller = 1
elif Contr_type == 'PI':
    Controller = 2
elif Contr_type == 'PID':
    Controller = 3

[k_c,t_i,t_d]  = func.RPG(num,Controller)     # Random Parameter Generator
                                    # Options: 1= P, 2 = PI, 3 = PID

# Different Ysp inputs           
SP_input = 'step'           # Choose Set point input by typing 'step' or 'ramp'
step_time  = 0
ramp_time = 5.
#u = func.Ramp(t,ramp_time,SP)
u = func.Step(t,step_time,SP)           
SP_info = [SP_input,step_time, ramp_time,SP]
  
# coefficients of the transfer function Gp = kp/(s^3 + As^2 + Bs +C)
A =3
B = 3
C = 1                 # Old process coefficients used in the initial project
kp =0.125 
SP = SP
kcst = np.arange(0,60,dt)

# Relatiopnship btwn kc and Ti obtained through the direct substitution method
tist =kp*kcst*A**2/(((A*B) - C - (kp*kcst))*(C + (kp*kcst)))


kczn ,tizn,tdzn = ZN(Gp_n,Gp_d,t,SP,Contr_type,dt,DT) # Ziegler-Nichols settings via function ZN
kcch ,tich,tdch = Cohen_Coon(Gp_n,Gp_d,t,SP,Contr_type,dt,DT)  

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
        Gc_n = [kc*ti*td,(kc*ti),kc]
        Gc_d = [ti,0] 
        
    # The process and controller transfer functions are multiplied to make the open loop TF                                    
    OL_TF_n = np.polymul(Gp_n,Gc_n)
    OL_TF_d = np.polymul(Gc_d,Gp_d)
    CL_TF_n = OL_TF_n
    CL_TF_d = np.polyadd(OL_TF_d,OL_TF_n)
    (A,B,C,D) =signal.tf2ss(OL_TF_n,OL_TF_d)      # Open Loop Transfer Function is converted to State Space
    (A_CL,B_CL,C_CL,D_CL) =signal.tf2ss(CL_TF_n,CL_TF_d) # Closed Loop Transfer Function is converted to State Space


    rootsA = np.array(linalg.eigvals(A_CL))
    
#    step_response = signal.lsim((A,B,C,D),u,t,X0=None,interp=1)[1]
#    step_responseDDE = DDE(A,B,C,D,t,SP_info,DT)
    step_responseEuler = Euler(A,B,C,D,t,u,DT)
    
    if (rootsA.real < 0).all():
        for i in range(0,entries):          # Stabilty of the Closed Loop is checked 
            Y = step_responseEuler
            y[i,k] = Y[i]
            
    else:
        y[:,k] = np.NaN    
    
    k_c[k] = kc
    t_i[k] = ti
    
kc = k_c
ti = t_i
y = y.T

fig = plotgraphs(kc,ti,y,num,entries,t,tfinal,dt,SP,kcst,tist)