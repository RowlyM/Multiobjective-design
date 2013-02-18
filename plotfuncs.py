# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 00:23:28 2013
@author: Nokukhanya Khwela
         Modified by Rowly Mudzhiba
"""

import numpy as np

def overshoot(x,num,SP,entries,t):
        tpr = np.zeros(num)
        por = np.zeros(num)
        for u in range(0,num):
            if (x[:][u]== None):
                por[u]= None
                tpr[u] = None
            else:
                por[u] = ((np.max(x[:][u]))- SP)/SP
                for g in range(0,entries):
                    if x[u][g] ==np.max(x[:,u]):
                        tpr[u] = t[g]
                       
                    if por[u] < 0:
                        por[u] = np.NINF
                        tpr[u] = np.NINF
                        
        return {'por':por ,'tpr':tpr}
        
def risetime(x,num,entries,SP,t): 
        tr = np.zeros(num)
        for j in range(0,num):
            if (np.isnan(x[j][:])).all()== True:
                tr[j] = None 
            else:
                for k in range(0, entries-1):    
                    if np.sign(SP - x[j][k])!= np.sign(SP - x[j][k+1]): # added a equals sign
                        if np.sign(SP - x[j][k])==0:                 
                            tr[j] = t[k]
                        else :
                            tr[j] = np.interp(SP,[x[j][k],x[j][k+1]],[t[k],t[k+1]])
                        break
        return tr