Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018, 20:59:26) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> #http://bit.ly/python-ar2e

>>> def f(x):
	print x
	print x**2
	print x**3
	print x**4

	
>>> f(11)
11
121
1331
14641
>>> def f(x):
	yield x
	yield x**2
	yield x**3
	yield x**4

	
>>> list(f(11))
[11, 121, 1331, 14641]
>>> set(f(11))
set([121, 11, 14641, 1331])
>>> dict.fromkeys(f(11))
{121: None, 11: None, 14641: None, 1331: None}
>>> for x in f(11):
	print x

	
11
121
1331
14641
>>> zip(range(4), f(11))
[(0, 11), (1, 121), (2, 1331), (3, 14641)]
>>> 
>>> zip('abc', 'defg')
[('a', 'd'), ('b', 'e'), ('c', 'f')]
>>> zip('abcX', 'def')
[('a', 'd'), ('b', 'e'), ('c', 'f')]
>>> # zip(5, infinite) -> 5
>>> 
>>> 
>>> 
>>> from itertools import *
>>> zip(count(10), 'abcde')
[(10, 'a'), (11, 'b'), (12, 'c'), (13, 'd'), (14, 'e')]
>>> count = None
>>> def mycount(start=0):
	i = start
	while True:
		print i
		i += 1

		
>>> mycount(10)
10
11
12
13
14
15
16
17
18
19


Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    mycount(10)
  File "<pyshell#32>", line 4, in mycount
    print i
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> #http://bit.ly/python-ar2e
>>> 
>>> 
>>> #http://bit.ly/python-ar2e
>>> def mycount(start=0):
	i = start
	while True:
		print i
		i += 1

		
>>> def mycount(start=0):
	i = start
	while True:
		yield i
		i += 1

		
>>> g = mycount(10)
>>> next(g)
10
>>> next(g)
11
>>> next(g)
12
>>> zip(g, 'abc')
[(13, 'a'), (14, 'b'), (15, 'c')]
>>> zip(mycount(10), 'abc')
[(10, 'a'), (11, 'b'), (12, 'c')]
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/iterator_school.py ======
TestResults(failed=0, attempted=22)
>>> 
>>> 
>>> from itertools import *
>>> ord('A')
65
>>> chr(65)
'A'
>>> chr(ord(chr(ord(chr(101)))))
'e'
>>> map(ord, 'Raymond')
[82, 97, 121, 109, 111, 110, 100]
>>> it = imap(ord, 'Raymond')
>>> next(it)
82
>>> next(it)
97
>>> next(it)
121
>>> from itertools import *
>>> it = imap(ord, 'Raymond')
>>> next(it)
82
>>> imap = None
>>> 
>>> 
>>> def myimap(func, iterable):
	for x in iterable:
		print func(x)

		
>>> myimap(ord, 'Raymond')
82
97
121
109
111
110
100
>>> def myimap(func, iterable):
	for x in iterable:
		yield func(x)

		
>>> it = myimap(ord, 'Raymond')
>>> next(it)
82
>>> next(it)
97
>>> next(it)
121
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/iterator_school.py ======
TestResults(failed=0, attempted=26)
>>> 
>>> import time
>>> time.ctime()
'Fri May 18 08:19:29 2018'
>>> time.time()
1526645974.562817
>>> def timestamp():
	while True:
		print time.ctime()

		
>>> timestamp()
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:57 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018
Fri May 18 08:19:58 2018


Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    timestamp()
  File "<pyshell#83>", line 3, in timestamp
    print time.ctime()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/idlelib/PyShell.py", line 1356, in write
    return self.shell.write(s, self.tags)
KeyboardInterrupt
>>> def timestamp():
	while True:
		yield time.ctime()

		
>>> it = timestamp()
>>> next(it)
'Fri May 18 08:20:46 2018'
>>> next(it)
'Fri May 18 08:20:47 2018'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/iterator_school.py ======
TestResults(failed=0, attempted=26)
>>> 
>>> 
>>> game = raw_input('Good morning Dr. Falken, do you want to play a game? ')
Good morning Dr. Falken, do you want to play a game? GlobalThermonuclearWar
>>> game
'GlobalThermonuclearWar'
>>> def user_input():
	while True:
		line = raw_input('> ')
		if line == 'quit':
			return
		print line.upper()

		
>>> user_input()
> PT, sir
PT, SIR
> PT, sir
PT, SIR
> We like, we love it
WE LIKE, WE LOVE IT
> We want more of it
WE WANT MORE OF IT
> quit
>>> def user_input():
	while True:
		line = raw_input('> ')
		if line == 'quit':
			return
		yield line

		
>>> list(user_input())
> Augusta Weather
> Thunderstorms today
> Good luck Raymond flying home
> quit
['Augusta Weather', 'Thunderstorms today', 'Good luck Raymond flying home']
>>> log = zip(user_input(), count(1), timestamp())

Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    log = zip(user_input(), count(1), timestamp())
NameError: name 'count' is not defined
>>> log = zip(user_input(), mycount(1), timestamp())
> Now is the time

Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    log = zip(user_input(), mycount(1), timestamp())
  File "/Users/raymond/Dropbox/Public/army2/iterator_school.py", line 206, in timestamp
NameError: global name 'time' is not defined
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/iterator_school.py ======



====== RESTART: /Users/raymond/Dropbox/Public/army2/iterator_school.py ======

=============================== RESTART: Shell ===============================
>>> log = zip(user_input(), mycount(1), timestamp())

Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    log = zip(user_input(), mycount(1), timestamp())
NameError: name 'user_input' is not defined
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/iterator_school.py ======
TestResults(failed=0, attempted=26)
>>> log = zip(user_input(), mycount(1), timestamp())
> Now is the time
> for all good me
> n to come to the
> aid of their country
> 
> Veni, vedi, veci
> quit
>>> from pprint import pprint
>>> pprint(log)
[('Now is the time', 1, 'Fri May 18 08:30:21 2018'),
 ('for all good me', 2, 'Fri May 18 08:30:25 2018'),
 ('n to come to the', 3, 'Fri May 18 08:30:29 2018'),
 ('aid of their country', 4, 'Fri May 18 08:30:37 2018'),
 ('', 5, 'Fri May 18 08:30:37 2018'),
 ('Veni, vedi, veci', 6, 'Fri May 18 08:30:45 2018')]
>>> 
>>> 
>>> 
>>> for c in 'LOVE':
	print c

	
L
O
V
E
>>> for c in 'LOVE':
	for d in 'HATE':
		print c+d

		
LH
LA
LT
LE
OH
OA
OT
OE
VH
VA
VT
VE
EH
EA
ET
EE
>>> for c in 'LOVE':
	for d in 'HATE':
		for e in 'PEACE':
			print c+d+e

			
LHP
LHE
LHA
LHC
LHE
LAP
LAE
LAA
LAC
LAE
LTP
LTE
LTA
LTC
LTE
LEP
LEE
LEA
LEC
LEE
OHP
OHE
OHA
OHC
OHE
OAP
OAE
OAA
OAC
OAE
OTP
OTE
OTA
OTC
OTE
OEP
OEE
OEA
OEC
OEE
VHP
VHE
VHA
VHC
VHE
VAP
VAE
VAA
VAC
VAE
VTP
VTE
VTA
VTC
VTE
VEP
VEE
VEA
VEC
VEE
EHP
EHE
EHA
EHC
EHE
EAP
EAE
EAA
EAC
EAE
ETP
ETE
ETA
ETC
ETE
EEP
EEE
EEA
EEC
EEE
>>> from itertools import product
>>> for c, d in product('LOVE', 'HATE'):
	print c+d

	
LH
LA
LT
LE
OH
OA
OT
OE
VH
VA
VT
VE
EH
EA
ET
EE
>>> for t in product('LOVE', 'HATE'):
	print t

	
('L', 'H')
('L', 'A')
('L', 'T')
('L', 'E')
('O', 'H')
('O', 'A')
('O', 'T')
('O', 'E')
('V', 'H')
('V', 'A')
('V', 'T')
('V', 'E')
('E', 'H')
('E', 'A')
('E', 'T')
('E', 'E')
>>> t
('E', 'E')
>>> ''.join(t)
'EE'
>>> from itertools import *
>>> for s in imap(''.join, product('LOVE', 'HATE')):
	print s

	
LH
LA
LT
LE
OH
OA
OT
OE
VH
VA
VT
VE
EH
EA
ET
EE
>>> print '\n'.join(imap(''.join, product('LOVE', 'HATE')))
LH
LA
LT
LE
OH
OA
OT
OE
VH
VA
VT
VE
EH
EA
ET
EE
>>> print '\n'.join(imap(''.join, product('LOVE', 'LOVE')))
LL
LO
LV
LE
OL
OO
OV
OE
VL
VO
VV
VE
EL
EO
EV
EE
>>> print '\n'.join(imap(''.join, product('LOVE', repeat=2)))
LL
LO
LV
LE
OL
OO
OV
OE
VL
VO
VV
VE
EL
EO
EV
EE
>>> print '\n'.join(imap(''.join, product('LOVE', repeat=3)))
LLL
LLO
LLV
LLE
LOL
LOO
LOV
LOE
LVL
LVO
LVV
LVE
LEL
LEO
LEV
LEE
OLL
OLO
OLV
OLE
OOL
OOO
OOV
OOE
OVL
OVO
OVV
OVE
OEL
OEO
OEV
OEE
VLL
VLO
VLV
VLE
VOL
VOO
VOV
VOE
VVL
VVO
VVV
VVE
VEL
VEO
VEV
VEE
ELL
ELO
ELV
ELE
EOL
EOO
EOV
EOE
EVL
EVO
EVV
EVE
EEL
EEO
EEV
EEE
>>> for p in permutations('LOVE'):
	print p

	
('L', 'O', 'V', 'E')
('L', 'O', 'E', 'V')
('L', 'V', 'O', 'E')
('L', 'V', 'E', 'O')
('L', 'E', 'O', 'V')
('L', 'E', 'V', 'O')
('O', 'L', 'V', 'E')
('O', 'L', 'E', 'V')
('O', 'V', 'L', 'E')
('O', 'V', 'E', 'L')
('O', 'E', 'L', 'V')
('O', 'E', 'V', 'L')
('V', 'L', 'O', 'E')
('V', 'L', 'E', 'O')
('V', 'O', 'L', 'E')
('V', 'O', 'E', 'L')
('V', 'E', 'L', 'O')
('V', 'E', 'O', 'L')
('E', 'L', 'O', 'V')
('E', 'L', 'V', 'O')
('E', 'O', 'L', 'V')
('E', 'O', 'V', 'L')
('E', 'V', 'L', 'O')
('E', 'V', 'O', 'L')
>>> for p in permutations('LOVE', 2):
	print p

	
('L', 'O')
('L', 'V')
('L', 'E')
('O', 'L')
('O', 'V')
('O', 'E')
('V', 'L')
('V', 'O')
('V', 'E')
('E', 'L')
('E', 'O')
('E', 'V')
>>> for p in combinations('LOVE', 2):
	print p

	
('L', 'O')
('L', 'V')
('L', 'E')
('O', 'V')
('O', 'E')
('V', 'E')
>>> # Jedi47mattheW
>>> # JEDI
>>> # jEDI
>>> 
>>> #    1
>>> #    2
>>> #    1900-2100
>>> 
>>> def square(x):
	'Return a value times itself'
	return x ** 2

>>> square
<function square at 0x106f89e60>
>>> id(square)
4411924064
>>> hex(id(square))
'0x106f89e60'
>>> 
>>> type(square)
<type 'function'>
>>> square.__class__
<type 'function'>
>>> square.__name__
'square'
>>> square.__doc__
'Return a value times itself'
>>> square.__code__
<code object square at 0x106c7e930, file "<pyshell#157>", line 1>
>>> square.__code__.co_code
'|\x00\x00d\x01\x00\x13S'
>>> map(ord, square.__code__.co_code)
[124, 0, 0, 100, 1, 0, 19, 83]
>>> from dis import dis
>>> dis(square)
  3           0 LOAD_FAST                0 (x)
              3 LOAD_CONST               1 (2)
              6 BINARY_POWER        
              7 RETURN_VALUE        
>>> map(square, range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> s = [square, pow]
>>> s[0](10)
100
>>> s[1](2, 5)
32
>>> square(5)
25
>>> #     ^--- __call__
>>> square.__call__(5)
25
>>> square.__class__
<type 'function'>
>>> square.__class__.__class__
<type 'type'>
>>> square.__class__.__class__.__class__
<type 'type'>
>>> square.__class__.__class__.__class__.__class__
<type 'type'>
>>> 
>>> f = square
>>> f(5)
25
>>> f is square
True
>>> f.__name__
'square'
>>> f.__doc__
'Return a value times itself'
>>> f.__name__ = 'pointy_circle'
>>> f.__doc__ = 'what you get when smush a circle'
>>> 
>>> help(square)
Help on function pointy_circle in module __main__:

pointy_circle(x)
    what you get when smush a circle

>>> class A:
	pass

>>> a = A()
>>> 
>>> a.__class__
<class __main__.A at 0x107038188>
>>> a.__dict__
{}
>>> 
>>> a.x = 10
>>> a.__dict__
{'x': 10}
>>> square.x = 15
>>> square.__dict__
{'x': 15}
>>> dir(square)
['__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__doc__', '__format__', '__get__', '__getattribute__', '__globals__', '__hash__', '__init__', '__module__', '__name__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'func_closure', 'func_code', 'func_defaults', 'func_dict', 'func_doc', 'func_globals', 'func_name', 'x']
>>> 
>>> map(ord, 'Raymond')
[82, 97, 121, 109, 111, 110, 100]
>>> def f():
	return ord

>>> f()
<built-in function ord>
>>> f()('A')
65
>>> 
>>> 
>>> 
>>> x = 10
>>> y = x + 1
>>> y
11
>>> y = 11
>>> 
>>> 
>>> x = 10
>>> x = x
>>> x = 10
>>> 
>>> x = x
>>> 
>>> 
>>> def f(x):
	return x

>>> f(5)
5
>>> f('hello')
'hello'
>>> f(ord)
<built-in function ord>
>>> f(ord)('A')
65
>>> 
>>> x = 10
>>> x = f(x)
>>> x
10
>>> def f(x):
	print 'Howdy!'
	return x

>>> x = f(x)
Howdy!
>>> x
10
>>> 
>>> x = 10
>>> y = 100
>>> def f(x):
	global y
	y += 1
	return x

>>> x = f(x)
>>> y
101
>>> square(5)
25
>>> square(6)
36
>>> square(5)
25
>>> square(6)
36
>>> import time
>>> time.time()
1526648904.380829
>>> time.time()
1526648906.518344
>>> from random import *
>>> randrange(1000, 2000, 100)
1600
>>> randrange(1000, 2000, 100)
1300
>>> 
>>> 
>>> def square(x):
	'Return a value times itself'
	return x ** 2

>>> xlat = {}
>>> 
>>> def register(func):
	xlat[func.__name__] = func
	return func

>>> square = register(square)
>>> square(5)
25
>>> xlat
{'square': <function square at 0x107058c80>}
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> xlat
{'square': <function square at 0x10051db90>}
>>> square(5)
25
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> xlat
{'collatz': <function collatz at 0x104c17de8>, 'square': <function square at 0x104c17b90>}
>>> xlat['collatz'](10)
5
>>> xlat['collatz'](11)
34
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> big_func(10)
Doing hard work
11
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> square(10)
100
>>> halve(10)
5
>>> increment(10)
11
>>> decrement(10)
9
>>> collatz(10)
5
>>> collatz(11)
34
>>> cube(10)
100
>>> 
>>> 
>>> pprint(xlat)
{'big_func': <function big_func at 0x108d77488>,
 'collatz': <function collatz at 0x108d77410>,
 'cube': <function cube at 0x108d77230>,
 'decrement': <function decrement at 0x108d77398>,
 'halve': <function halve at 0x108d772a8>,
 'increment': <function increment at 0x108d77320>,
 'square': <function square at 0x108d771b8>}
>>> 
>>> program = raw_input('Enter a program: ')
Enter a program: cube halve halve increment collatz square
>>> program
'cube halve halve increment collatz square'
>>> program.split()
['cube', 'halve', 'halve', 'increment', 'collatz', 'square']
>>> x = 10
>>> for command in program.split():
	y = xlat[command](x)
	print '%r --(%s)--> %r' % (x, command, y)
	x = y

	
10 --(cube)--> 100
100 --(halve)--> 50
50 --(halve)--> 25
25 --(increment)--> 26
26 --(collatz)--> 13
13 --(square)--> 169
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> interpret(50)
Enter a program: halve cube increment
50 --(halve)--> 25
25 --(cube)--> 15625
15625 --(increment)--> 15626
>>> big_func(10)
Doing hard work
11
>>> square.__doc__
'Return a value times itself'
>>> cube.__doc__
>>> 
>>> cube.__doc__ = '<undocumented>'
>>> 
>>> help(cube)
Help on function cube in module __main__:

cube(x)
    <undocumented>

>>> halve.__doc__
>>> 
>>> def nodoc(func):
	if func.__doc__ is None:
		func.__doc__ = '<undocumented>'
	return func

>>> 
>>> square = nodoc(square)
>>> halve = nodoc(halve)
>>> 
>>> help(square)
Help on function square in module __main__:

square(x)
    Return a value times itself

>>> help(halve)
Help on function halve in module __main__:

halve(x)
    <undocumented>

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> help(cube)
Help on function cube in module __main__:

cube(x)
    <undocumented>

>>> def crazy(func):
	return chr

>>> @crazy
def square(x):
	return x ** 2

>>> square(65)
'A'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> decrement(66)
'B'
>>> increment(67)
'C'
>>> xlat['decrement'](65)

Traceback (most recent call last):
  File "<pyshell#333>", line 1, in <module>
    xlat['decrement'](65)
KeyError: 'decrement'
>>> pprint(xlat)
{'big_func': <function big_func at 0x1112e85f0>,
 'chr': <built-in function chr>,
 'collatz': <function collatz at 0x1112e8578>,
 'cube': <function cube at 0x1112e8410>,
 'halve': <function halve at 0x1112e8488>,
 'increment': <function increment at 0x1112e8500>,
 'square': <function square at 0x1112e8398>}
>>> 

>>> 
=============================== RESTART: Shell ===============================
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> x = 10
>>> globals()['x']
10
>>> globals()['x'] = 11
>>> x
11
>>> sorted(globals().keys())
['__builtins__', '__doc__', '__name__', '__package__', 'x']
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'x']
>>> 
>>> locals()['x']
11
>>> locals()['x'] = 12
>>> x
12
>>> globals()['x']
12
>>> locals() == globals()
True
>>> 
>>> x = 10
  File "<pyshell#350>", line 1
    = 10
    ^
IndentationError: unexpected indent
>>> y

Traceback (most recent call last):
  File "<pyshell#351>", line 1, in <module>
    y
NameError: name 'y' is not defined

>>> 
>>> x = 10
>>> y = 20
>>> 
>>> f(x):
	
SyntaxError: invalid syntax
>>> def f(x):
	z = x + 1
	print locals()

	
>>> f(5)
{'x': 5, 'z': 6}
>>> x
10
>>> def f(x):
	z = x + 1
	print locals()
	print x, y, z

	
>>> f(5)
{'x': 5, 'z': 6}
5 20 6
>>> 
>>> # All assignments go into locals()
>>> # At the module level (outside a function or class), locals and globals are the same
>>> # Lookups go in a chain:  locals() -> globals()
>>> len('hello')
5
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'f', 'x', 'y']
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']
>>> 
>>> def len(obj):
	return 42

>>> len('hello')
42
>>> del len
>>> len('hello')
5
>>> # Lookups go in a chain:  locals() -> globals() -> __builtins__
>>> 
>>> 
>>> from os import *
>>> cwd()

Traceback (most recent call last):
  File "<pyshell#385>", line 1, in <module>
    cwd()
NameError: name 'cwd' is not defined
>>> getcwd()
'/Users/raymond/Dropbox/Public/army2'
>>> chdir('pub')
>>> listdir('.')
['kmeans.html', 'day4.html', 'decorator_school.html', 'k_nearest.html', 'study_irises.html', 'index.html', 'bitarray.html', 'day5.html', 'spell_check.html', 'day2b.html', 'distance.html', 'multiprocessing_demo.html', 'threading_demo.html', 'multiple_inheritance.html', 'day2.html', 'day3.html', 'day1b.html', 'steps.html', 'threading_demo_fuzzing.html', 'day1a.html', 'day1_36.html', 'params.html', 'iterator_school.html', 'download.html', 'bloomfilter.html', 'k_neerest.html', 'how_map_works.html', 'grouping_demo.html', 'instrument.html']
>>> chdir('..')
>>> getcwd()
'/Users/raymond/Dropbox/Public/army2'
>>> f = open('notes/hamlet.txt')

Traceback (most recent call last):
  File "<pyshell#391>", line 1, in <module>
    f = open('notes/hamlet.txt')
TypeError: function takes at least 2 arguments (1 given)
>>> f = open('notes/hamlet.txt', 0)
>>> type(f)
<type 'int'>
>>> f
11
>>> import os
>>> dir(os)
['EX_CANTCREAT', 'EX_CONFIG', 'EX_DATAERR', 'EX_IOERR', 'EX_NOHOST', 'EX_NOINPUT', 'EX_NOPERM', 'EX_NOUSER', 'EX_OK', 'EX_OSERR', 'EX_OSFILE', 'EX_PROTOCOL', 'EX_SOFTWARE', 'EX_TEMPFAIL', 'EX_UNAVAILABLE', 'EX_USAGE', 'F_OK', 'NGROUPS_MAX', 'O_APPEND', 'O_ASYNC', 'O_CREAT', 'O_DIRECTORY', 'O_DSYNC', 'O_EXCL', 'O_EXLOCK', 'O_NDELAY', 'O_NOCTTY', 'O_NOFOLLOW', 'O_NONBLOCK', 'O_RDONLY', 'O_RDWR', 'O_SHLOCK', 'O_SYNC', 'O_TRUNC', 'O_WRONLY', 'P_NOWAIT', 'P_NOWAITO', 'P_WAIT', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'UserDict', 'WCONTINUED', 'WCOREDUMP', 'WEXITSTATUS', 'WIFCONTINUED', 'WIFEXITED', 'WIFSIGNALED', 'WIFSTOPPED', 'WNOHANG', 'WSTOPSIG', 'WTERMSIG', 'WUNTRACED', 'W_OK', 'X_OK', '_Environ', '__all__', '__builtins__', '__doc__', '__file__', '__name__', '__package__', '_copy_reg', '_execvpe', '_exists', '_exit', '_get_exports_list', '_make_stat_result', '_make_statvfs_result', '_pickle_stat_result', '_pickle_statvfs_result', '_spawnvef', 'abort', 'access', 'altsep', 'chdir', 'chflags', 'chmod', 'chown', 'chroot', 'close', 'closerange', 'confstr', 'confstr_names', 'ctermid', 'curdir', 'defpath', 'devnull', 'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fchdir', 'fchmod', 'fchown', 'fdopen', 'fork', 'forkpty', 'fpathconf', 'fstat', 'fstatvfs', 'fsync', 'ftruncate', 'getcwd', 'getcwdu', 'getegid', 'getenv', 'geteuid', 'getgid', 'getgroups', 'getloadavg', 'getlogin', 'getpgid', 'getpgrp', 'getpid', 'getppid', 'getsid', 'getuid', 'initgroups', 'isatty', 'kill', 'killpg', 'lchflags', 'lchmod', 'lchown', 'linesep', 'link', 'listdir', 'lseek', 'lstat', 'major', 'makedev', 'makedirs', 'minor', 'mkdir', 'mkfifo', 'mknod', 'name', 'nice', 'open', 'openpty', 'pardir', 'path', 'pathconf', 'pathconf_names', 'pathsep', 'pipe', 'popen', 'popen2', 'popen3', 'popen4', 'putenv', 'read', 'readlink', 'remove', 'removedirs', 'rename', 'renames', 'rmdir', 'sep', 'setegid', 'seteuid', 'setgid', 'setgroups', 'setpgid', 'setpgrp', 'setregid', 'setreuid', 'setsid', 'setuid', 'spawnl', 'spawnle', 'spawnlp', 'spawnlpe', 'spawnv', 'spawnve', 'spawnvp', 'spawnvpe', 'stat', 'stat_float_times', 'stat_result', 'statvfs', 'statvfs_result', 'strerror', 'symlink', 'sys', 'sysconf', 'sysconf_names', 'system', 'tcgetpgrp', 'tcsetpgrp', 'tempnam', 'times', 'tmpfile', 'tmpnam', 'ttyname', 'umask', 'uname', 'unlink', 'unsetenv', 'urandom', 'utime', 'wait', 'wait3', 'wait4', 'waitpid', 'walk', 'write']
>>> from os import *
>>> 
=============================== RESTART: Shell ===============================
>>> from os import getcwd, listdir
>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'getcwd', 'listdir']
>>> import os
>>> os.getcwd()
'/Users/raymond/Dropbox/Public/army2'
>>> from turtle import *
>>> shape('turtle')
>>> forward(10)
>>> forward(90)
>>> right(90)
>>> forward(100)
>>> import turtle
>>> turtle.color('red')
>>> turtle.width(10)
>>> turtle.right(90)
>>> turtle.forward(100)
>>> 
=============================== RESTART: Shell ===============================
>>> xyzpdq

Traceback (most recent call last):
  File "<pyshell#413>", line 1, in <module>
    xyzpdq
NameError: name 'xyzpdq' is not defined
>>> # All assignments go into locals()
>>> # At the module level (outside a function or class), locals and globals are the same
>>> # Lookups go in a chain:  locals() -> globals() -> __builtins__ -> NameError
>>> 
>>> 
>>> 
>>> 
=============================== RESTART: Shell ===============================
>>> # Assigning words
>>> x = 10
>>> def square(x):
	return x ** 2

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__', 'square', 'x']
>>> class Router:
	pass

>>> dir()
['Router', '__builtins__', '__doc__', '__name__', '__package__', 'square', 'x']
>>> 
>>> import collections
>>> 
>>> dir()
['Router', '__builtins__', '__doc__', '__name__', '__package__', 'collections', 'square', 'x']
>>> 
>>> type(collections)
<type 'module'>
>>> type(square)
<type 'function'>
>>> type(Router)
<type 'classobj'>
>>> type(x)
<type 'int'>
>>> coll = collections
>>> coll is collections
True
>>> def f(x):
	y = x + 1
	import math
	class Switch:
		pass
	def g(z):
		pass
	print locals()

	
>>> f(5)
{'y': 6, 'x': 5, 'Switch': <class __main__.Switch at 0x10e794600>, 'math': <module 'math' from '/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/lib-dynload/math.so'>, 'g': <function g at 0x10ccbab90>}
>>> 
>>> 
>>> def f(x):
	def g(y):
		print x, y
	g(10)

	
>>> x = 100
>>> f(5)
5 10
>>> 
>>> # Literals and Keywords:
>>> #   "...."   -> string object:   data: hello        methods:  upper lower split join
>>> #   1234     -> integer object:  data: 1234         methods:  __add__ __mul__
>>> #   def ...  -> function object: data: 124 0 0      methods:  __call__
>>> #   class ...-> class object:    data: attr/method  methods:  __call__
>>> #   import ..-> module object:   data: var/func/class  methods: __getattribute__
>>> 
>>> import math
>>> math.pi
3.141592653589793
>>> math.__dict__.keys()
['pow', 'fsum', 'cosh', 'ldexp', 'hypot', 'acosh', 'tan', 'asin', 'isnan', 'log', 'fabs', 'floor', 'atanh', 'modf', 'sqrt', '__package__', 'frexp', 'degrees', 'lgamma', 'log10', '__doc__', 'asinh', 'fmod', 'atan', 'factorial', '__file__', 'copysign', 'expm1', 'ceil', 'isinf', 'sinh', '__name__', 'trunc', 'cos', 'pi', 'e', 'tanh', 'radians', 'sin', 'atan2', 'erf', 'erfc', 'exp', 'acos', 'log1p', 'gamma']
>>> math.pi
3.141592653589793
>>> math.__dict__['pi']
3.141592653589793
>>> object.__getattribute__(math, 'pi')
3.141592653589793
>>> def salute(self):
	print 'Aye, aye sir'

	
>>> Sailor = type('Sailor', (object,), {'salute': salute})
>>> type(Sailor)
<type 'type'>
>>> 
>>> popeye = Sailor()
>>> bluto = Sailor()
>>> 
>>> popeye
<__main__.Sailor object at 0x10e79c910>
>>> bluto
<__main__.Sailor object at 0x10e79c2d0>
>>> popeye.salute()
Aye, aye sir
>>> bluto.salute()
Aye, aye sir
>>> sailor = type('sailor', (object,), {'salute': salute})
>>> popeye = sailor()
>>> 
>>> def recuit_navy():
	return sailor()

>>> type(recuit_navy)
<type 'function'>
>>> ahab = recuit_navy()
>>> ahab.salute()
Aye, aye sir
>>> 
>>> # Lookups go in a chain:  locals() -> globals() -> __builtins__ -> NameError
>>> 
>>> 
>>> 
>>> 
>>> def f(x):
	def g(y):
		print x, y
	g(10)

	
>>> f(5)
5 10
>>> def f(x):
	def g(y):
		print x, y
	return g

>>> h = f(5)
>>> h(7)
5 7
>>> h.__name__
'g'
>>> h.__code__.co_code
'\x88\x00\x00G|\x00\x00GHd\x00\x00S'
>>> h.__doc__ is None
True
>>> h.__closure__
(<cell at 0x10e56b638: int object at 0x7fb73e60b3e8>,)
>>> h.__closure__[0]
<cell at 0x10e56b638: int object at 0x7fb73e60b3e8>
>>> h.__closure__[0].cell_contents
5
>>> def f(x):
	'I am eff'
	def g(y):
		'I am gee'
		print x, y
	return g

>>> h = f(5)
>>> i = f(6)
>>> j = f(7)
>>> 
>>> funcs = [h, i, j]
>>> [type(func) for func in funcs]
[<type 'function'>, <type 'function'>, <type 'function'>]
>>> [hex(id(func)) for func in funcs]
['0x10ccbab90', '0x10e79daa0', '0x10e79db18']
>>> [func.__name__ for func in funcs]
['g', 'g', 'g']
>>> [func.__doc__ for func in funcs]
['I am gee', 'I am gee', 'I am gee']
>>> [func.__code__.co_code for func in funcs]
['\x88\x00\x00G|\x00\x00GHd\x01\x00S', '\x88\x00\x00G|\x00\x00GHd\x01\x00S', '\x88\x00\x00G|\x00\x00GHd\x01\x00S']
>>> [func(10) for func in funcs]
5 10
6 10
7 10
[None, None, None]
>>> [func.__closure__[0].cell_contents for func in funcs]
[5, 6, 7]
>>> 
>>> 
>>> a, b, c = [10, 20, 30]
>>> a
10
>>> b
20
>>> c
30
>>> map(lambda x: x**2, range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> a, b, c = map(lambda x: x**2, range(3))
>>> 
>>> 
>>> def f(x):
	'I am eff'
	def g(y):
		'I am gee'
		print x, y
	return g

>>> a, b, c = map(f, [5, 6, 7])
>>> a
<function g at 0x10e79db90>
>>> b
<function g at 0x10e79d410>
>>> c
<function g at 0x10e79dc80>
>>> a(10)
5 10
>>> b(10)
6 10
>>> c(10)
7 10
>>> 
>>> 
>>> 
>>> pow(2, 5)
32
>>> b = 2
>>> e = 5
>>> p = pow(b, e)
>>> import time
>>> import logging
>>> logging.basicConfig(level=logging.INFO)
>>> 
>>> def instrumented_pow(b, e):
	'Wrapper around pow() to instrument time and arguments'
	start = time.time()
	answer = pow(b, e)
	end = time.time()
	logging.info('Called pow() with %d %d giving %d in %f seconds',
		     b, e, answer, end - start)
		     
	return answer

>>> p = instrumented_pow(b, e)
INFO:root:Called pow() with 2 5 giving 32 in 0.000004 seconds
>>> 
>>> 
>>> 
>>> a = 2 + 5
>>> b = 2 + 6
>>> c = 2 + 7
>>> def f():
	return 2 + 5

>>> a = f()
>>> a
7
>>> def f(x):
	return 2 + x

>>> f(5)
7
>>> f(6)
8
>>> f(7)
9
>>> def addtwo(x):
	return 2 + x

>>> a, b, c, d, e, f, g, h, i, j = map(addtwo, range(5, 15))
>>> 
>>> 
>>> a = 3 + 5
>>> a = 3 + 5
>>> a = 3 + 6
>>> 
>>> def addthree(x):
	return 3 + x

>>> map(addthree, range(5, 15))
[8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
>>> def addtwo(x):
	return 2 + x

>>> def addthree(x):
	return 3 + x

>>> def addfour(x):
	return 4 + x

>>> def f():
	def addtwo(x):
		return 2 + x
	return addtwo

>>> addtwo = f()
>>> addtwo(10)
12
>>> def make_adder(y):
	def add_something(x):
		return y + x
	return add_something

>>> addtwo = make_adder(2)
>>> addthree = make_adder(3)
>>> addfour = make_adder(4)
>>> 
>>> 
>>> addtwo(10)
12
>>> addthree(10)
13
>>> addfour(10)
14
>>> def make_adder(y):
	def add_something(x):
		return y + x
	return add_something

>>> addtwo, addthree, addfour, addfive, addsix, addseven = map(make_adder, range(2, 8))
>>> 
>>> add2, add3, add4, add5, add6, add7 = map(make_adder, range(2, 8))
>>> 
>>> def name(n):
	return 'add%d' % n

>>> name2

Traceback (most recent call last):
  File "<pyshell#628>", line 1, in <module>
    name2
NameError: name 'name2' is not defined
>>> name(2)
'add2'
>>> 
>>> def add4(x):
	return 4 + x

>>> for n in range(2, 100):
	locals()[name[n]] = make_adder(n)

	

Traceback (most recent call last):
  File "<pyshell#635>", line 2, in <module>
    locals()[name[n]] = make_adder(n)
TypeError: 'function' object has no attribute '__getitem__'
>>> for n in range(2, 100):
	locals()[name(n)] = make_adder(n)

	
>>> dir()
['Router', 'Sailor', '__builtins__', '__doc__', '__name__', '__package__', 'a', 'add10', 'add11', 'add12', 'add13', 'add14', 'add15', 'add16', 'add17', 'add18', 'add19', 'add2', 'add20', 'add21', 'add22', 'add23', 'add24', 'add25', 'add26', 'add27', 'add28', 'add29', 'add3', 'add30', 'add31', 'add32', 'add33', 'add34', 'add35', 'add36', 'add37', 'add38', 'add39', 'add4', 'add40', 'add41', 'add42', 'add43', 'add44', 'add45', 'add46', 'add47', 'add48', 'add49', 'add5', 'add50', 'add51', 'add52', 'add53', 'add54', 'add55', 'add56', 'add57', 'add58', 'add59', 'add6', 'add60', 'add61', 'add62', 'add63', 'add64', 'add65', 'add66', 'add67', 'add68', 'add69', 'add7', 'add70', 'add71', 'add72', 'add73', 'add74', 'add75', 'add76', 'add77', 'add78', 'add79', 'add8', 'add80', 'add81', 'add82', 'add83', 'add84', 'add85', 'add86', 'add87', 'add88', 'add89', 'add9', 'add90', 'add91', 'add92', 'add93', 'add94', 'add95', 'add96', 'add97', 'add98', 'add99', 'addfive', 'addfour', 'addseven', 'addsix', 'addthree', 'addtwo', 'ahab', 'b', 'bluto', 'c', 'coll', 'collections', 'd', 'e', 'f', 'func', 'funcs', 'g', 'h', 'i', 'instrumented_pow', 'j', 'logging', 'make_adder', 'math', 'n', 'name', 'p', 'popeye', 'recuit_navy', 'sailor', 'salute', 'square', 'time', 'x']
>>> add91(100)
191
>>> def instrumented_pow(b, e):
	'Wrapper around pow() to instrument time and arguments'
	start = time.time()
	answer = pow(b, e)
	end = time.time()
	logging.info('Called pow() with %d %d giving %d in %f seconds',
		     b, e, answer, end - start)

	return answer

>>> p = instrumented_pow(b, e)
INFO:root:Called pow() with 8 11 giving 8589934592 in 0.000001 seconds
>>> c = 'A'
>>> n = ord(c)
>>> def instrumented_ord(c):
	'Wrapper around ord() to instrument time and arguments'
	start = time.time()
	answer = ord(c)
	end = time.time()
	logging.info('Called ord() with %s giving %d in %f seconds',
		     c, answer, end - start)
	return answer

>>> n = instrumented_ord(c)
INFO:root:Called ord() with A giving 65 in 0.000001 seconds
>>> p = instrumented_pow(b, e)
INFO:root:Called pow() with 8 11 giving 8589934592 in 0.000002 seconds
>>> n = 50
>>> cp = chr(n)
>>> def instrumented_chr(n):
	'Wrapper around chr() to instrument time and arguments'
	start = time.time()
	answer = chr(n)
	end = time.time()
	logging.info('Called chr() with %s giving %s in %f seconds',
		     n, answer, end - start)
	return answer

>>> cp = instrumented_chr(50)
INFO:root:Called chr() with 50 giving 2 in 0.000001 seconds
>>> chr(50)
'2'
>>> cp = instrumented_chr(65)
INFO:root:Called chr() with 65 giving A in 0.000003 seconds
>>> def f():
	def instrumented_chr(n):
		'Wrapper around chr() to instrument time and arguments'
		start = time.time()
		answer = chr(n)
		end = time.time()
		logging.info('Called chr() with %s giving %s in %f seconds',
			     n, answer, end - start)
		return answer
	return instrumented_chr

>>> instrumented_chr = f()
>>> cp = instrumented_chr(65)
INFO:root:Called chr() with 65 giving A in 0.000003 seconds
>>> def add_instrumentation(orig_func):
	def instrumented_func(*args):
		'Wrapper around somefunction() to instrument time and arguments'
		start = time.time()
		answer = orig_func(*args)
		end = time.time()
		logging.info('Called %s() with %s giving %s in %f seconds',
			     orig_func.__name__, args, answer, end - start)
		return answer
	return instrumented_chr

>>> def add_instrumentation(orig_func):
	def instrumented_func(*args):
		'Wrapper around somefunction() to instrument time and arguments'
		start = time.time()
		answer = orig_func(*args)
		end = time.time()
		logging.info('Called %s() with %s giving %s in %f seconds',
			     orig_func.__name__, args, answer, end - start)
		return answer
	return instrumented_func

>>> instrumented_chr = add_instrumentation(chr)
>>> instrumented_ord = add_instrumentation(ord)
>>> instrumented_pow = add_instrumentation(pow)
>>> 
>>> cp = instrumented_chr(65)
INFO:root:Called chr() with (65,) giving A in 0.000002 seconds
>>> cp = instrumented_pow(2, 5)
INFO:root:Called pow() with (2, 5) giving 32 in 0.000003 seconds
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> x = 10
>>> y = square(10)
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> x = 10
>>> y = square(x)
INFO:root:Called square() with (10,) giving 100 in 0.000002 seconds
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> y = cube(10)
INFO:root:Called cube() with (10,) giving 1000 in 0.000002 seconds
>>> y = halve(10)
INFO:root:Called halve() with (10,) giving 5 in 0.000002 seconds
>>> 
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> x = 10
>>> y = big_func(10)
Doing hard work
INFO:root:Called big_func() with (10,) giving 11 in 1.069154 seconds
>>> y = big_func(20)
Doing hard work
INFO:root:Called big_func() with (20,) giving 21 in 1.102940 seconds
>>> y = big_func(10)
Doing hard work
INFO:root:Called big_func() with (10,) giving 11 in 1.079210 seconds
>>> 
>>> # memoization
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> y = big_func(10)
Doing hard work
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> y = big_func(10)
Doing hard work
>>> y
11
>>> bf_cache
{10: 11}
>>> y = big_func(20)
Doing hard work
>>> bf_cache
{10: 11, 20: 21}
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> y = big_func(10)
Doing hard work
>>> y = big_func(20)
Doing hard work
>>> y = big_func(10)
>>> y
11
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> big_func(10)
Doing hard work
11
>>> big_func(20)
Doing hard work
21
>>> cube(10)
1000
>>> bf_cache
{10: 11, 20: 21}
>>> cu_cache
{10: 1000}
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> cube(10)
1000
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> big_func(10)

Traceback (most recent call last):
  File "<pyshell#701>", line 1, in <module>
    big_func(10)
  File "/Users/raymond/Dropbox/Public/army2/decorator_school.py", line 134, in inner
    if x in cu_cache:
NameError: global name 'cu_cache' is not defined
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> big_func(10)
Doing hard work
INFO:root:Called big_func() with (10,) giving 11 in 1.088968 seconds
11
>>> big_func(20)
Doing hard work
INFO:root:Called big_func() with (20,) giving 21 in 1.063500 seconds
21
>>> big_func(10)
11
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> big_func(10)
Doing hard work
INFO:root:Called big_func() with (10,) giving 11 in 1.080507 seconds
11
>>> big_func(10)
11
>>> halve(10)
INFO:root:Called inner() with (10,) giving 5 in 0.000008 seconds
5
>>> halve(10)
INFO:root:Called inner() with (10,) giving 5 in 0.000002 seconds
5
>>> big_func.__closure__
(<cell at 0x1115ae948: dict object at 0x111588910>, <cell at 0x1115ae980: function object at 0x1115be500>)
>>> big_func.__closure__[1]
<cell at 0x1115ae980: function object at 0x1115be500>
>>> big_func.__closure__[1].cell_contents
<function instrumented_func at 0x1115be500>
>>> big_func.__closure__[1].cell_contents(1)
Doing hard work
INFO:root:Called big_func() with (1,) giving 2 in 1.077370 seconds
2
>>> big_func.__closure__[0]
<cell at 0x1115ae948: dict object at 0x111588910>
>>> big_func.__closure__[0].cell_contents
{10: 11}
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> big_func(50)
Doing hard work
INFO:root:Called big_func() with (50,) giving 51 in 1.098363 seconds
51
>>> big_func(70)
Doing hard work
INFO:root:Called big_func() with (70,) giving 71 in 1.080460 seconds
71
>>> show_cache(big_func)
{50: 51, 70: 71}
>>> big_func.__closure__[0].cell_contents
{50: 51, 70: 71}
>>> big_func.__closure__[0].cell_contents[70] = 75
>>> 
>>> 
>>> big_func(60)
Doing hard work
INFO:root:Called big_func() with (60,) giving 61 in 1.072966 seconds
61
>>> big_func(70)
75
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> 
>>> 
>>> big_func(10)
Doing hard work
INFO:root:Called big_func() with (10,) giving 11 in 1.082900 seconds
11
>>> 
>>> 
>>> big_func.__name__
'inner'
>>> big_func.__doc__
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> cube.__name__
'cube'
>>> cube.__doc__
'Wrapper around somefunction() to instrument time and arguments'
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> cube.__name__
'cube'
>>> cube.__doc__
'Return a value times itself thrice'
>>> y = cube(5)
INFO:root:Called cube() with (5,) giving 125 in 0.000003 seconds
>>> y
125
>>> help(cube)
Help on function cube in module __main__:

cube(*args)
    Return a value times itself thrice

>>> 
>>> from dis import dis
>>> dis(cube)
 71           0 LOAD_GLOBAL              0 (time)
              3 LOAD_ATTR                0 (time)
              6 CALL_FUNCTION            0
              9 STORE_FAST               1 (start)

 72          12 LOAD_DEREF               0 (orig_func)
             15 LOAD_FAST                0 (args)
             18 CALL_FUNCTION_VAR        0
             21 STORE_FAST               2 (answer)

 73          24 LOAD_GLOBAL              0 (time)
             27 LOAD_ATTR                0 (time)
             30 CALL_FUNCTION            0
             33 STORE_FAST               3 (end)

 74          36 LOAD_GLOBAL              1 (logging)
             39 LOAD_ATTR                2 (info)
             42 LOAD_CONST               1 ('Called %s() with %s giving %s in %f seconds')

 75          45 LOAD_DEREF               0 (orig_func)
             48 LOAD_ATTR                3 (__name__)
             51 LOAD_FAST                0 (args)
             54 LOAD_FAST                2 (answer)
             57 LOAD_FAST                3 (end)
             60 LOAD_FAST                1 (start)
             63 BINARY_SUBTRACT     
             64 CALL_FUNCTION            5
             67 POP_TOP             

 76          68 LOAD_FAST                2 (answer)
             71 RETURN_VALUE        
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> 
>>> 
>>> 
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> cube.__name__
'inner'
>>> cube.__doc__
>>> from dis import dis
>>> dis(cube)
 84           0 LOAD_FAST                0 (x)
              3 LOAD_DEREF               0 (cache)
              6 COMPARE_OP               6 (in)
              9 POP_JUMP_IF_FALSE       20

 85          12 LOAD_DEREF               0 (cache)
             15 LOAD_FAST                0 (x)
             18 BINARY_SUBSCR       
             19 RETURN_VALUE        

 86     >>   20 LOAD_DEREF               1 (orig_func)
             23 LOAD_FAST                0 (x)
             26 CALL_FUNCTION            1
             29 STORE_FAST               1 (answer)

 87          32 LOAD_FAST                1 (answer)
             35 LOAD_DEREF               0 (cache)
             38 LOAD_FAST                0 (x)
             41 STORE_SUBSCR        

 88          42 LOAD_FAST                1 (answer)
             45 RETURN_VALUE        
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> help(cube)
Help on function cube in module __main__:

cube(x)
    Return a value times itself thrice

>>> cube.__closure__
(<cell at 0x1082177c0: dict object at 0x1081f04b0>, <cell at 0x1082177f8: function object at 0x108213050>)
>>> cube.__closure__[1]
<cell at 0x1082177f8: function object at 0x108213050>
>>> cube.__closure__[1].cell_contents
<function cube at 0x108213050>
>>> cube.__closure__[1].cell_contents.__closure__
(<cell at 0x108217050: function object at 0x10820fc80>,)
>>> cube.__closure__[1].cell_contents.__closure__[0]
<cell at 0x108217050: function object at 0x10820fc80>
>>> cube.__closure__[1].cell_contents.__closure__[0].cell_contents
<function cube at 0x10820fc80>
>>> 
>>> # Jason Bourne   JB   -> Spy
>>> # Jack Bauer     JB   -> Spy
>>> # James Bond     JB   -> Spy
>>> # Justin Bieber  JB
>>> 
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> help(cube)
Help on function cube in module __main__:

cube(x)
    Return a value times itself thrice

>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> x = 10
>>> y = square(10)
INFO:root:Called square() with (10,) giving 100 in 0.000004 seconds
>>> y = square(20)
INFO:root:Called square() with (20,) giving 400 in 0.000002 seconds
>>> show_cache(square)
<function square at 0x1073bb1b8>
>>> y = big_func(10)
Doing hard work
INFO:root:Called big_func() with (10,) giving 11 in 1.074376 seconds
>>> y = big_func(20)
Doing hard work
INFO:root:Called big_func() with (20,) giving 21 in 1.100503 seconds
>>> show_cache(big_func)
{10: 11, 20: 21}
>>> 
====== RESTART: /Users/raymond/Dropbox/Public/army2/decorator_school.py ======
>>> 
>>> y = big_func(10)
Doing hard work
INFO:root:Called big_func() with (10,) giving 11 in 1.074376 seconds
>>> y = big_func(20)
Doing hard work
INFO:root:Called big_func() with (20,) giving 21 in 1.100503 seconds
>>> show_cache(big_func)
{10: 11, 20: 21}
SyntaxError: invalid syntax
>>> 

>>> 
>>> from reverend.thomas import Bayes
>>> gender = Bayes()
>>> gender.train('male', 'bill hank chris mark martin pat adam hank chris zack sean')
>>> gender.train('female', 'mindy shelly pat mary daisy amber chris pat becky sue')
>>> gender.guess('hank')
[('male', 0.9999)]
>>> gender.guess('mindy')
[('female', 0.9999)]
>>> gender.guess('pat')
[('female', 0.6451612903225806), ('male', 0.35483870967741926)]
>>> gender.guess('chris')
[('male', 0.6875000000000001), ('female', 0.3125)]
>>> gender.train('male', 'red red orange yellow red orange blue black brown blue red yellow')
>>> gender.train('female', 'pink red green green blue blue chartreuse green blue yellow orange blue green')
>>> gender.guess('red')
[('male', 0.8), ('female', 0.19999999999999996)]
>>> gender.guess('pink')
[('female', 0.9999)]
>>> gender.guess('green')
[('female', 0.9999)]
>>> gender.guess('yellow')
[('male', 0.6666666666666666), ('female', 0.33333333333333326)]
>>> gender.guess('yellow chris')
[('male', 0.6666666666666666), ('female', 0.33333333333333326)]
>>> gender.guess('yellow pat')
[('male', 0.49999999999999994), ('female', 0.49999999999999994)]
>>> gender.train('male', 'game mat us game mat glad aloto game aloto mat glad')
>>> gender.train('female', 'glad mat fgt dmd pnp mat aloto aloto gladfgt dmd')
>>> gender.guess('yellow chris aloto')
[('male', 0.6732673267326732), ('female', 0.3267326732673267)]
>>> gender.guess('yellow chris glad')
[('male', 0.6732673267326732), ('female', 0.3267326732673267)]
>>> gender.guess('yellow chris game')
[('male', 0.8083591400206317), ('female', 0.3267326732673267)]
>>> 
>>> 
