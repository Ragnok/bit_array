''' Goals:

* Learn to instrument Python with tracer objects.
* Practice subclass builtin types.
* Review dunder methods:  cmp hash lt le ge eq ne
* Solidify the containers presentation
* Refine your understand of immutability and hashability
* See the effects of the matching logic:
     if a is b: return True              # identity implies equality
     if hash(a) != hash(b): return False # contrapositive of the hash invariant homomorphism
     return a == b

* __cmp__ is a three-way compare:  -1 means less-than     0 means equal         1 means greater-than
* __lt__ __le__ __gt__ __ge__ __eq__ __ne__ are rich comparision -> boolean (or something else for numpy arrays)

* Memory diagram for the class and instances:  https://goo.gl/XcFdmA

'''

from math import log
from bisect import bisect

cmpcnt = 0
hashcnt = 0

def reset():
    global cmpcnt, hashcnt
    cmpcnt = 0
    hashcnt = 0

def show():
    print 'There are {cmpcnt} compares and {hashcnt} hashes'.format(cmpcnt=cmpcnt, hashcnt=hashcnt)

class Int(int):
    'Tracer version of int()'

    def __cmp__(self, other):
        global cmpcnt
        cmpcnt += 1
        print 'Comparing %d to %d' % (self, other)
        return int.__cmp__(self, other)

    def __hash__(self):
        global hashcnt
        hashcnt += 1
        print 'Hashing %s' % self
        return int.__hash__(self)

s = map(Int, [10, 20, 30, 40, 5, 10, 15, 20])
a = Int(11)
b = Int(20)
c = s[2]
n = len(s)

# Study list searches ############################

reset();    print a in s;   show()  # O(n) linear search, left-to-right.  When not found, it takes len(s) compares.
reset();    print b in s;   show()  # Early-out for matches.  "in" operator for lists is faster for successful searches.
reset();    print c in s;   show()  # Identity matches saves exactly one comparison

print 'Predicted sort compares', round(n * log(n, 2))
reset();    s.sort();       show()  # Timsort takes advange of partially sorted data and just merges the monotonic subsequences

print 'Predicted bisect compares', log(n, 2)
reset();    bisect(s, a);   show()  # Bisect always takes log(n) steps regardless of success or identity
reset();    bisect(s, b);   show()
reset();    bisect(s, c);   show()

## Study set (hashtable searches) #################

data = map(Int, [10, 20, 30, 40, 5, 10, 15, 20])
a = Int(11)
b = Int(20)
c = data[2]
n = len(s)

other_data = map(Int, [20, 30, 40, 300, 400, 500, 300]) + data[-4:]
t = set(other_data)

print '=' * 30
reset(); s = set(data);     show()  # Work to build a set: n calls to hash() and 1 compare per non-identical duplicate
reset(); print a in s;      show()  # Cost of unsuccessful search is 1 hash and 0 compares
reset(); print b in s;      show()  # Cost of successful search is 1 hash and 1 compare
reset(); print c in s;      show()  # Cost of successful identity match 1 hash and 0 compares

print '=' * 30                      # Conversion to/from dict takes 0 hashes and 0 compares, same for copy()
reset(); d = dict.fromkeys(s);  show()
reset(); s2 = set(d);       show()
reset(); s3 = s.copy();     show()

reset(); print s & t;       show()  # Union, intersection, difference cost 0 hashes and 1 comparesper non-identical overlap
reset(); print s | t;       show()
reset(); print s - t;       show()

## Immutability and Hashability

'''

Q. Why do we hash?
A. The same reason we use zip codes -- to reduce the search space

Q. Is there a risk?
A. Yes, if you look in the wrong zip code, you'll never find what you're looking for.

Q. Does our notion equality matter?
A. It works as long as the zip codes match the equality relation.
   For example if "Raymond" is deemed equal to "RAYMOND",
   their hash value need to be the same.

Q. How do you say this in technospeak?
A. Hash invariant:

        If x == y, then hash(x) == hash(y)

Q. Do people sometimes mess this up?
A. Yes! They change equality and forget to update the hash.

'''

from random import seed, choice, randrange, random

class CIStr(str):
    'Case insensitive string'

    def __eq__(self, other):        # s == t
        return self.lower() == other.lower()

    def __ne__(self, other):        # s != t
        return self.lower() != other.lower()        

    def __hash__(self):             # hash(s)   <-- dict/set
        return hash(self.lower())

    def __repr__(self):             # >>> s
        return repr(self.lower())


s = CIStr('RACHEL')
t = CIStr('Rachel')
assert s == t
assert len({s, t}) == 1

class WitnessProtectionProgram(str):

    def __hash__(self):
        return randrange(1000000)

bg = WitnessProtectionProgram('Tony Soprano')
safe_house = {bg}

rat = WitnessProtectionProgram('Tony Soprano')
print rat in safe_house

class HashableList(list):
    "Anti-pattern -- Don't do this"

    def __hash__(self):
        return hash(tuple(self))

c = HashableList([10, 20, 30])
s = {c}
print c in s, 'We expect this to be true'
c.append(40)
print c in s, 'We what this to be true but it will fail'

class Person:
    'Legitimate use case for a mutable, hashable class'
    # Core concept:  hash on the immutable portion of the class

    def __init__(self, name, dragons=0):
        self.name = name            # Immutable portion
        self.dragons = dragons      # Mutable portion

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return self.name != other.name

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return 'Person({0!r}, dragons={1})'.format(
            self.name, self.dragons)

d = Person('Danyres', dragons=3)
j = Person('Jon Snow')
w = Person('Ice King')

s = {d, j, w}
print s
d.dragons -= 1
w.dragons += 1
print s

assert d in s and j in s and w in s and len(s) == 3
        






