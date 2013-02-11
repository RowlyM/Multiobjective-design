# -*- coding: utf-8 -*-
"""
Created on Sat Feb 09 10:34:56 2013

@author: Rowly
"""
import numpy as np
from scipy import linalg
from scipy import signal
from plotgraphs import *
from MODminifunc import*
import matplotlib.pyplot as plt

def ZN(OL_Gp_n,OL_Gp_d,t,SP,Contr,dt,Td):
        
        u = Step2(t,SP,dt,Td)
        (A,B,C,D) =signal.tf2ss(OL_Gp_n,OL_Gp_d)      # Transfer Function is converted to State Space
        y = signal.lsim((A,B,C,D),u,t,X0=None,interp=1)[1]
        kp = max(y)
        for i in np.arange(0,len(t)):
        
            if y[i]>0:
                t1 = t[i]
                break
    
        for i in np.arange(0,len(t)):   
            if y[i] > 0.6321*max(y):
                t2 = t[i]
                break

        tau =((t2 - t1))
        Td =(t2 - tau)
        CP = np.zeros(3)
        
        
        if Contr == 'P':
            print 'P Controller'
            CP[0]= tau/(Td*kp)
   
        elif Contr == 'PI':
            print 'PI Controller'
            CP[0]= tau*0.9/(Td*kp)
            CP[1] = 3*Td
            
        
        elif Contr == 'PID':
            print 'PID Controller'
            CP[0] = 1.2*(tau/(Td*kp))
            CP[1] = 2*Td
            CP[2] = .5*Td
#        plt.plot(t,y)
#        plt.show()
        print CP    
        return CP
    
def Cohen_Coon(OL_Gp_n,OL_Gp_d,t,SP,Contr,dt,Td):
        u = Step2(t,SP,dt,Td)
        (A,B,C,D) =signal.tf2ss(OL_Gp_n,OL_Gp_d)      # Transfer Function is converted to State Space
        y = signal.lsim((A,B,C,D),u,t,X0=None,interp=1)[1]
        kp = max(y)
        for i in np.arange(0,len(t)):
        
            if y[i]>0:
                t1 = t[i]
                break
    
        for i in np.arange(0,len(t)):   
            if y[i] > 0.6321*max(y):
                t2 = t[i]
                break

        tau =((t2 - t1))
        Td =(t2 - tau)
        a = (kp*Td)/tau
        b = Td/(Td+tau)
        CP = np.zeros(3)
        
        if Contr == 'P':
            print 'P Controller'
            CP[0]= (1/a)*(1+(0.35*b)/(1-b))
   
        elif Contr == 'PI':
            print 'PI Controller'
            CP[0]= (.9/a)*(1+(0.92*b)/(1-b))
            CP[1] = (3.3-3*b)/(1+1.2*b)*Td
            
        
        elif Contr == 'PID':
            print 'PID Controller'
            CP[0] = (1.35/a)*(1+(0.18*b)/(1-b))
            CP[1] = (2.5-2*b)/(1-0.39*b)*Td
            CP[2] = (.37-.37*b)/(1-0.81*b)*Td
            
        elif Contr == 'PD':
            print 'PID Controller'
            CP[0] = (1.24/a)*(1+(0.13*b)/(1-b))
            CP[2] = (.27-.36*b)/(1-0.87*b)*Td
        print CP
        return CP