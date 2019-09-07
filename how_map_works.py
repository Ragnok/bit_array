'Goal: Learn how the various forms of map() and zip() work'

import time
from itertools import imap, izip
from random import shuffle

los = [
    'the quick brown fox',
    'happy days',
    'come to the aid of their country',
    'she sells sea shells by the sea shore',
]

def mymap(func, iterable):
    result = []
    for x in iterable:
        y = func(x)
        result.append(y)
    return result

def myimap(func, iterable):
    for x in iterable:
        y = func(x)
        yield y

def myimap_unordered(func, iterable):
    data = list(iterable)
    shuffle(data)
    for x in data:
        y = func(x)
        yield y

def mylen(s):
    #print 'Computing the length of %r' % s
    time.sleep(1)
    return s, len(s)

for s, size in myimap_unordered(mylen, los):
    print size, '<--', s[:10]
