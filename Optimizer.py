# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:25:13 2013

@author: Rowly
"""
# import matplotlib.pyplot as plt
import Simulator as sim
import Mopsocd_setup_window as mop
from pymopsocd import *
import matplotlib.pyplot as plt 

def Optimize(tfinal, dt, Gp_n, Gp_d, SP, DT, u):
    Nparticles, archivesize, maxgen, pMut, rememberevals, printinterval, kc_range, ti_range, td_range = mop.cc(
    )
    'Nparticles, archivesize, maxgen, kc_range, ti_range, td_range ,Xobjective, Yobjective'

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
            obj = sim.response_gen(
                tfinal, dt, Gp_n, Gp_d, SP, DT, u, *position)
            return cevaluation(position, array([obj[0], obj[1], obj[2], obj[3], obj[4]]))
    prob = problemcontrol(kc_range, ti_range, td_range)
    theswarm = swarm(prob, Nparticles=Nparticles,
                     archivesize=archivesize,
                     maxgen=maxgen,
                     pMut=pMut,
                     rememberevals=rememberevals,
                     printinterval=printinterval)

    theswarm.run()

    # plt.figure()
    # font = {'family' : 'cambria',
    #        'weight' : 'normal',
    #        'size'   : 14}
    #
    # plt.matplotlib.rc('font', **font)
    # plt.figure().set_facecolor('white')
#    plt.figure()
#    plt.plot(*zip(*[e.value for e in theswarm.allevals]), color='white', marker='o', linestyle='')
#    plt.show()
    return (zip(*sorted([list(e.value) for e in theswarm.archive.list if not isnan(e.value).all()])))
