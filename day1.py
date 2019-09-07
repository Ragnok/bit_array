Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 03:03:55) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> {'raymond': 'red', 'rachel': 'blue', 'matthew': 'green'}
{'raymond': 'red', 'rachel': 'blue', 'matthew': 'green'}
>>> 
=============================== RESTART: Shell ===============================
>>> {'raymond': 'red', 'rachel': 'blue', 'matthew': 'green'}
{'raymond': 'red', 'rachel': 'blue', 'matthew': 'green'}
>>> 
=============================== RESTART: Shell ===============================
>>> {'raymond': 'red', 'rachel': 'blue', 'matthew': 'green'}
{'raymond': 'red', 'rachel': 'blue', 'matthew': 'green'}
>>> hash('raymond')
3594020881237891007
>>> hash('raymond')
3594020881237891007
>>> hash('raymond')
3594020881237891007
>>> 
=============================== RESTART: Shell ===============================
>>> hash('raymond')
-9147000320847335250
>>> hash('raymond')
-9147000320847335250
>>> hash('raymond')
-9147000320847335250
>>> 
>>> # dunder methods
>>> 30 + 40
70
>>> #  ^------ EVP
>>> # ^---^--- Employees
>>> 
>>> #  +   -->  __add__
>>> #                       underscore underscore add underscore underscore
>>> #                       underscore underscore add
>>> #                       under under add
>>> #                       doubleunder
>>> #                       dunder
>>> 
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> 30 + 40
70
>>> (30).__add__(40)
70
>>> type(30)
<class 'int'>
>>> type(30).__add__
<slot wrapper '__add__' of 'int' objects>
>>> type(30).__add__(30, 40)
70
>>> 
>>> s = 'hello'
>>> s + ' world'
'hello world'
>>> type(s)
<class 'str'>
>>> #    ^-- "stir"
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> type(s).__add__(s, ' world')
'hello world'
>>> 
>>> def f(a, b):
	return a + b

>>> f(10, 20, 30)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    f(10, 20, 30)
TypeError: f() takes 2 positional arguments but 3 were given
>>> f(10)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    f(10)
TypeError: f() missing 1 required positional argument: 'b'
>>> f(10, 20)
30
>>> f('hello', ' world')
'hello world'
>>> f(None, {'hello': 'world'})
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    f(None, {'hello': 'world'})
  File "<pyshell#39>", line 2, in f
    return a + b
TypeError: unsupported operand type(s) for +: 'NoneType' and 'dict'
>>> 
>>> 
>>> f(10, 20)
30
>>> f('hello', ' world')
'hello world'
>>> f(10, 'world')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    f(10, 'world')
  File "<pyshell#39>", line 2, in f
    return a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
>>> 
>>> issubclass(KeyError, LookupError)
True
>>> issubclass(LookupError, Exception)
True
>>> lyrics = dict(britney = 'Oops, I did it again. I played your heart')
>>> 
>>> try:
	lirics['katy']
except Exception:
	print('You change your mind like a girl changes clothes')

	
You change your mind like a girl changes clothes
>>> try:
	lirics['britney']
except Exception:
	print('You change your mind like a girl changes clothes')

	
You change your mind like a girl changes clothes
>>> try:
	lirics['britney']
except KeyError:
	print('You change your mind like a girl changes clothes')

	
Traceback (most recent call last):
  File "<pyshell#64>", line 2, in <module>
    lirics['britney']
NameError: name 'lirics' is not defined
>>> try:
	lyrics['britney']
except KeyError:
	print('You change your mind like a girl changes clothes')

	
'Oops, I did it again. I played your heart'
>>> 
>>> 
>>> a = 10
>>> b = 2.5
>>> a + b
12.5
>>> type(a)
<class 'int'>
>>> type(a).__add__(a, b)
NotImplemented
>>> type(b).__radd__(b, a)
12.5
>>> 
>>> b = 'hello'
>>> a + b
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a + b
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> type(a).__add__(a, b)
NotImplemented
>>> type(b).__radd__(b, a)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    type(b).__radd__(b, a)
AttributeError: type object 'str' has no attribute '__radd__'
>>> 
>>> 
>>> # a + b    -->  a.__add__(b)
>>> #                     \-> answer
>>> # NotImplementsed --> b.__radd__(a)
>>> #                     \-> answer
>>> # TypeError
>>> 
>>> # "2" + 4 -> 6
>>> 
>>> 
>>> 
>>> 
>>> a = [10, 20, 30]
>>> b = [40, 50]
>>> a + b
[10, 20, 30, 40, 50]
>>> type(a).__add__(a, b)
[10, 20, 30, 40, 50]
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> import numpy
>>> a = numpy.array([10, 20, 30])
>>> b = numpy.array([40, 50, 60])
>>> a + b
array([50, 70, 90])
>>> f(a, b)
array([50, 70, 90])
>>> 
>>> 
>>> # http://bit.ly/python-ar2
>>> dir(int)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>> cmpcnt = 25
>>> 'There are {cmpcnt} compares'.format(cmpcnt=cmpcnt)
'There are 25 compares'
>>> f'There are {cmpcnt} compares'
'There are 25 compares'
>>> print( F'Yes!' )
Yes!
>>> 

>>> 
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018, 20:59:26) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> hettingers = {'raymond': 'red'}
>>> len(hettingers)
1
>>> hettingers
{'raymond': 'red'}
>>> hettingers = {'raymond': 'red', 'rachel': 'blue'}
>>> hettingers
{'rachel': 'blue', 'raymond': 'red'}
>>> 
>>> hettingers = {'raymond': 'red'}
>>> hettingers['rachel'] = 'blue'
>>> hettingers
{'rachel': 'blue', 'raymond': 'red'}
>>> abs(hash('raymond'))
2729357497184525765
>>> abs(hash('rachel'))
9091735575445484789
>>> abs(hash('raymond')) % 5
0
>>> abs(hash('raymond')) % 8
5
>>> abs(hash('rachel')) % 8
5
>>> # DINKs
>>> hettingers = {'raymond': 'red', 'rachel': 'blue', 'matthew': 'green'}
>>> hettingers
{'matthew': 'green', 'rachel': 'blue', 'raymond': 'red'}
>>> abs(hash('matthew'))
3244245660916063665
>>> abs(hash('matthew')) % 8
1
>>> hettingers = {'raymond': 'red'}
>>> hettingers['rachel'] = 'blue';   hettingers
{'rachel': 'blue', 'raymond': 'red'}
>>> hettingers['matthew'] = 'yellow';   hettingers
{'matthew': 'yellow', 'rachel': 'blue', 'raymond': 'red'}
>>> hettingers['susan'] = 'black';   hettingers
{'matthew': 'yellow', 'rachel': 'blue', 'raymond': 'red', 'susan': 'black'}
>>> hettingers['mary'] = 'orange';   hettingers
{'matthew': 'yellow', 'mary': 'orange', 'rachel': 'blue', 'raymond': 'red', 'susan': 'black'}
>>> hettingers['daisy'] = 'indigo';   hettingers
{'raymond': 'red', 'susan': 'black', 'rachel': 'blue', 'matthew': 'yellow', 'daisy': 'indigo', 'mary': 'orange'}
>>> abs(hash('raymond')) % 32
5
>>> abs(hash('rachel')) % 32
21
>>> {'raymond': 'red', 'rachel': 'blue', 'matthew': 'green'}
{'matthew': 'green', 'rachel': 'blue', 'raymond': 'red'}
>>> 
>>> 
>>> 
>>> dir(int)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
>>> 10 < 15
True
>>> (10).__cmp__(15)      # -1 0 1
-1
>>> (10).__cmp__(15) == -1
True
>>> (10).__cmp__(10)      # -1 0 1
0
>>> (10).__cmp__(5)      # -1 0 1
1
>>> 
>>> 'goodbye' < 'hello'
True
>>> 'goodbye'.__lt__('hello')
True
>>> 
>>> # __cmp__
>>> # __lt__ __le__ __eq__ __ne__ __gt__ __ge__
>>> import numpy as np
>>> np.array([10, 4, 20]) < np.array([5,7,12])
array([False,  True, False])
>>> 
Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 29 2018, 20:59:26) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 

>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> cmpcnt = 5
>>> reset()
>>> cmpcnt
5
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> cmpcnt = 5
>>> reset()
>>> cmpcnt
0
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> show()
There are 0 compares
>>> 
>>> 
>>> print 'The answer is %d today' % 10
The answer is 10 today
>>> print 'The answer is %d today' % 2**5
The answer is 32 today
>>> print 'The answer is %d today' % 2*5
The answer is 2 todayThe answer is 2 todayThe answer is 2 todayThe answer is 2 todayThe answer is 2 today
>>> print 'The answer is %d today' % (2*5)
The answer is 10 today
>>> print 'The answer is %d today but was %d yesterday' % (10, 20)
The answer is 10 today but was 20 yesterday
>>> print 'The answer is %(new)d today but was %(old)d yesterday' % dict(old=20, new=10)
The answer is 10 today but was 20 yesterday
>>> print 'The answer is {new} today but was {old} yesterday'.format(old=20, new=10)
The answer is 10 today but was 20 yesterday
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> show()
There are 0 compares
>>> 
>>> x = 10
>>> ++x
10
>>> x
10
>>> ++x
10
>>> x
10
>>> x = 10
>>> - x
-10
>>> - - x
10
>>> --x
10
>>> --x
10
>>> x++
SyntaxError: invalid syntax
>>> 
>>> # *(p++) *= *(q--) + *(p++);
>>> 
>>> 
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> 
>>> class A(object): pass

>>> class B(A): pass

>>> class C(A): pass

>>> class D(B, C): pass

>>> # D<B    D<C   C<A   B<A   A<object
>>> # B<C
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
>>> 
>>> D.__mro__
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
>>> #                            o----------------------^
>>> # super -> next in the MRO
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> Int(5) < Int(10)
Comparing 5 to 10

Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    Int(5) < Int(10)
  File "/Users/raymond/Dropbox/Public/army2/instrument.py", line 34, in __cmp__
    return super()
TypeError: super() takes at least 1 argument (0 given)
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> Int(5) < Int(10)
Comparing 5 to 10
True
>>> show()
There are 1 compares
>>> Int(15) < Int(10)
Comparing 15 to 10
False
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
>>> len(s)
8
>>> type(s)
<type 'list'>
>>> map(type, s)
[<class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>]
>>> set(map(type, s))
set([<class '__main__.Int'>])
>>> len(set(map(type, s)))
1
>>> 
>>> map(type, s) # SELECT TYPE(element) FROM S;
[<class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>, <class '__main__.Int'>]
>>> set(map(type, s)) # SELECT DISTINCT TYPE(element) FROM S;
set([<class '__main__.Int'>])
>>> 
>>> 
>>> names = ['luke', 'leia', 'han']
>>> names[0]
'luke'
>>> # -1
>>> # -1]
>>> 
>>> names[ 2 -1]
'leia'
>>> names[ 1 -1]
'luke'
>>> names[ 3 -1]
'han'
>>> names[ 3 - 1 ]
'han'
>>> 
>>> x = 10; print x**2
100
>>> s
[10, 20, 30, 40, 5, 10, 15, 20]
>>> 30 in s
Comparing 10 to 30
Comparing 20 to 30
Comparing 30 to 30
True
>>> 
>>> 
>>> s.__contains__(30)
Comparing 10 to 30
Comparing 20 to 30
Comparing 30 to 30
True
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
>>> len(s)
8
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
>>> # O(1)  O(n)  O(n**2)  O(n log n)
>>> from math import *
>>> def ss(n):
	return n * log(n, 2)

>>> ss(100)
664.3856189774725
>>> ss(1000)
9965.784284662088
>>> ss(10000)
132877.1237954945
>>> ss(100000)
1660964.0474436812
>>> ss(1000000)
19931568.569324173
>>> log(1000, 2)
9.965784284662087
>>> log(1000000, 2)
19.931568569324174
>>> log(1000000000, 2)
29.897352853986263
>>> 
>>> # merge shell bubble quick
>>> #                      ^-- O(n log n)   heap quick merge
>>> #                               ^-- best if the data is random
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
>>> 
>>> from bisect import *
>>> cuts = [60, 70, 80, 90]
>>> grades = 'FDCBA'
>>> 
>>> score = 72
>>> bisect(cuts, score)
2
>>> # [-- sect 0 --] 60  [-- sect 1 --] 70 [-- sect 2 --] 80 [-- sect 3 --] 90 [-- sect 4 --]
>>> score = 51
>>> bisect(cuts, score)
0
>>> score = 99
>>> bisect(cuts, score)
4
>>> grades[bisect(cuts, score)]
'A'
>>> grades[bisect(cuts, 70)]
'C'
>>> 
>>> 
>>> from bisect import *
>>> cuts = [60, 70, 80, 90]
>>> grades = 'FDCBA'
>>> grades[bisect(cuts, 85)]
'B'
>>> grades[bisect(cuts, 70)]
'C'
>>> bisect(cuts, 70)
2
>>> bisect_left(cuts, 70)
1
>>> # O(log n)
>>> 2 ** 20
1048576
>>> 
>>> 
>>> [grades[bisect(cuts, score)] for score in (10, 50, 99, 81, 70, 79, 95, 61, 72, 98)]
['F', 'F', 'A', 'B', 'C', 'C', 'A', 'D', 'C', 'A']
>>> table = [grades[bisect(cuts, score)] for score in range(101)]
>>> table
['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'C', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
>>> table[50]
'F'
>>> table[99]
'A'
>>> table[70]
'C'
>>> table = [table[score] for score in range(101)]
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
>>> 2 ** 3
8
>>> len(s)
8
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/instrument.py", line 69, in <module>
    other_data = map(Int, [20, 30, 40, 300, 400, 500, 300]) + data[-4:]
NameError: name 'data' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares

Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/instrument.py", line 69, in <module>
    other_data = map(Int, [20, 30, 40, 300, 400, 500, 300]) + data[-4:]
NameError: name 'data' is not defined
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares
Comparing 300 to 300
Comparing 20 to 20
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares
Comparing 300 to 300
Comparing 20 to 20
==============================
>>> hash('raymond')
2729357497184525765
>>> 'raymond'.__hash__()
2729357497184525765
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Comparing 300 to 300
Comparing 20 to 20
==============================
>>> hash(Int(20))
20
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
>>> hash(Int(20))
Hashing 20
20
>>> show()
There are 0 compares and 1 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 10
Comparing 10 to 10
True
There are 1 compares and 1 hashes
>>> 
>>> map(id, data)
[4582195496, 4582195640, 4582196576, 4582197656, 4582198520, 4582198376, 4582196720, 4582197512]
>>> c
10
>>> id(c)
4582189320
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 30
True
There are 0 compares and 1 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 30
True
There are 0 compares and 1 hashes
==============================
There are 0 compares and 0 hashes
>>> d
{20: None, 5: None, 40: None, 10: None, 30: None, 15: None}
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 30
True
There are 0 compares and 1 hashes
==============================
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 30
True
There are 0 compares and 1 hashes
==============================
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 30
True
There are 0 compares and 1 hashes
==============================
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([5, 40, 10, 15, 20, 30])
There are 4 compares and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 30
True
There are 0 compares and 1 hashes
==============================
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([5, 40, 10, 15, 20, 30])
There are 4 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([5, 40, 10, 300, 15, 400, 20, 500, 30])
There are 4 compares and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 30
True
There are 0 compares and 1 hashes
==============================
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([5, 40, 10, 15, 20, 30])
There are 4 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([5, 40, 10, 300, 15, 400, 20, 500, 30])
There are 4 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([])
There are 4 compares and 0 hashes
>>> 
========= RESTART: /Users/raymond/Dropbox/Public/army2/instrument.py =========
Comparing 11 to 10
Comparing 11 to 20
Comparing 11 to 30
Comparing 11 to 40
Comparing 11 to 5
Comparing 11 to 10
Comparing 11 to 15
Comparing 11 to 20
False
There are 8 compares and 0 hashes
Comparing 20 to 10
Comparing 20 to 20
True
There are 2 compares and 0 hashes
Comparing 30 to 10
Comparing 30 to 20
True
There are 2 compares and 0 hashes
Predicted sort compares 24.0
Comparing 20 to 10
Comparing 30 to 20
Comparing 40 to 30
Comparing 5 to 40
Comparing 5 to 30
Comparing 5 to 20
Comparing 5 to 10
Comparing 10 to 20
Comparing 10 to 10
Comparing 15 to 20
Comparing 15 to 10
Comparing 15 to 10
Comparing 20 to 15
Comparing 20 to 30
Comparing 20 to 20
There are 15 compares and 0 hashes
Predicted bisect compares 3.0
Comparing 11 to 20
Comparing 11 to 10
Comparing 11 to 15
There are 3 compares and 0 hashes
Comparing 20 to 20
Comparing 20 to 30
Comparing 20 to 20
There are 3 compares and 0 hashes
Comparing 30 to 20
Comparing 30 to 30
Comparing 30 to 40
There are 3 compares and 0 hashes
Hashing 20
Hashing 30
Hashing 40
Hashing 300
Hashing 400
Hashing 500
Hashing 300
Comparing 300 to 300
Hashing 5
Hashing 10
Hashing 15
Hashing 20
Comparing 20 to 20
==============================
Hashing 10
Hashing 20
Hashing 30
Hashing 40
Hashing 5
Hashing 10
Comparing 10 to 10
Hashing 15
Hashing 20
Comparing 20 to 20
There are 2 compares and 8 hashes
Hashing 11
False
There are 0 compares and 1 hashes
Hashing 20
Comparing 20 to 20
True
There are 1 compares and 1 hashes
Hashing 30
True
There are 0 compares and 1 hashes
==============================
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
There are 0 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([5, 40, 10, 15, 20, 30])
There are 4 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([5, 40, 10, 300, 15, 400, 20, 500, 30])
There are 4 compares and 0 hashes
Comparing 40 to 40
Comparing 10 to 10
Comparing 20 to 20
Comparing 30 to 30
set([])
There are 4 compares and 0 hashes
>>> 
