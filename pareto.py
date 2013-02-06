#!/usr/bin/env python

# Author: Carl Sandrock
    
class domset:
    def __init__(self, obfuns, pop=[]):
        self.obfuns = obfuns
        self.data = []
        self.insertmany(pop)
        
    def evaluate(self, x):
        return [f(x) for f in self.obfuns]

    def insert(self, x):
        fx = self.evaluate(x)
        for existing in self.data[:]:
            fe = self.evaluate(existing)
            fs = zip(fx, fe)
            if all(n < e for n, e in fs):
                self.data.remove(existing)
            if all(n >= e for n, e in fs):
                break # dominated by existing point
        else:
            self.data.append(x)

    def insertmany(self, pop):
        for p in pop:
            self.insert(p)

    def sort(self):
        self.data.sort(key=self.evaluate)

class domsetfromtable(domset):
    def __init__(self, table):
        from operator import itemgetter
        self.obfuns = [itemgetter(i) for i in range(len(table[0]))]
        self.data = []
        self.insertmany(table)
        
if __name__ == "__main__":
    import numpy as np
    import matplotlib.pyplot as pl

    x = np.random.rand(200) * 10
    y = np.random.rand(200) * 10
    good = x**2 + y**2 > 5**2

    x = x[good]
    y = y[good]
    front = domsetfromtable(zip(x, y)).data
    front.sort()
    
    xd, yd = map(np.array, zip(*front))
    pl.plot(x, y, '.', xd, yd, 'ro-')
    pl.show()
    #pl.savefig('samplepareto.pdf')
