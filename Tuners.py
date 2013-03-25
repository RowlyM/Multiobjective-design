# -*- coding: utf-8 -*-
"""
Created on Sat Feb 09 10:34:56 2013

@author: Rowly Mudzhiba
"""
import numpy as np
from scipy import signal
from EulerODE import closedloop_sim,Euler

def first_order_estimate(Gp_n,Gp_d,t,u,Contr_type,DT):
    (A,B,C,D) =signal.tf2ss(Gp_n,Gp_d)      # Transfer Function is converted to State Space
    y = Euler(A,B,C,D,t,u,DT)
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
    return tau, Td, kp


def ZN(Gp_n,Gp_d,t,u,Contr_type,DT):
        Contr = Contr_type
        tau, Td, kp = first_order_estimate(Gp_n,Gp_d,t,u,Contr_type,DT)
        CP = np.zeros(3)
#        print tau,Td,kp
        
        if Contr == 'P':
#            print 'P Controller'
            CP[0]= tau/(Td*kp)
   
        elif Contr == 'PI':
#            print 'PI Controller'
            CP[0]= tau*0.9/(Td*kp)
            CP[1] = 3*Td
            
        
        elif Contr == 'PID':
#            print 'PID Controller'
            CP[0] = 1.2*(tau/(Td*kp))
            CP[1] = 2*Td
            CP[2] = .5*Td
            
#        print 'Ziegler-Nicholas parameters'     
#        print CP    
        return CP

def Cohen_Coon(Gp_n,Gp_d,t,u,Contr_type,DT):
        Contr = Contr_type
        tau, Td, kp = first_order_estimate(Gp_n,Gp_d,t,u,Contr_type,DT)
        a = (kp*Td)/tau
        b = Td/(Td+tau)
        CP = np.zeros(3)
        
        if Contr == 'P':
#            print 'P Controller'
            CP[0]= (1/a)*(1+(0.35*b)/(1-b))
   
        elif Contr == 'PI':
#            print 'PI Controller'
            CP[0]= (.9/a)*(1+(0.92*b)/(1-b))
            CP[1] = (3.3-3*b)/(1+1.2*b)*Td
            
        
        elif Contr == 'PID':
#            print 'PID Controller'
            CP[0] = (1.35/a)*(1+(0.18*b)/(1-b))
            CP[1] = (2.5-2*b)/(1-0.39*b)*Td
            CP[2] = (.37-.37*b)/(1-0.81*b)*Td
            
#        print ' Cohen- Coon Parameters'
#        print CP
        return CP

