''' Demonstrate how to use multi-processing to speed-up I/O bound applications
    such as those commonly found in networking applications.

    Learn to group tasks into parallelizable work (making roads or vacuuming or mowing lawns)
    versus non-parallelizable work that requires sequential step (making babies).

    Three pitfalls of thin channel communication:
    1) Too many trips back and forth
    2) Not doing enough work relative to the travel time
    3) Taking too much with you or bringing too much back

RR1:  Get your app tested and debugged in a singled process mode first
      before you start threading.  Multiprocessing NEVER makes debugging easier.

RR2:  Use caution when multiprocessing or forking from with an IDE.
      Watch-out, you might end-up forking your IDE as well.

GIL:  Global interpreter lock.   CPython has lots of global states.
      There is a lock head whenever that state can be updated
      which is most of the time.  Because of this, multithread code
      in CPython runs as many threads your want but only ONE executes
      at a time.  This means CPython threads are great for IO bound
      and a disaster for CPU bound.

Q. How big should the pool be for multiple processes?
A. Could set it to the number of cores.
   If any processes block, you're better of with more than the number of cores.

How to partition strings into equal length segments:
    >>> s = 'she sells sea shells by the sea shore and peter piper picked a peck of pickled peppers'
    >>> cores = 4
    >>> segment = -(-len(s) // cores)
    >>> segments = [s[i*segment: i*segment+segment] for i in range(cores)]
    >>> sum(pool.imap(lambda s: s.count('e'), segments))       # <-- Don't do this because you're passing in too much data
    >>> sum(pool.map(lambda i: s[i*segment:i*segment+segment].count('e'), range(cores)))  # <-- better to only pass in the segment number

When segmenting data, some care needs to be taken for data at the split boundaries:

    >>> def count_words(s):
            return len(re.findall(r'\w+', s))

    >>> count_words(s)
    17
    >>> sum(map(count_words, segments))
    20
    >>> for seg in segments:
            print count_words(seg), seg

    5 she sells sea shells b
    6 y the sea shore and pe
    5 ter piper picked a pec
    4 k of pickled peppers

                  Good                                   Bad
               -------------------------            ---------------------
With threads:  no communication overhead            GIL limits to 1 thread, Switching overhead
With processes: No GIL, No Switching, Multi-Core    Communication overhead

'''

from pprint import pprint
from itertools import imap, izip
import urllib
import time
from itertools import izip, imap
from contextlib import closing
import urllib

# import requests

IO_BOUND = True

if IO_BOUND:
    # Use separate threads when you are IO bound
    from multiprocessing.pool import ThreadPool as Pool
else:
    # Use separate processes when you are CPU bound
    from multiprocessing.pool import Pool

sites = [
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
    'http://arstechnica.com/',
    'http://www.reuters.com/',
    'http://abcnews.go.com/',
    'http://www.cnbc.com/',
    'http://www.yahoo.com/',
]

def get_page(url):
    with closing(urllib.urlopen(url)) as u:
        return url, u.read()

def get_size(url):
    with closing(urllib.urlopen(url)) as u:
        return url, len(u.read())

pool = Pool(4)
start = time.time()
for url, size in pool.imap_unordered(get_size, sites):
    print size, url
end = time.time()
print end - start





