#!/usr/bin/env python

from math import *
from numpy import *


def flip(pf):
    return random.rand() < pf


def choice(seq):
    return seq[random.randint(len(seq))]


def sortrank(arr):
    i = argsort(arr)
    return [i, arr[i]]


def dhelp(arr, i):
    N = len(arr)
    if i == 0:
        return arr[1] - arr[0]
    elif i == N-1:
        return arr[N-1] - arr[N-2]
    else:
        return min(arr[i]-arr[i-1],arr[i+1]-arr[i])


def mindist(arr):
    d = array([dhelp(arr, i) for i in range(len(arr))])
    maxval = max(d)
    d[0] += maxval
    d[-1] += maxval
    return d


class particle:
    def __init__(self, prob):
        self.problem = prob
        self.position = self.problem.initpos()
        self.velocity = zeros(self.problem.size)
        self.feasible = True
        self.best = self.problem.evaluate(self.position);

    def evaluate(self):
        if self.feasible:
            self.value = self.problem.evaluate(self.position)
            if self.value.dominates(self.best) or \
                    not self.best.dominates(self.value) and flip(0.5):
                self.best = self.value
        else:
            self.value = cevaluation(self.position, self.problem.bigvalues)

    def updatevelocity(self, gbest):
        N = self.problem.size
        self.velocity = 1.0*(0.4*self.velocity + \
            1.0*random.rand(N)*(self.best.position - self.position) + \
            1.0*random.rand(N)*(gbest.position - self.position))

    def updateposition(self):
        self.position += self.velocity

    def maintain(self):
        self.feasible = self.problem.feasible(self.position)

    def dominates(self, otherparticle):
        return self.value.dominates(otherparticle.value)
    
    def mutate(self, f):
        minvalue, maxvalue = self.problem.get_ranges()
        dimension = random.randint(0,self.problem.size-1)
        r = f*(maxvalue[dimension] - minvalue[dimension])
        minv = max(self.position[dimension]-r, minvalue[dimension])
        maxv = min(self.position[dimension]+r, maxvalue[dimension])
        self.position[dimension] = random.uniform(minv,maxv)
    
    def __repr__(self):
        s = "Particle at " + str(self.position) + " Value: " + str(self.value)
        if self.feasible:
            s += " (feasible)"
        else:
            s += " (infeasible)"
        return s


class swarm:
    def __init__(self, prob, Nparticles, archivesize, maxgen, pMut, rememberevals=False,printinterval=0):
        self.particles = [particle(prob) for i in range(Nparticles)]
        self.Nparticles = Nparticles
        self.maxgen = maxgen
        self.pMut = pMut
        self.t = 0 # step
        self.archive = archive(archivesize)
        self.printinterval = printinterval
        self.rememberevals = rememberevals
        self.allevals = []
        for p in self.particles:
            p.evaluate()
            if self.rememberevals: self.allevals.append(p.value)
        self.archive.insert(self.prune())
    
    def step(self):
        self.t += 1
        self.archive.crowding()
        topelements = max(int(self.archive.getlen()*0.10),1)
        top = self.archive.list[:topelements]
        for p in self.particles:
            gbest = choice(top)
            p.updatevelocity(gbest)
            p.updateposition()
            if self.t < self.maxgen*self.pMut:
                f = (1-self.t/(self.maxgen*self.pMut))**1.5
                if flip(f):
                    p.mutate(f)
            p.maintain()
            p.evaluate()
            if self.rememberevals: self.allevals.append(p.value)
        self.archive.insert(self.prune())
        if self.archive.changed: self.archive.tofile(file('front_pl%03i' % self.t, 'w'))
    
    def run(self):
        while self.t < self.maxgen:
            self.step()
#            if self.t % self.printinterval == 0 or self.t == self.maxgen:
#                self.report()
    
#    def report(self):
#        print "Iteration:", self.t, \
#            "Archive size:", self.archive.getlen(), \
#            "Feasible particles:", sum([1 for p in self.particles if p.feasible]), \
#            "Average velocity magnitude:", sum([linalg.norm(p.velocity) for p in self.particles])/self.Nparticles
#         self.archive.report()
#         for p in self.particles: print p 
    
    def prune(self):
        nd = []
        for p in self.particles:
            if p.feasible:
                for ndp in nd:
                    if ndp.dominates(p):
                        break
                else:
                    nd.append(p)          
        return nd
    
    def __repr__(self):
        return "Swarm with %i particles, archive with %i items" % (len(self.particles), self.archive.getlen())


class archive:
    def __init__(self, size):
        self.size = size
        self.list = list()

    def getlen(self):
        return len(self.list)
    
    def insert(self, particles):
#        print "Adding", len(particles), "particles"
        for p in particles:
            self.addevaluation(p.value)
    
    def addevaluation(self, candidate):
        # Strategy: If we have room for the candidate, we append the
        # candidate if it is not dominated by any evaluation in the
        # list.  Otherwise, we have to make room.  We can replace an
        # entry that is dominated by the candidate, but if the
        # candidate is not dominated by any entry, we have to get rid
        # of an entry in the archive.  We do this by culling a crowded
        # value in the most crowded 90% of the list.

        self.changed = False
        beforelen = len(self.list)
        self.list = [e for e in self.list if not candidate.dominates(e)]
        afterlen = len(self.list)

        if beforelen > afterlen:
#            print
#            print "Pruned list", beforelen, afterlen
            self.changed = True
        
        if self.getlen() < self.size:
            for e in self.list:
                if e.dominates(candidate):
                    break
            else:
#                print "Inserting new candidate"
                self.list.append(candidate)
                self.changed = True
        else:
            ins = True # Should we insert this candidate?
            prune = True # Should we discard a crowded value do do so?
#            print self.list
            for i, e in enumerate(self.list):
                if candidate.dominates(e):
                    prune = False # do not prune based on crowding,
                                  # just replace this value
                    break
                elif e.dominates(candidate):
                    ins = False # do not insert if archive dominates
                    break
            if ins:
#                print "Inserting"
                if prune:
                    self.crowding()
                    bottom = floor(self.getlen()*0.9)
                    i = random.randint(bottom, self.getlen()-1)
                self.list[i] = candidate
                self.changed = True
    
    def tofile(self, thefile):
        sortedlist = sorted(self.list, key=lambda v: v.value[0])
        lines = ['\t'.join([str(v) for v in e.value]) for e in sortedlist]
        thefile.write('\n'.join(lines) + '\n')
    
#    def report(self):
#        print "Size of Pareto Set:", self.getlen()
#        for entry in self.list:
#            print entry
    
    def crowding(self):
        # the crowding distance for a particle is the sum of the
        # smallest distances from this particle to its nearest
        # neighbour in terms of the objective values.  We calculate
        # this by sorting the values for each function, calculating
        # the smallest distance and adding over the particles.
        Nitems = self.getlen()
        if Nitems > 1:
            Nvalues = len(self.list[0].value)
            
#            print self.list
            crowdd = zeros(Nitems)
            for f in range(Nvalues):
                indexes, sortedvalue = sortrank(array([item.value[f] for item in self.list]))
		#print len(indexes)
                crowdd += mindist(sortedvalue)
            for i, e in enumerate(self.list):
                e.crowding = crowdd[i]
            self.list.sort(key=lambda e: e.crowding, reverse=True)
    
    def __repr__(self):
        return 'Archive, contains %i points' % self.getlen()


class evaluation:
    def __init__(self, position, value):
        self.position = position
        self.value = value

    def dominance(self, other):
        return sum(self.value < other.value)
    
    def dominates(self, other):
        """Check for domination"""
        return alltrue(self.value < other.value)
    
    def __getitem__(self, N):
        return self.value[N]
    
    def __repr__(self):
        return 'Evaluation at %s. Value %s' % (self.position, self.value)


class cevaluation(evaluation):
    def __init__(self, position, value):
        evaluation.__init__(self, position, value)
        self.crowding = 0

    def __repr__(self):
        return evaluation.__repr__(self) + ' d: ' + str(self.crowding)


class problem:
    """ Generic problem class - simple wrapper """

    def __init__(self, name, xrange, fs):
        self.name = name
        self.xrange = xrange
        self.size = len(xrange)
        self.obnames = ['f' + str(i) for i in range(self.size)]
        self.fs = fs
        
    def initpos(self):
        return random.rand(self.size)

    def get_ranges(self):
        return zip(*self.xrange)

    def feasible(self, position):
        return True

    def evaluate(self, position):
        return cevaluation(position, array(self.fs(position)))
    



# DTLZ6
# (0.0, 1.0)
# f1: x[0]
# f2: x[1]
# f3: s = sum(x)
#     g = 1 + (9/20.0) * s;
#     t = sum(x * ( 1 + sin( 3*pi*x))) / (1 + g)
#     h = 3 - t
#     return (1 + g) * h


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    kita = problem('Kita', 
                   [(0.0, 0.7)]*2, 
                   lambda x: [-x[0]**2 + x[1],
                              x[0]/2.0 + x[1] + 1])
        
    kursawe = problem('Kursawe',
                      [(-5.0, 5.0)]*3, 
                      lambda x: [sum(-10.0 * exp(-0.2 * sqrt(x[:-1]**2 + x[1:]**2))),
                                 sum(abs(x)**0.8 + 5.0*sin(x**3))])
        
    deb = problem('Deb', 
                  [(0.1, 1.0)]*2, 
                  lambda x: [x[0],
                             (2.0 - exp(-((x[1]-0.2)/0.004)**2) - 0.8*exp(-((x[1]-0.6)/0.4))**2)/x[0]])
    
    for prob in (kita, ):
        theswarm = swarm(prob, Nparticles=10, 
                         archivesize=50, 
                         maxgen=10,
                         pMut=0.01,
                         rememberevals=True,
                         printinterval=20)
        theswarm.run()
        plt.figure()
        plt.plot(*zip(*[e.value for e in theswarm.allevals]), color='blue', marker='.', linestyle='')
        plt.plot(*zip(*sorted([list(e.value) for e in theswarm.archive.list])), color='red')
        plt.title(prob.name)
    plt.show()
    
