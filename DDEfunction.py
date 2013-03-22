# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 14:12:13 2013

@author: Rowly Mudzhiba
        
"""

from numpy import*
import PyDDE.pydde as p
from MODminifunc import mirror

def DDE(A,B,C,D,t,SP_info,DT):
    SP_input = SP_info[0]
    step_time = SP_info[1]
    ramp_time = SP_info[2]
    SP = SP_info[3]

    
    # ddegrad code below will be explained properly on the log-book
    def ddegrad(s,c,t):
        # Ysp is generated at time increment
        if SP_input == 'step':
            if t < step_time:
                Ysp = 0
            else:
                Ysp = SP
        elif SP_input == 'ramp':
            if t < ramp_time:
                Ysp = (SP/ramp_time)*t
            else:
                Ysp = SP     
                
        NODEs = len(c)-1
        print NODEs 
        grad = zeros(NODEs)
        for g in range(0,NODEs):
            if DT == 0:
                if g == 0:
                    grad[g] = (SP-s[0])*c[-1]+ dot(c[0:NODEs],s[0:NODEs])
                else:
                    grad[g] = s[g]
            else:
                if g == 0:
                    if t <= DT:
                        grad[g] = 0
                    else:
                        alag = zeros(NODEs)
                        if t > DT:
                            for l in range(0,NODEs):
                                alag[l] = p.pastvalue(l,t-(DT),0)
                        grad[g] =(SP-alag[0])*c[-1]+ dot(c[0:NODEs],s[0:NODEs])
                else:
                    grad[g] = s[g]    
                    
        return array(grad)
    
    def ddesthist(g, s, c, t): # Stores past state variables and its used by the PyDDE solver
        return (s, g)
   
    
    # Setting up constants that are used in the "ode_eg.initproblem"
    cons = zeros((2,len(A)))
    A = mirror(A[0])
    for i in range(0,2):
        for j in range(0,len(A)):
            if i == 0:
                cons[i,j] = A[j]
            else:
                cons[i,j] = C[0,j]
           
    odecons = cons.ravel()
#    print odecons
    ini_values = zeros(len(A)*2)
    odeist = ini_values
    if len(A)==1:
        n = 1
    else:
        n = len(A)*2-1
    
    # PyDDE Solvers
    ode_eg = p.dde()
    ode_eg.initproblem(no_vars=n, no_cons=len(odecons), nlag=1, nsw=0,
                           t0=0.0, t1=t[-1],
                           initstate=odeist, c=odecons, otimes=t,
                           grad=ddegrad,storehistory=ddesthist)
        
    odestsc = array([0])   
    ode_eg.initsolver(tol=1*10**(-5), hbsize=1000,
                          dt=t[1], 
                          statescale=odestsc)
        
    ode_eg.solve()
    
    
    yDDE =ode_eg.data[:,1]
    return yDDE
