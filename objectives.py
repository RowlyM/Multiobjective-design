# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 00:23:28 2013
@author: Nokukhanya Khwela
         Modified by Rowly Mudzhiba
"""

import numpy as np
import scipy as sp

def overshoot(t,x,num,entries,SP):
        # List changes
        tpr = np.zeros(num)
        por = np.zeros(num)
        for u in range(0,num):
            if (x[u,:]== None): # Checks if theres any 'None' on the responce vector
                por[u]= None
                tpr[u] = None
            else:
                por[u] = ((np.max(x[u,:]))- SP)/SP # Calculates overshoot ratio = (max-SP)/SP
                for g in range(0,entries):
                    if x[u,g] == np.max(x[u,:]):
                        tpr[u] = t[g]               # Finds the time where the maximum is
                       
                    if por[u] < 0:
                        por[u] = np.NINF            
                        tpr[u] = np.NINF
                        
        return {'por':por ,'tpr':tpr}
        
def risetime(t,x,num,entries,SP): 
        tr = np.zeros(num)
        for j in range(0,num):
            if (np.isnan(x[j,:])).all() == True:
                tr[j] = None 
            else:
                for k in range(0, entries-1):    
                    if np.sign(SP - x[j,k])!= np.sign(SP - x[j,k+1]):
                        if np.sign(SP - x[j,k])==0:                 
                            tr[j] = t[k]
                        else :
                            tr[j] = np.interp(SP,[x[j][k],x[j][k+1]],[t[k],t[k+1]])
                        break
        return tr
        
def ISE(t,x,num,entries,SP):
    ise = np.zeros(num)
    for i in range(0,num):
        if x[i,:] == None:
            ise[i] = None
        else:    
            error = np.subtract(SP,x[i,:])
            ise[i] = sp.integrate.simps((error**2),t)
    return ise
   
def IAE(t,x,num,entries,SP):
    iae = np.zeros(num)
    for i in range(0,num):
        if x[i,:] == None:
            iae[i] = None
        else:
            error = abs(np.subtract(SP,x[i,:]))
            ise[i] = sp.integrate.simps(error,t)
    return ise
    
def ITAE(t,x,num,entries,SP):
    itae = np.zeros(num)
    for i in range(0,num):
        if x[i,:] == None:
            itae[i] = None
        else:
            error = np.multiply(t,abs(np.subtract(SP,x[i,:])))
            itae[i] = sp.integrate.simps(error,t)
    return ise