# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:23:21 2013

@author: Rowly
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import *
from scipy import integrate
from scipy import signal

#
Gp_n = [1]       
Gp_d = [1,1]
Gc_n = [1]
Gc_d = [1]
t = np.arange(0,10,0.0001)
SP = np.ones(len(t))
OL_TF_n = np.polymul(Gp_n, Gc_n)
OL_TF_d = np.polymul(Gc_d,Gp_d)
(A,B,C,D) =signal.tf2ss(OL_TF_n, OL_TF_d)

step_response = signal.lsim((A,B,C,D),SP,t,X0=None,interp=1)[1]

def ISE(SP,y,t):
    error = np.subtract(SP,y)
    ISE = sum((error**2)*t[1])
    return ISE
   
def IAE(SP,y,t):
    error = abs(np.subtract(SP,y))
    IAE = sum(error*t[1])
    return IAE
    
def ITAE(SP,y,t):
    error = np.multiply(t,abs(np.subtract(SP,y)))
    ITAE = sum(error*t[1])
    return ITAE
print 'ISE results'    
print (integrate.quad(lambda (t):(1-(1-e**-t))**2,0,100)[0])
print ISE(SP,step_response,t)

print 'IAE results'
print (integrate.quad(lambda (t):abs((1-(1-e**-t))),0,100)[0])
print IAE(SP,step_response,t)

print 'ITAE results'
print (integrate.quad(lambda (t):t*abs((1-(1-e**-t))),0,100)[0])
print ITAE(SP,step_response,t)

plt.plot(t,step_response)
plt.show()