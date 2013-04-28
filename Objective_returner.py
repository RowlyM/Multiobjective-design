# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:02:33 2013

@author: Rowly

This is similar to Ojectives.py 
"""

import numpy as np
import scipy as sp

def Ojectives(t,x,num,entries,SP):
    def overshoot(t,x,num,entries,SP):
        # List changes
        for u in range(0,num):
            if np.isnan(x).any()==True: # Checks if theres any 'None' on the responce vector
                por= np.NaN
                tpr = np.NaN
            else:
                if (((np.max(x[u][:]))- SP)/SP)< .6:
                    
                    por = ((np.max(x[u][:]))- SP)/SP # Calculates overshoot ratio = (max-SP)/SP
                else:
                    por= np.NaN
                for g in range(0,entries):
                    if x[u][g] == np.max(x[u][:]):
                        tpr = t[g]               # Finds the time where the maximum is
                       
                    if por < 0:
                        por= np.NaN            
                        tpr = np.NaN
                        
                    if por == None:
                        tpr =np.NaN
                    
                        
        return por,tpr
    por, tpr = overshoot(t,x,num,entries,SP)    
        
    def risetime(t,x,num,entries,SP): 
        
        if np.isnan(x).any():
            tr = np.NaN 
        elif np.isnan(por):
            tr = np.NaN
        
        else:
            for k in range(0, entries-1):    
                if np.sign(SP - x[0][k])!=np.sign(SP - x[0][k+1]):
                    if por ==0:
                        tr1 =np.interp(0.1*SP,[x[0][k],x[0][k+1]],[t[k],t[k+1]])
                        tr2 = np.interp(0.9*SP,[x[0][k],x[0][k+1]],[t[k],t[0][k+1]])
                        tr = tr2-tr1
                        break
                    elif por!=0 and np.isnan(por)==False:
                        if np.sign(SP - x[0][k+1])==0:                 
                            tr = t[k+1]
                        else :
                            tr = np.interp(SP,[x[0][k],x[0][k+1]],[t[k],t[k+1]])
                            break
        return tr
    tr = risetime(t,x,num,entries,SP)        
            
    def ISE(t,x,num,entries,SP):
        for i in range(0,num):
            if np.isnan(x).any()==True:
                ise = np.NaN
            else:    
                error = np.subtract(SP,x[i][:])
                ise = sp.integrate.simps((error**2),t)
        return ise
    ise = ISE(t,x,num,entries,SP)    
       
    def IAE(t,x,num,entries,SP):
        iae = np.zeros(num)
        for i in range(0,num):
            if np.isnan(x).any()==True:
                iae = np.NaN
            else:
                error = abs(np.subtract(SP,x[i][:]))
                iae = sp.integrate.simps(error,t)
        return iae
    iae = IAE(t,x,num,entries,SP)    
        
    def ITAE(t,x,num,entries,SP):
        for i in range(0,num):
            if np.isnan(x).any()==True:
                itae= np.NaN
            else:
                error = np.multiply(t,abs(np.subtract(SP,x[i][:])))
                itae = sp.integrate.simps(error,t)
        return itae
    itae = ITAE(t,x,num,entries,SP)
    return por, tr, ise, iae, itae