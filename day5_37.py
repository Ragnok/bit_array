Python 3.7.0b4 (v3.7.0b4:eb96c37699, May  2 2018, 04:13:13) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> # python3.7 --version          --> 3.7.0b4
>>> 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
>>> c
(33, 1.0, 0.5)
>>> x, y, z = c
>>> c[0]
33
>>> c[:2]
(33, 1.0)
>>> {c}
{(33, 1.0, 0.5)}
>>> type(c)
<class 'tuple'>
>>> c
(33, 1.0, 0.5)
>>> (c[0] * 1.2,) + c[1:]
(39.6, 1.0, 0.5)
>>> 
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
>>> x, y, z = c
>>> c[0]
33
>>> c[:2]
(33, 1.0)
>>> (c[0] * 1.2,) + c[1:]
(39.6, 1.0, 0.5)
>>> {c}
{Color(hue=33, saturation=1.0, lightness=0.5)}
>>> 
>>> 
>>> c
Color(hue=33, saturation=1.0, lightness=0.5)
>>> c[0]
33
>>> c.saturation
1.0
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is {c.saturation}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
>>> print(  F"Yes!" )
Yes!
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=33, saturation=1.0, lightness=0.5)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
>>> c.__annotations__
OrderedDict([('hue', <class 'int'>), ('saturation', <class 'float'>), ('lightness', <class 'float'>)])
>>> c.saturation = 45
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    c.saturation = 45
AttributeError: can't set attribute
>>> list(c)
[33, 1.0, 0.5]
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
>>> x, y, z = c
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x, y, z = c
TypeError: cannot unpack non-iterable Color object
>>> hash(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    hash(c)
TypeError: unhashable type: 'Color'
>>> vars(c)
{'hue': 33, 'saturation': 1.0, 'lightness': 0.5}
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
Traceback (most recent call last):
  File "/Users/raymond/Dropbox/Public/army2/dataclass_demo.py", line 17, in <module>
    c.show()
  File "/Users/raymond/Dropbox/Public/army2/dataclass_demo.py", line 10, in show
    print(f'{self.hue}\N{degree sign} / {100.0 * self.saturation:.2f}% / {100.0 * self.luminosity:.2f}%')
AttributeError: 'Color' object has no attribute 'luminosity'
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
33° / 100.00% / 50.00%
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
>>> 
======= RESTART: /Users/raymond/Dropbox/Public/army2/dataclass_demo.py =======
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
33° / 100.00% / 50.00%
The saturation is 1.0
Color(hue=33, saturation=1.0, lightness=0.5)
Color(hue=45, saturation=1.0, lightness=0.5)
45° / 100.00% / 50.00%
>>> # __init__ __repr__ __eq__
>>> 
>>> 
>>> x = 11
>>> print('The square of %d is %s' % (x, x**2))          # Old-style
The square of 11 is 121
>>> print('The square of %(x)d is %(sq)s' % dict(sq=x**2, x=x))    # Old-style with dict
The square of 11 is 121
>>> #     C x D = L
>>> # The apple doesn't fall far from the tree
>>> 
>>> print('The square of {x} is {sq}'.format(sq=x**2, x=x))
The square of 11 is 121
>>> print('The square of {x} is {x**2}')
The square of {x} is {x**2}
>>> 
>>> print(  F"Yes!" )
Yes!
>>> 
>>> # F-strings in Python 3.6
>>> # Dataclasses in Python 3.7
>>> print(f'The square of {x} is {x**2}')
The square of 11 is 121
>>> print(F'The square of {x} is {x**2}')
The square of 11 is 121
>>> print(F'The square of {x} is {{x**2}}')
The square of 11 is {x**2}
>>> print('The square of %d is {x**2}' % 10)
The square of 10 is {x**2}
>>> 
