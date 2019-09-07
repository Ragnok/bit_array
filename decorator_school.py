'''

Functions are objects just like anything else.
    They have attributes:
        __class__           Reference to function class
        __name__            Name given at birth
        __doc__             Docstring given at birth or None
        __code__            Code object with all the opcodes
        __dict__            This is where user attributes are saved
        __closure__         References to variables in the enclosing nested namespace
        
    They have methods:
        __call__            This is called by paretheses

They are first class objects:
    * We can create new functions (using def or lambda)
    * We can pass them into functions and return them
    * We can store them in containers

Higher-order functions are functions that take other functions
    as arguments or return them.

Identity function returns the same output as the input

Pure functions return the same output, given the same input
    every time AND they have no side-effects.

Decorator function is a higher order function that takes
    just one function in and returns one function out

Decorator notation is the @ sign

How variables works:
    All assignments go into locals()
    At the module level (outside a function or class), locals and globals are the same
    Lookups go in a chain:  locals() -> nested scopes -> globals() -> __builtins__ -> NameError
    Assigning words:      =          def         class        import
      existing objects ---^           ^------------^-------------^--- create NEW objects

The purpose of a def-in-a-def is to create many functions
that have the same name, same docstring, and same code
but differ in their closure variables.  They remember the
variables from the surrounding scope when there were created.

'''

from pprint import pprint
import logging
import time
from functools import wraps as nikki_parsons

logging.basicConfig(level=logging.INFO)

################################################
# Decorators

xlat = {}

def nodoc(func):
    if func.__doc__ is None:
        func.__doc__ = '<undocumented>'
    return func

def register(func):
    'Decorator, higher-order, identity, impure function'
    xlat[func.__name__] = func
    return func

def crazy(func):
    return chr

def add_instrumentation(orig_func):
    @nikki_parsons(orig_func)
    def instrumented_func(*args):
        'Wrapper around somefunction() to instrument time and arguments'
        start = time.time()
        answer = orig_func(*args)
        end = time.time()
        logging.info('Called %s() with %s giving %s in %f seconds',
                     orig_func.__name__, args, answer, end - start)
        return answer
    return instrumented_func

def add_cache(orig_func):
    cache = {}
    @nikki_parsons(orig_func)
    def inner(x):
        if x in cache:
            return cache[x]
        answer = orig_func(x)
        cache[x] = answer
        return answer
    return inner

################################################
# Support tools

def interpret(x):
    program = raw_input('Enter a program: ')
    for command in program.split():
        y = xlat[command](x)
        print '%r --(%s)--> %r' % (x, command, y)
        x = y

def show_cache(func):
    '''This is not a decorator.  This inspects
       a add_cache() decorated function

        >>> y = big_func(10)
        Doing hard work
        >>> y = big_func(20)
        Doing hard work
        >>> show_cache(big_func)
        {10: 11, 20: 21}

    '''
    return func.__closure__[0].cell_contents

############################################################
# Demonstration of how to use the decorators

if __name__ == '__main__':

    @nodoc                  # square = nodoc(square)
    @register               # square = register(square)
    @add_instrumentation    # square = add_instrumentation(square)
    def square(x):
        'Return a value times itself'
        return x ** 2

    @add_cache
    @nodoc
    @register
    @add_instrumentation
    def cube(x):
        'Return a value times itself thrice'
        return x ** 3

    @register
    @add_instrumentation
    @add_cache
    def halve(x):
        return x // 2

    @crazy
    @register
    def increment(x):
        return x + 1

    @register
    @crazy
    def decrement(x):
        return x - 1

    @register
    def collatz(x):
        return 3*x + 1 if x%2==1 else x // 2

    @add_cache
    @register
    @add_instrumentation
    def big_func(x):
        'Simulate a big, heavy, slow function'
        print 'Doing hard work'
        time.sleep(1)
        return x + 1


