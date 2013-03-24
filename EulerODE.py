# -*- coding: utf-8 -*-
"""

@author: Rowly Mudzhiba

Euler fuction was developed to replace the DDEfunction. DDEfunction results are not satisfactory.
"""
import numpy as np
from scipy import interp
from MODminifunc import mirror

def Euler(A,B,C,D,t,u,DT):
    A = mirror(A[0])            # reverse the order of the vector eg [1,3] to [3,1]
    C = mirror(C[0])
    
    NODEs = len(A[0:])          #number of ODEs
    def dydt(SV,SVm,SP): 
        NODEs = len(A[0:])    
        ODEs = np.zeros(NODEs) 
        for s in range(0,NODEs):
            if s<(NODEs-1):
                ODEs[s] = SV[s+1]
                
            elif s == (NODEs-1):
                ODEs[s] = (SP-SVm)+np.dot(SV,A)
        return (ODEs)
        
    SS = np.zeros(NODEs)        # Initial states values
    SVm = 0.                    # Measured value
    dt = t[1] 
    y = np.zeros(len(t))
    SV_save = np.zeros(len(t)) 
    
    for i in range(0,len(t)):
        SS = SS + dt*np.array((dydt(SS,SVm,u[i])))
        y[i] = np.dot(C,SS)
        SV_save[i] = y[i]
        
        if DT == 0:
           SVm = y[i]
            
        else:
            if t[i]<= DT:
                y[i] =0
            elif (t[i]>DT):
                y[i]= interp(t[i]-DT,t,SV_save)
                SVm = y[i]

    return y
    
def closedloop_sim(A, B, C, D, tspan, r, DT):
    """ Simulate the closed loop resopnse of a system with loop transfer function (L)
    described by the State Space matrices A, B, C and D and an output delay DT
    
    r  +  e  +-------+  y  +----+
    --->o--->|   L   |-----| DT |-----+---> y_D 
       -^    +-------+     +----+     |
        |                             |
        +-----------------------------+
        
    """
    
    x = np.zeros(A.shape[0])
    ys = np.zeros_like(tspan)
    
    # Assume fixed step size, and start at zero, so 
    dt = tspan[1]
    
    for i, t in enumerate(tspan):
        # Dead time using interpolation
        y_D = interp(t - DT, tspan, ys)

        # error calculation: wrapped in an array to produce correct product result
        e = np.array([r[i] - y_D])
        
        # State space form
        dxdt = A.dot(x) + B.dot(e)
        y = C.dot(x) + D.dot(e)

        # Store result
        ys[i] = y_D
        
        # Euler integration
        x = x + dxdt*dt
    
    return ys
