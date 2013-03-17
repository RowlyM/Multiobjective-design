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
    
    
    
    
    