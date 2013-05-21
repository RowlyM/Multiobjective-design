# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 15:06:05 2013

@author: Rowly
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg
from scipy import signal
from plotgraphs import *
import MODminifunc as func
from Tuners import*
from EulerODE import Euler

def Gen(num_of_gens, Gp_n, Gp_d, SP, tfinal, dt, DT):

    def plotter(kc,ti,td,x,num,entries,t,tfinal,dt,SP,kcst,tist):
        
        global kc_unstable, ti_unstable, td_unstable
        global kc_offset, ti_offset, td_offset
        global kc_goodpoints, ti_goodpoints, td_goodpoints
        global kc_idx, ti_idx, td_idx, xt
        
        por,tpr = obj.overshoot(t,x,num,entries,SP)
        
    #   calculates the risetime
       
        tr= obj.risetime(t,x,num,entries,SP)
        SSoffset = np.isneginf(por)
        UNSTABLE = np.isnan(por)  
        ISE = obj.ISE(t,x,num,entries,SP)
        IAE = obj.IAE(t,x,num,entries,SP)
        ITAE = obj.ITAE(t,x,num,entries,SP)
        goodpoints = ~(np.isnan(tr)| np.isnan(por)|np.isneginf(por))
        idx = np.arange(0,num)
        tr = tr[goodpoints]
        por = por[goodpoints]
        tpr = tpr[goodpoints]
        ISE = ISE[goodpoints]
        idx = idx[goodpoints]
        x = x[goodpoints]
        xt = x
        p = pareto.domset([itemgetter(1), itemgetter(2)], zip(idx, por, tr, ISE, IAE, ITAE))
       
        front = p.data
        idx, ppor, ptr, pise, piae, pitae = map(np.array, zip(*front))
        sortidx = np.argsort(ppor)
        ppor = ppor[sortidx]
        ptr = ptr[sortidx]
        pise = pise[sortidx]
        piae = piae[sortidx]
        pitae = pitae[sortidx]
        
        kc_unstable, ti_unstable, td_unstable = kc[UNSTABLE], ti[UNSTABLE], td[UNSTABLE]
        kc_offset, ti_offset, td_offset = kc[SSoffset], ti[SSoffset], td[SSoffset]
        kc_goodpoints, ti_goodpoints, td_goodpoints = kc[goodpoints], ti[goodpoints], td[goodpoints]
        kc_idx, ti_idx, td_idx = kc[idx], ti[idx], td[idx]

       
    t = np.arange(0, tfinal, dt)
    entries = len(t)
    num = 20           # number of tuning constant sets
    y = np.zeros((entries, num))
    
    # Controller choice
    Contr_type = 'PI'               # Choose controller by typing 'P' , 'PI' or 'PID'
    if Contr_type == 'P':
        Controller = 1
    elif Contr_type == 'PI':
        Controller = 2
    elif Contr_type == 'PID':
        Controller = 3
    
    [k_c, t_i, t_d] = func.RPG(num, Controller)     # Random Parameter Generator
                                        # Options: 1= P, 2 = PI, 3 = PID
    
    # Different Ysp inputs
    SP_input = 'step'           # Choose Set point input by typing 'step' or 'ramp'
    step_time = 0
    ramp_time = 5.
    # u = func.Ramp(t,ramp_time,SP)
    u = func.Step(t, step_time, SP)
    SP_info = [SP_input, step_time, ramp_time, SP]
    
    # coefficients of the transfer function Gp = kp/(s^3 + As^2 + Bs +C)
    A = 3
    B = 3
    C = 1                 # Old process coefficients used in the initial project
    kp = 0.125
    SP = SP
    kcst = np.arange(0, 60, dt)
    
    # Relatiopnship btwn kc and Ti obtained through the direct substitution method
    tist = kp * kcst * A ** 2 / (((A * B) - C - (kp * kcst)) * (C + (kp * kcst)))
    
    
    kczn, tizn, tdzn = ZN(Gp_n, Gp_d, t, u, Contr_type, DT)
                           # Ziegler-Nichols settings via function ZN
    kcch, tich, tdch = Cohen_Coon(Gp_n, Gp_d, t, u, Contr_type, DT)
    
    ## System responce
    for k in range(0, num):
        if k == num - 1:
            kc = kczn           # Inserting Ziegler-Nicholas parameters
            ti = tizn
            td = tdzn
    
        elif k == num - 2:        # Inserting Cohen-Coon parameters
            kc = kcch
            ti = tich
            td = tdch
        else:
            kc = k_c[k]
            ti = t_i[k]
            td = t_d[k]
    
        if ti == 0:
            Gc_d = 1
            Gc_n = [kc * ti * td, (kc * ti), kc]
    
        else:
            Gc_n = [kc * ti * td, (kc * ti), kc]
            Gc_d = [ti, 0]
    
        # The process and controller transfer functions are multiplied to make the
        # open loop TF
        OL_TF_n = np.polymul(Gp_n, Gc_n)
        OL_TF_d = np.polymul(Gc_d, Gp_d)
        CL_TF_n = OL_TF_n
        CL_TF_d = np.polyadd(OL_TF_d, OL_TF_n)
        (A, B, C, D) = signal.tf2ss(OL_TF_n, OL_TF_d)
         # Open Loop Transfer Function is converted to State Space
        (A_CL, B_CL, C_CL, D_CL) = signal.tf2ss(CL_TF_n, CL_TF_d)
         # Closed Loop Transfer Function is converted to State Space
    
        rootsA = np.array(linalg.eigvals(A_CL))
    
    #    step_response = signal.lsim((A,B,C,D),u,t,X0=None,interp=1)[1]
    #    step_responseDDE = DDE(A,B,C,D,t,SP_info,DT)
        step_responseEuler = Euler(A, B, C, D, t, u, DT)
    
        if (rootsA.real < 0).all():
            for i in range(0, entries):          # Stabilty of the Closed Loop is checked
                Y = step_responseEuler
                y[i, k] = Y[i]
    
        else:
            y[:, k] = np.NaN
    
        k_c[k] = kc
        t_i[k] = ti
    
    kc = k_c
    ti = t_i
    td = t_d
    y = y.T
    
    plotter(kc, ti, td, y, num, entries, t, tfinal, dt, SP, kcst, tist)
#    fig = plt.figure(4)
#
#    plt.plot(t,xt[4][:])
#    plt.show()

    return kc_unstable, ti_unstable, td_unstable, kc_offset, ti_offset, td_offset,kc_goodpoints, ti_goodpoints, td_goodpoints, kc_idx, ti_idx, td_idx 
