''' Space-efficient, probablistic data structure for fast membership testing.

Learning objectives:
* Build new data structure as required
* Understand deeply how Bloom filters work
* API design patterns -- iterable default input for collections
* range() vs xrange()
* Practice common dunder methods like __init__ and __contains__
* General strategy for optimization:  When using a general purpose tool in special way, don't pay the cost for generalization.
* Quantifer predicates: any() and all()
* Random module:  seed() and sample()
* Engineering methodology for coding -- incremental improvements

'''

from random import seed, sample
from pprint import pprint
try:
    from cbitarray import BitArray
except ImportError:
    from bitarray import BitArray

class BloomFilter:
    'Space-efficient, probablistic data structure'
    # https://en.wikipedia.org/wiki/Bloom_filter

    def __init__(self, iterable=(), population=56, probes=6):
        self.population = xrange(population)
        self.probes = probes
        self.data = BitArray(population)
        for name in iterable:
            self.add(name)

    def add(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        for i in lucky:
            self.data[i] = 1

    def __contains__(self, name):
        seed(name)
        lucky = sample(self.population, self.probes)
        return all(self.data[i] for i in lucky)

if __name__ == '__main__':

    hettingers = BloomFilter('raymond rachel matthew ramon jackie dennis sharon'.split())
    print 'susan' in hettingers
    print 'rachel' in hettingers









        



