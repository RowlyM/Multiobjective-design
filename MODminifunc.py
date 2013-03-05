# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 15:24:18 2013

@author: Rowly Mudzhiba
"""

import numpy as np
from scipy import linalg

def mirror(a):
        b  = len(a)
        t = 0
        c = np.ones(b)
        for i in range(b-1,-1,-1):
            c[t] = a[i]
            t += 1
        return c

def Ramp(t,dt,rt,max_ramp):
    Ysp = np.zeros(len(t))
    rt_inc =rt/dt
    grad =max_ramp/rt_inc
    for i in np.arange(0,len(t)):
        if i <=rt_inc:
            Ysp[i] = grad*t[i]    
        else:
            Ysp[i] = max_ramp
        
    return Ysp       
        
def Step(t,step_max):
    Ysp = np.zeros(len(t)) 
    Ysp[1:] = step_max
    return Ysp
    
def Step2(t,step_max,dt,d):  # This function is used in the Tuning function
        Ysp = np.zeros(len(t))
        inc = d/dt
        Ysp[inc:] = step_max
        return Ysp
    
def RPG(num,n):
        k_c = np.zeros(num)
        t_i = np.zeros(num)
        t_d = np.zeros(num)
        if n == 3:
            aa = np.random.rand(num,n)  # Used for random search for control parameters
            a = 0
            while a <= (num/2):             # First while loop is used to increase the probability of getting 
                k_c[a] = (2)*aa[a, 0]       # small parameter range (0-2)
                t_i[a] = (2)*aa[a, 1]
                t_d[a] = (1)*aa[a, 2]
                a +=1
    
            while a <= num-1:
                k_c[a] = (60-2)*aa[a, 0]+2 
                t_i[a ] = (30-2)*aa[a, 1]
                t_d[a] = (5)*aa[a, 2]
                a +=1
        
            return k_c,t_i,t_d
        elif n == 2:
            aa = np.random.rand(num,n)
            a = 0 
            while a <= (num/2):
                k_c[a] = (2)*aa[a, 0] 
                t_i[a] = (2)*aa[a, 1]
                a +=1
            
            while a <= num-1:
                k_c[a] = (60-2)*aa[a, 0]+2 
                t_i[a ] = (30-2)*aa[a, 1]    
                a +=1
        else:
             aa = np.random.rand(num,n)
             a = 0 
             while a <= (num/2):
                k_c[a] = (2)*aa[a]
                a +=1
            
             while a <= num-1:
                k_c[a] = (60-2)*aa[a]  
                a +=1
           
        return k_c,t_i,t_d




    