# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 13:19:10 2013

@author: Rowly Mudzhiba

This a modification of simulate.py by Nokukhanya Khwela

"""
import numpy as np
from scipy import signal
from scipy import linalg
from EulerODE import Euler
import Objective_returner
import MODminifunc as func

def State_Space_mats(Gp_n, Gp_d, kc, ti, td):

    if ti == 0:
        Gc_d = 1
        Gc_n = [kc*ti*td,(kc*ti),kc] 
        
    else:    
        Gc_n = [kc*ti*td,(kc*ti),kc]
        Gc_d = [ti,0]
        
    OL_TF_n = np.polymul(Gp_n,Gc_n)
    OL_TF_d = np.polymul(Gc_d,Gp_d)
    CL_TF_n = OL_TF_n
    CL_TF_d = np.polyadd(OL_TF_d,OL_TF_n)
    OL_mats =signal.tf2ss(OL_TF_n,OL_TF_d)      # Open Loop Transfer Function is converted to State Space
    CL_mats =signal.tf2ss(CL_TF_n,CL_TF_d) # Closed Loop Transfer Function is converted to State Space
    
    return OL_mats, CL_mats
    
def stable(A_CL):
    rootsA = np.array(linalg.eigvals(A_CL))
    return (rootsA.real < 0).all()
    
    
def response_gen(tfinal, dt, Gp_n, Gp_d, SP, DT,SP_input,step_time,ramp_time, kc, ti,td):
    t = np.arange(0, tfinal, dt)
    num = 1
    entries = len(t)
    if SP_input == 'Step':
        u = func.Step(t, step_time, SP)
    else:
        u = func.Ramp(t, ramp_time, SP)
        
    y = np.zeros((num,entries))
    OL_mats = State_Space_mats(Gp_n, Gp_d, kc, ti, td)[0]
    CL_mats = State_Space_mats(Gp_n, Gp_d, kc, ti, td)[1]
    step_responseEuler = Euler(OL_mats[0], OL_mats[1], OL_mats[2], OL_mats[3],t,u,DT)
    
    rootsA = np.array(linalg.eigvals(CL_mats[0]))
    
    if (rootsA.real < 0).all():
        y[0][:] = step_responseEuler[:]
        
    else:
        y  = np.NaN    
    objectives =  Objective_returner.Ojectives(t,y,num,entries,SP)
    return objectives

    