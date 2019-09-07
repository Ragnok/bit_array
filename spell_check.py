'''Build a spell-checker

Learning objectives:
* When to prefer regexes instead of str.split().
* Avoid \w+ when writing regexes
* Caching expensive constant set-up time using pickle.
* Performance implications (speed/space) of various
  data structures:  lists, sets, and a Bloom filter.
* Factor-out hard-coded behaviors in functions.
* Basic timing techniques.

'''

import re
try:
    import cPickle as pickle
except ImportError:
    import pickle
from bloomfilter import BloomFilter

def make_checker(word_file='notes/words.txt', force_lower=True):
    '''Return a checker correctly spelled words

        >>> 'army' in make_checker()
        True
        >>> 'ahmee' in make_checker()
        False

    '''
    try:
        with open('words.pickle') as cache_file:
            return pickle.load(cache_file)
    except IOError:
        pass
    
    with open(word_file) as f:
        s = f.read()
    if force_lower:
        s = s.lower()
    bf = BloomFilter(s.split(), population=4000000, probes=12)
    
    with open('words.pickle', 'w') as cache_file:
        pickle.dump(bf, cache_file)

    return bf

def spell_check(text, correct_words, word_pattern=r"[A-Za-z'-]+",
                case_insensitive=True):
    ''' Given natural *text* in a string that may contain punction,
        use the *word_pattern* regular expression to isolate words
        to verify whether they are in the the *correct_words*.
        By default, the spelling is case insensitive.

            >>> spell_check('Army Marines', ['army', 'navy', 'airforce'])
            Misspelled
            ----------
            marines
        
    '''
    print 'Misspelled'
    print '----------'
    if case_insensitive:
        text = text.lower()
    for word in re.findall(word_pattern, text):
        if word not in correct_words:
            print word

if __name__ == '__main__':
    import doctest
    import time

    print doctest.testmod()

    correct_words = '''
        a aid all an army assistance at bad be by beautiful
        by child children come country cute don't doesn't
        flag for from go going good he her help his is late
        later man many men my no now of our she some state
        that the their to ugly was with woman women
    '''.split()

    text = '''
        Now, iss the tymme for all
        guhd ood men tooo comee to the
        ayd of thur country and city.
        Don't be leight!
    '''

    start = time.time()
    correct_words = make_checker()
    end = time.time()
    print end - start

    start = time.time()    
    spell_check(text, correct_words)
    end = time.time()
    print end - start
