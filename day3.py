Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018, 20:59:26) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # http://bit.ly/python-ar2c

>>> b = bytearray(20)
>>> len(b)
20
>>> b[5] = 125
>>> b[0]
0
>>> b[5]
125
>>> list(b)
[0, 0, 0, 0, 0, 125, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> b
bytearray(b'\x00\x00\x00\x00\x00}\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 22, in <module>
    b = BitArray(20)
NameError: name 'BitArray' is not defined
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 27, in <module>
    b = BitArray(20)
TypeError: this constructor takes no arguments
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 31, in <module>
    print len(b)
AttributeError: BitArray instance has no attribute '__len__'
>>> help(len)
Help on built-in function len in module __builtin__:

len(...)
    len(object) -> integer
    
    Return the number of items of a sequence or collection.

>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 32, in <module>
    print len(b)
AttributeError: BitArray instance has no attribute '__len__'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
20

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 35, in <module>
    b[11] = 1
AttributeError: BitArray instance has no attribute '__setitem__'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
20

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 42, in <module>
    b[11] = 1
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 31, in __setitem__
    self.data[bytenum] |= (1 << bitnum)
AttributeError: BitArray instance has no attribute 'data'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 41, in <module>
    b = BitArray(20)
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 24, in __init__
    self.data = bytearray(numbytes)
NameError: global name 'numbytes' is not defined
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 42, in <module>
    b = BitArray(20)
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 24, in __init__
    numbytes = ceiling_division(numbits, 8)
NameError: global name 'ceiling_division' is not defined
>>> [None] * 10
[None, None, None, None, None, None, None, None, None, None]
>>> [0.10] * 10
[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
>>> sum([0.10] * 10)
0.9999999999999999
>>> sum([0.10] * 10) == 1.00
False
>>> from math import floor
>>> floor(sum([0.10] * 10))
0.0
>>> 
>>> 
>>> 4 / 3   +   7 / 3   +   1 / 3
3
>>> 4 / 3
1
>>> 7 / 3
2
>>> 1 / 3
0
>>> 4.0 / 3   +   7.0 / 3   +   1.0 / 3
4.0
>>> sum([1.0 / 10.0] * 10))
SyntaxError: invalid syntax
>>> sum([1.0 / 10.0] * 10)
0.9999999999999999
>>> from fractions import Fraction
>>> Fraction(4, 3) + Fraction(1, 2) - Fraction(1, 6)
Fraction(5, 3)
>>> sum([Fraction(1, 10)] * 10))
SyntaxError: invalid syntax
>>> [Fraction(1, 10)]
[Fraction(1, 10)]
>>> [Fraction(1, 10)] * 10
[Fraction(1, 10), Fraction(1, 10), Fraction(1, 10), Fraction(1, 10), Fraction(1, 10), Fraction(1, 10), Fraction(1, 10), Fraction(1, 10), Fraction(1, 10), Fraction(1, 10)]
>>> sum([Fraction(1, 10)] * 10)
Fraction(1, 1)
>>> 
>>> 
>>> from decimal import Decimal
>>> Decimal('1.1') + Decimal('2.2') == Decimal('3.3')
True
>>> 1.1 + 2.2 == 3.3
False
>>> s = 1.1 + 2.2
>>> t = 3.3
>>> s
3.3000000000000003
>>> t
3.3
>>> s
3.3000000000000003
>>> print ('%.4f' % s)
3.3000
>>> s == 3.3
False
>>> 
>>> # floats         -> binary floating points   stored as fraction
>>> #                   numerator is a 53 bit integer
>>> #                   denoninator is a power of two
>>> 
>>> # Decimal        -> decimal floating points   stored as fraction
>>> #                   numerator is an arbitrary precision integer
>>> #                   denoninator is a power of ten
>>> 
>>> # Fraction       -> stored as a fraction
>>> #                   numerator is an arbitrary precision integer
>>> #                   denominator is an arbitrary precision integer
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 42, in <module>
    b = BitArray(20)
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 24, in __init__
    numbytes = ceiling_division(numbits, 8)
NameError: global name 'ceiling_division' is not defined
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
**********************************************************************
File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 25, in __main__.ceiling_division
Failed example:
    ceiling_division(16, 12)
Expected:
    2
Got nothing
**********************************************************************
1 items had failures:
   1 of   1 in __main__.ceiling_division
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1)

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 58, in <module>
    b = BitArray(20)
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 37, in __init__
    self.data = bytearray(numbytes)
TypeError: 'NoneType' object is not iterable
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 62, in <module>
    print list(b)
TypeError: iteration over non-sequence
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
**********************************************************************
File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 25, in __main__.ceiling_division
Failed example:
    ceiling_division(16, 12)
Expected:
    3
Got:
    2
**********************************************************************
1 items had failures:
   1 of   1 in __main__.ceiling_division
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1)
20

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 62, in <module>
    print list(b)
TypeError: iteration over non-sequence
>>> # -i
>>> 
>>> from unicodedata import *
>>> 
=============================== RESTART: Shell ===============================
>>> from unicodedata import *
>>> dir()
['UCD', '__builtins__', '__doc__', '__name__', '__package__', 'bidirectional', 'category', 'combining', 'decimal', 'decomposition', 'digit', 'east_asian_width', 'lookup', 'mirrored', 'name', 'normalize', 'numeric', 'ucd_3_2_0', 'ucnhash_CAPI', 'unidata_version']
>>> help(name)
Help on built-in function name in module unicodedata:

name(...)
    name(unichr[, default])
    Returns the name assigned to the Unicode character unichr as a
    string. If no name is defined, default is returned, or, if not
    given, ValueError is raised.

>>> name(u'-')
'HYPHEN-MINUS'
>>> print 'TheRaymondWay\u2122'
TheRaymondWay\u2122
>>> print u'TheRaymondWay\u2122'
TheRaymondWay™
>>> print u'TheRaymondWay\N{trade mark sign}'
TheRaymondWay™
>>> print u'\N{snowman}'
☃
>>> print u'\N{snowman}\N{comet}'
☃☄
>>> print u'\N{snowman}\N{umbrella}\N{comet}'
☃☂☄
>>> print u'The answer is \u0664\u0662 today'
The answer is ٤٢ today
>>> 
>>> 
>>> print u'x + y = z \N{right tack} z = x + y'
x + y = z ⊢ z = x + y
>>> 
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 63, in <module>
    print list(b)
TypeError: iteration over non-sequence
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 63, in <module>
    print b[11]
AttributeError: BitArray instance has no attribute '__getitem__'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
<__main__.BitArray instance at 0x10549f098>
>>> # All sequences are iterable!
>>> # A sequence is any object that defines __getitem__ and __len__
>>> # such that s[0], s[1], .... s[len(s) - 1]
>>> 
>>> s = 'hello'
>>> dir()
['BitArray', '__builtins__', '__doc__', '__file__', '__name__', '__package__', 'b', 'ceiling_division', 'doctest', 's']
>>> dir(s)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 
>>> len(s)
5
>>> s[0]
'h'
>>> s[1]
'e'
>>> for c in s:
	print c

	
h
e
l
l
o
>>> 
>>> 
>>> list(b)
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
<__main__.BitArray instance at 0x10f1bf290>
>>> 
>>> 
>>> # There are two ways to look at an object:
>>> # __str__ is called by "print" for display to an end-user, so the output needs to be pretty
>>> # __repr__ is called by ">>> " or %r or !r for a programmer, so the output needs to be informative
>>> 
>>> s = u'lim x \N{long rightwards arrow} \N{infinity}, 1 / sin\N{superscript two}(x)'
>>> print s
lim x ⟶ ∞, 1 / sin²(x)
>>> s
u'lim x \u27f6 \u221e, 1 / sin\xb2(x)'
>>> 
>>> 
>>> 30 + 40
70
>>> print 30 + 40
70
>>> '7' + '0'
'70'
>>> print '7' + '0'
70
>>> (30 + 40) * 5
350
>>> ('7' + '0') * 5
'7070707070'
>>> set([3+5, 4+7, 2+9])
set([8, 11])
>>> set([8, 11])
set([8, 11])
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray(20)
>>> 
>>> 
>>> b
BitArray(20)
>>> BitArray(50)
BitArray(50)
>>> list('abc')
['a', 'b', 'c']
>>> 
>>> 
>>> x = 1
>>> type(x)
<type 'int'>
>>> str(x)
'1'
>>> map(type, b)
[<type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>, <type 'int'>]
>>> list(b)
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> map(str, b)
['0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
>>> ''.join(map(str, b))
'000001100001000000000000'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray(000001100001000000000000)
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray(000001100001000000000000)
>>> s = "000001100001000000000000"
>>> print s
000001100001000000000000
>>> s
'000001100001000000000000'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('000001100001000000000000')
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> 
>>> BitArray(100)
BitArray('00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> [b[i] for i in range(size)]

Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    [b[i] for i in range(size)]
NameError: name 'size' is not defined
>>> [b[i] for i in range(10)]
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0]
>>> [str(b[i]) for i in range(10)]
['0', '0', '0', '0', '0', '1', '1', '0', '0', '0']
>>> ''.join([str(b[i]) for i in range(10)])
'0000011000'
>>> BitArray(30)
BitArray('000000000000000000000000000000')
>>> BitArray(31)
BitArray('000000000000000000000000000000')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> BitArray(50)
BitArray('000000000000000000000000000000 ...')
>>> BitArray(100000)
BitArray('000000000000000000000000000000 ...')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> open('notes/hamlet.txt')
<open file 'notes/hamlet.txt', mode 'r' at 0x10a713810>
>>> open('notes/hamletasd.txt')

Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    open('notes/hamletasd.txt')
IOError: [Errno 2] No such file or directory: 'notes/hamletasd.txt'
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/army2/params.py ===========
>>> f(hotwire=10, backup=None, runlive=True)
runlive --> True
hotwire --> 10
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/army2/params.py ===========
>>> g(hotwire=10, runlive=True)
hotwire --> 10
runlive --> True
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/army2/params.py ===========
>>> 
=========== RESTART: /Users/raymond/Dropbox/Public/army2/params.py ===========
>>> g(hotwire=10, runlive=True)
{'rl': True, 'hw': 10}
>>> b = bytearray(20)
>>> b[18] = 1
>>> b[18]
1
>>> b[-2]
1
>>> b[-2 + len(b)]
1
>>> s = 'cyber.army.mil'
>>> s[-3]
'm'
>>> s[-3:]
'mil'
>>> s = 'python.cyber.army.mil'
>>> s[-3:]
'mil'
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> b[11]
1
>>> b[-9]
1
>>> b[12]
0
>>> b[-8]
0
>>> b = bytearray(20)
>>> b[50]

Traceback (most recent call last):
  File "<pyshell#161>", line 1, in <module>
    b[50]
IndexError: bytearray index out of range
>>> b[-5]
0
>>> b[-50]

Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    b[-50]
IndexError: bytearray index out of range
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> # binary digit
>>> #  xxxxxxxxx
>>> # b         it
>>> # byte   8 bits
>>> # nibble 4 bits
>>> # octets
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> b[-2]
0
>>> b[-50]

Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    b[-50]
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 47, in __getitem__
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> b[50]

Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    b[50]
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 47, in __getitem__
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> b[2] = 1
>>> b[50] = 1

Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    b[50] = 1
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 55, in __setitem__
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> b[-50] = 1

Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    b[-50] = 1
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 55, in __setitem__
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> b[-2] = 1
>>> b[-2]
1
>>> b = bytearray(20)
>>> b[2] = None

Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    b[2] = None
TypeError: an integer or string of size 1 is required
>>> b[2] = 1000

Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    b[2] = 1000
ValueError: byte must be in range(0, 256)
>>> b[200] = 1000

Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    b[200] = 1000
IndexError: bytearray index out of range
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> 
>>> 
>>> 
>>> 
>>> 
>>> b[-3] = 1
>>> b[-3]
1
>>> b[17]
1
>>> b[-100]

Traceback (most recent call last):
  File "<pyshell#190>", line 1, in <module>
    b[-100]
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 47, in __getitem__
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> b[21]

Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    b[21]
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 47, in __getitem__
    raise IndexError('bitarray index out of range')
IndexError: bitarray index out of range
>>> b[5] = None

Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    b[5] = None
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 57, in __setitem__
    raise TypeError('an integer of size 1 is required')
TypeError: an integer of size 1 is required
>>> b[5] = 10

Traceback (most recent call last):
  File "<pyshell#193>", line 1, in <module>
    b[5] = 10
  File "/Users/raymond/Dropbox/Public/army2/bitarray.py", line 59, in __setitem__
    raise ValueError('bit must be a 0 or 1')
ValueError: bit must be a 0 or 1
>>> 
>>> import math
>>> math.sqrt(36)
6.0
>>> math.sqrt('hello')

Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    math.sqrt('hello')
TypeError: a float is required
>>> math.sqrt(-36)

Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    math.sqrt(-36)
ValueError: math domain error
>>> # ~/ar
>>> # /Users/raymond/ar
>>> 
>>> 
>>> # D.R.Y. -- Do not repeat yourself!
>>> # is kind of "Code smell"
>>> # this particular smell indicates
>>> # a need to "refactor".
>>> 
>>> # D.R.Y. -- Do not repeat yourself!
>>> # There should be a single source of truth
>>> # All essential ideas should be
>>> #   expressed exactly once in the code.
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> 
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> 
========== RESTART: /Users/raymond/Dropbox/Public/army2/bitarray.py ==========
TestResults(failed=0, attempted=1)
20
1
0
1
1
0
[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]
BitArray('00000110000100000000')
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/bloomfilter.py ========
False
True
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
TestResults(failed=0, attempted=3)
Misspelled
----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
don't
leight
>>> 4000000 / 8
500000
>>> # 18Mb -> 0.5Mb
>>> # 36x
>>> 
>>> # 9Mb -> 0.25Mb
>>> # 250kb  L2 cache  40x
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
TestResults(failed=0, attempted=3)
Misspelled
----------
iss
tymme
guhd
ood

======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
TestResults(failed=0, attempted=3)

=============================== RESTART: Shell ===============================
>>> import time
>>> time.time()
1526484759.242394
>>> time.ctime()
'Wed May 16 11:32:43 2018'
>>> 
>>> 
>>> time.sleep(5); print 'Done'
Done
>>> start = time.time()
>>> end = time.time()
>>> end - start
4.5801098346710205
>>> 
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
TestResults(failed=0, attempted=3)
8.54858994484
Misspelled
----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
don't
leight
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
8.74886798859
Misspelled
----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
don't
leight
0.616056919098
>>> 
>>> 
>>> import pickle
>>> hansolo = dict(
	ship = 'milleneum falcon',
	friends = ['luke', 'leia', 'chewy'],
	rank = 'CAPT',
	status = 'wanted by Jabba the Hutt',
)
>>> len(hansolo)
4
>>> hansolo['rank']
'CAPT'
>>> 
>>> for friend in hansolo['friends']:
	print "Don't worry Han, %s will save you" % friend.capitalize()

	
Don't worry Han, Luke will save you
Don't worry Han, Leia will save you
Don't worry Han, Chewy will save you
>>> type(hansolo)
<type 'dict'>
>>> carbonite = pickle.dumps(hansolo)
>>> del hansolo
>>> type(carbonite)
<type 'str'>
>>> len(carbonite)
168
>>> for friend in hansolo['friends']:
	print "Don't worry Han, %s will save you" % friend.capitalize()

	

Traceback (most recent call last):
  File "<pyshell#251>", line 1, in <module>
    for friend in hansolo['friends']:
NameError: name 'hansolo' is not defined
>>> 
>>> hansolo = pickle.loads(carbonite)
>>> type(hansolo)
<type 'dict'>
>>> 
>>> for friend in hansolo['friends']:
	print "Don't worry Han, %s will save you" % friend.capitalize()

	
Don't worry Han, Luke will save you
Don't worry Han, Leia will save you
Don't worry Han, Chewy will save you
>>> carbonite
"(dp0\nS'status'\np1\nS'wanted by Jabba the Hutt'\np2\nsS'ship'\np3\nS'milleneum falcon'\np4\nsS'friends'\np5\n(lp6\nS'luke'\np7\naS'leia'\np8\naS'chewy'\np9\nasS'rank'\np10\nS'CAPT'\np11\ns."
>>> 
>>> 
>>> 
>>> help(pickle.dump)
Help on function dump in module pickle:

dump(obj, file, protocol=None)

>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
8.5331568718
Misspelled
----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
don't
leight
0.601397037506
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
0.00594282150269
Misspelled
----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
don't
leight
0.600029945374
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/spell_check.py", line 84, in <module>
    correct_words = make_checker()
  File "/Users/raymond/Dropbox/Public/army2/spell_check.py", line 27, in make_checker
    with open('words.pickle') as cache_file:
IOError: [Errno 2] No such file or directory: 'words.pickle'
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
8.23147106171
Misspelled
----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
don't
leight
0.426192998886
>>> 8.7 / 0.0047
1851.0638297872338
>>> 1851.0638297872338
1851.0638297872338
>>> # GIGO <-- Garbage In / Garbage Out
>>> #                         ^-- Gourmet Out
>>> 
======== RESTART: /Users/raymond/Dropbox/Public/army2/spell_check.py ========
TestResults(failed=0, attempted=3)
0.0051281452179
Misspelled
----------
iss
tymme
guhd
ood
tooo
comee
ayd
thur
don't
leight
0.599986076355
>>> # $ python -i threading_demo.py
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 5
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
The count is 9
--------------
The count is 10
--------------
Finished!
>>> 
>>> counter
10
>>> i
9
>>> range(10)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 5
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
The count is 9
--------------
The count is 10
--------------
Finished!
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count isThe count isThe count isThe count isThe count isThe count isThe count isThe count isThe count isFinished!The count is         
 101010101010101010
>>> 10









--------------------------------------------------------------------------------------------------------------------------------------------










>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count isThe count isThe count isThe count isThe count isThe count isThe count isThe count isThe count isThe count isFinished!          
10101010101010101010
>>> 









--------------------------------------------------------------------------------------------------------------------------------------------










======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/threading_demo.py", line 77, in <module>
    t = thread(target=counter_manager)
NameError: name 'thread' is not defined
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/threading_demo.py", line 77, in <module>
    t = threading(target=counter_manager)
TypeError: 'module' object is not callable
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count isThe count isThe count isThe count isThe count isThe count isThe count isThe count isThe count isThe count isFinished!          
10101010101010101010
>>> 









--------------------------------------------------------------------------------------------------------------------------------------------










======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
>>> Exception in thread Thread-2:
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 801, in __bootstrap_inner
    self.run()
  File "/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/threading.py", line 754, in run
    self.__target(*self.__args, **self.__kwargs)
AttributeError: Queue instance has no __call__ method


======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
>>> 
The count is 0
--------------
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 4
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
Finished!
The count is 9
--------------

======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 0
--------------
The count is 0
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
>>> 
The count is 5
--------------
The count is 5
--------------
The count is 7
--------------
The count is 8
--------------
Finished!
The count is 9
--------------

======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 0
--------------
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 6
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
Finished!
The count is 9
--------------
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 0
--------------
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 5
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
Finished!
The count is 9
--------------
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 0
--------------
The count is 1
--------------
The count is 2
--------------
The count is 2
--------------
The count is 4
--------------
The count is 5
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
The count is 9
--------------
Finished!
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 0
--------------
The count is 0
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 5
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
Finished!
The count is 9
--------------
>>> fuzz()
>>> fuzz()
>>> fuzz()
>>> 
=== RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo_fuzzing.py ===
Starting up
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 5
--------------
The count is 6
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
The count is 9
--------------
Finished!
The count is 10
--------------
>>> 
=== RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo_fuzzing.py ===
Starting up
The count is 1
--------------
The count is 3
--------------
The count is 3
--------------
The count is 6
--------------
The count is 6
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
The count is 9
--------------
Finished!
The count is 10
--------------
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 5
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
The count is 9
--------------
Finished!
The count is 10
--------------
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 5
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
The count is 9
--------------
Finished!
The count is 10
--------------
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/threading_demo.py =======
Starting up
The count is 1
--------------
The count is 2
--------------
The count is 3
--------------
The count is 4
--------------
The count is 5
--------------
The count is 6
--------------
The count is 7
--------------
The count is 8
--------------
The count is 9
--------------
The count is 10
--------------
Finished!
>>> 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
[19, 10, 32, 37]
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
Computing the length of 'happy days'
Computing the length of 'come to the aid of their country'
Computing the length of 'she sells sea shells by the sea shore'
[19, 10, 32, 37]
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
Computing the length of 'happy days'
Computing the length of 'come to the aid of their country'
Computing the length of 'she sells sea shells by the sea shore'
19
10
32
37
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
Computing the length of 'happy days'
Computing the length of 'come to the aid of their country'
Computing the length of 'she sells sea shells by the sea shore'
19
10
32
37
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
19
10
32
37
>>> "It hangs!"
'It hangs!'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
the quick brown fox
happy days
come to the aid of their country
she sells sea shells by the sea shore
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
Computing the length of 'happy days'
Computing the length of 'come to the aid of their country'
Computing the length of 'she sells sea shells by the sea shore'
the quick brown fox
happy days
come to the aid of their country
she sells sea shells by the sea shore
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
Computing the length of 'happy days'
Computing the length of 'come to the aid of their country'
Computing the length of 'she sells sea shells by the sea shore'
19
10
32
37
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
19
Computing the length of 'happy days'
10
Computing the length of 'come to the aid of their country'
32
Computing the length of 'she sells sea shells by the sea shore'
37
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
19
10
32
37
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
19 <-- the quick 
10 <-- happy days
32 <-- come to th
37 <-- she sells 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
Computing the length of 'happy days'
Computing the length of 'come to the aid of their country'
Computing the length of 'she sells sea shells by the sea shore'
19 <-- the quick 
10 <-- happy days
32 <-- come to th
37 <-- she sells 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
19 <-- the quick 
Computing the length of 'happy days'
10 <-- happy days
Computing the length of 'come to the aid of their country'
32 <-- come to th
Computing the length of 'she sells sea shells by the sea shore'
37 <-- she sells 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
19 <-- the quick 
Computing the length of 'happy days'
10 <-- happy days
Computing the length of 'come to the aid of their country'
32 <-- come to th
Computing the length of 'she sells sea shells by the sea shore'
37 <-- she sells 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
19 <-- the quick 
Computing the length of 'come to the aid of their country'
32 <-- happy days
Computing the length of 'happy days'
10 <-- come to th
Computing the length of 'she sells sea shells by the sea shore'
37 <-- she sells 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
Computing the length of 'the quick brown fox'
19 <-- the quick 
Computing the length of 'come to the aid of their country'
32 <-- come to th
Computing the length of 'she sells sea shells by the sea shore'
37 <-- she sells 
Computing the length of 'happy days'
10 <-- happy days
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
37 <-- she sells 
19 <-- the quick 
10 <-- happy days
32 <-- come to th
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/how_map_works.py =======
SyntaxError: invalid syntax
>>> 
>>> 

>>> 
>>> 
