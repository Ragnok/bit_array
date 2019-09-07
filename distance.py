''' Make a function that computes the distance between two points.

    Real goals:
        - Demonstrate the value of successive refinement
        - Build your numerical analysis sophistication
'''

from math import sqrt, fsum
from itertools import izip

def dist(p, q):
    ''' Compute the distance between two 2-D points on a plane

        >>> dist((97,), (138,))
        41.0
        >>> dist((138,), (97,))
        41.0
        >>> dist((97, 102), (93, 99))
        5.0
        >>> dist((97, 102, 85), (93, 99, 101))
        16.76305461424021

    '''
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/distance-formula-in-3de
    return sqrt(fsum((m - n) ** 2.0 for m, n in izip(p, q)))

if __name__ == '__main__':
    import doctest

    print doctest.testmod()





##def dist1(p, q):
##    '''Compute the distance between two points on a line
##
##        >>> dist1((97,), (138,))
##        41.0
##        >>> dist1((138,), (97,))
##        41.0
##
##    '''
##    x1, = p
##    x2, = q
##    return sqrt((x2 - x1)**2)
##
##def dist2(p, q):
##    ''' Compute the distance between two 2-D points on a plane
##
##        >>> dist2((97, 0), (138, 0))
##        41.0
##        >>> dist2((138, 0), (97, 0))
##        41.0
##        >>> dist2((97, 102), (93, 99))
##        5.0
##
##    '''
##    # http://www.mathwarehouse.com/algebra/distance_formula/index.php
##    x1, y1 = p
##    x2, y2 = q
##    return sqrt((x2 - x1)**2 + (y2 - y1)**2)
