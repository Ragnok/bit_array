''' Goal:  Learn about code generators that create
    data holders or generate boiler plate code for
    a class.

Video on dataclasses:
    # https://www.youtube.com/watch?v=T-TwcmT6Rcw&t=15s

Named tuples are tuple-like, so they are immutable
hashable, compact, iterable, and unpackable.

Dataclasses are like regular classes with an instance
dictionary.  It automatically provides __init__,
__repr__, __eq__, and turns off hashing.   They are
mutable, unhashable, large, and cannot be unpacked.

'''

from typing import NamedTuple
from dataclasses import dataclass

class Color(NamedTuple):
    hue: int
    saturation: float
    lightness: float = 0.5

    def show(self):
        print(f'{self.hue}\N{degree sign} / {100.0 * self.saturation:.2f}% / {100.0 * self.lightness:.2f}%')

c = Color(33, 1.0)
print(f'The saturation is {c.saturation}')
print(c)
d = c._replace(hue=45)
print(d)
c.show()

@dataclass
class Color:
    hue: int
    saturation: float
    lightness: float = 0.5

    def show(self):
        print(f'{self.hue}\N{degree sign} / {100.0 * self.saturation:.2f}% / {100.0 * self.lightness:.2f}%')

c = Color(33, 1.0)
print(f'The saturation is {c.saturation}')
print(c)
c.hue = 45
print(c)
c.show()
