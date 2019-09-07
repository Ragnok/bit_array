''' Iterator Protocol -- Universal Design Pattern

ITERABLE:  Anything you can loop over.  It need not be mutable or have state.
    Like a database that is read-only.

    .__iter__              --> Return a fresh NEW iterator
    .__getitem__/__len__   --> Automatically iterable without a __iter__.
                                These are called "Sequence"
                                n = len(s)
                                s[0], s[1], s[2], ..., s[n-1], IndexError

ITERATOR: Object with mutable state that actually does the looping.
    Like a cursor over a database

    .__iter__               --> Return itself (because it is already an iterator, perhaps partially consumed)
    .next()                 --> 1) Fetches and returns a value
                                2) Updates the internal state
                                3) Raise StopIteration when done


Short-cuts:
    iter(obj)               --> obj.__iter__()
    next(it)                --> it.next()

'''

import time

# How to consume iterators #################################

def mylist(iterable):
    '''Loops over an iterable, storing the values in a new list

        >>> mylist('abc')
        ['a', 'b', 'c']
        >>> mylist('')
        []
        >>> mylist((10, 20, 30))
        [10, 20, 30]

    '''
    result = []
    it = iter(iterable)
    while True:
        try:
            value = next(it)
        except StopIteration:
            break
        result.append(value)
    return result

def mylist_better(iterable):
    '''Loops over an iterable, storing the values in a new list

        >>> mylist_better('abc')
        ['a', 'b', 'c']
        >>> mylist_better('')
        []
        >>> mylist_better((10, 20, 30))
        [10, 20, 30]

    '''
    result = []
    for value in iterable:
        result.append(value)
    return result

# How to make iterators ##################################

class MyXrange:
    # ITERABLE class
    '''
        >>> r = MyXrange(10, 15)
        >>> it = iter(r)
        >>> next(it)
        10
        >>> next(it)
        11
        >>> list(it)
        [12, 13, 14]
        >>> for x in MyXrange(10, 15):
        ...	print x
        ...
        10
        11
        12
        13
        14
        >>> sum(MyXrange(10, 15))
        60
        >>> list(MyXrange(10, 15))
        [10, 11, 12, 13, 14]
        >>> mylist(MyXrange(10, 15))
        [10, 11, 12, 13, 14]

    '''

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __repr__(self):
        return 'MyXrange(%d, %d)' % (self.start, self.stop)

    def __iter__(self):
        return MyXrangeIterator(self.start, self.stop)

class MyXrangeIterator:
    # ITERATOR

    def __init__(self, start, stop):
        self.i = start
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        value = self.i
        if value >= self.stop:
            raise StopIteration
        self.i += 1
        return value

def myxrange(start, stop):
    '''
        >>> mylist(myxrange(10, 15))
        [10, 11, 12, 13, 14]

    '''
    i = start
    while i < stop:
        yield i
        i += 1

def myizip(iterable1, iterable2):
    '''
        >>> list(myizip('abc', 'def'))
        [('a', 'd'), ('b', 'e'), ('c', 'f')]
    '''
    it1 = iter(iterable1)
    it2 = iter(iterable2)
    while True:
        try:
            v1 = next(it1)
            v2 = next(it2)
        except StopIteration:
            break
        yield (v1, v2)
    
def myenumerate(iterable, start=0):
    '''
        >>> names = ['raymond', 'rachel', 'matthew']
        >>> list(myenumerate(names, start=1))
        [(1, 'raymond'), (2, 'rachel'), (3, 'matthew')]

    '''
    i = start
    for value in iterable:
        yield i, value
        i += 1

def myreversed(sequence):
    '''
        >>> names = ['raymond', 'rachel', 'matthew']
        >>> list(myreversed(names))
        ['matthew', 'rachel', 'raymond']
    '''
    n = len(sequence)
    for i in xrange(n-1, -1, -1):
        yield sequence[i]


def mycount(start=0):
    '''
        >>> zip(mycount(10), 'abc')
        [(10, 'a'), (11, 'b'), (12, 'c')]
    '''
    i = start
    while True:
        yield i
        i += 1

def myimap(func, iterable):
    '''
        >>> it = myimap(ord, 'Raymond')
        >>> next(it)
        82
        >>> next(it)
        97
        >>> next(it)
        121
    '''
    for x in iterable:
        yield func(x)

def timestamp():
    '''
    >> it = timestamp()
    >> next(it)
    'Fri May 18 08:20:46 2018'
    >> next(it)
    'Fri May 18 08:20:47 2018'

    '''
    while True:
        yield time.ctime()

def user_input():
    '''
        >> list(user_input())
        > Augusta Weather
        > Thunderstorms today
        > Good luck Raymond flying home
        > quit
        ['Augusta Weather', 'Thunderstorms today', 'Good luck Raymond flying home']
    '''
    while True:
        line = raw_input('> ')
        if line == 'quit':
            return
        yield line


if __name__ == '__main__':
    import doctest

    print doctest.testmod()







