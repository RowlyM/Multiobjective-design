# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:25:13 2013

@author: Rowly Mudzhiba
"""

import Simulator as sim
import Mopsocd_setup_window as mop
from pymopsocd import *

def Optimize(tfinal, dt, Gp_n, Gp_d, SP, DT,SP_input,step_time,ramp_time):
    ''' The Optimize runs the the MOPSO-cd window and runs the MOPSO-cd.'''
    
    Nparticles, archivesize, maxgen, pMut, rememberevals, printinterval, kc_range, ti_range, td_range = mop.cc()

    class problemcontrol(problem):
        def __init__(self, kc_range, ti_range, td_range):
            self.xrange = [kc_range[0], ti_range[0], td_range[0]]
            self.bigvalues = array([1.7, 90])
            self.size = len(self.xrange)
            self.obnames = ['Rise time', 'Overshoot']

        def feasible(self, position):
            A = sim.State_Space_mats(Gp_n, Gp_d, *position)[0]
            return sim.stable(A[0])

        def evaluate(self, position):
            obj = sim.response_gen(tfinal, dt, Gp_n, Gp_d, SP,
                                   DT,SP_input,step_time,ramp_time, *position)
            return cevaluation(position, array([obj[0], obj[1], obj[2], obj[3], obj[4]]))
    prob = problemcontrol(kc_range, ti_range, td_range)
    
    theswarm = swarm(prob, Nparticles=Nparticles,
                     archivesize=archivesize,
                     maxgen=maxgen,
                     pMut=pMut,
                     rememberevals=rememberevals,
                     printinterval=printinterval)

    theswarm.run()

    return (zip(*sorted([list(e.value) for e in theswarm.archive.list if not isnan(e.value).all()])))
