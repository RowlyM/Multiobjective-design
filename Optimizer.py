# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:25:13 2013

@author: Rowly
"""
import numpy as np
import Simulator as sim
import MODminifunc as func
import Mopsocd_setup_window as mop
from pymopsocd import *
def Optimize(tfinal, dt, Gp_n, Gp_d, SP, DT,u):    
    Nparticles, archivesize, maxgen, kc_range, ti_range, td_range ,Xobjective, Yobjective = mop.cc()
    'Nparticles, archivesize, maxgen, kc_range, ti_range, td_range ,Xobjective, Yobjective' 
    
    class problemcontrol(problem):
        def __init__(self, kc_range, ti_range, td_range):
            self.xrange = [kc_range[0], ti_range[0],td_range[0]]
            self.bigvalues = array([1.7 , 90])
            self.size = len(self.xrange)
            self.obnames = ['Rise time', 'Overshoot']
            
    
        def feasible(self, position):
            A = sim.State_Space_mats(Gp_n, Gp_d, *position)[0]
            return sim.stable(A[0])
    
        def evaluate(self, position):
            obj = sim.response_gen(tfinal, dt, Gp_n, Gp_d, SP, DT,u,*position)
            return cevaluation(position, array([obj[0], obj[1]]))
    
    
    prob = problemcontrol(kc_range, ti_range, td_range)
    theswarm = swarm(prob, Nparticles=Nparticles[0], 
                         archivesize=archivesize[0], 
                         maxgen=maxgen[0],
                         pMut=0.01,
                         rememberevals=True,
                         printinterval=1)
    
    theswarm.run()
    
    #plt.figure()
    #font = {'family' : 'cambria', 
    #        'weight' : 'normal', 
    #        'size'   : 14} 
    # 
    #plt.matplotlib.rc('font', **font)
    #plt.figure().set_facecolor('white')
    ##plt.plot(*zip(*[e.value for e in theswarm.allevals]), color='white', marker='o', linestyle='')
    
#    objplot = plt.plot(*zip(*sorted([list(e.value) for e in theswarm.archive.list if not isnan(e.value).all()])), color='red',linewidth = 2.5)
#    return objplot             