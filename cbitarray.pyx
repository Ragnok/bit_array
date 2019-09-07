''' Build a bitarray with an API similar to bytearray

List of techniques:
    - Pick out the n-th bit:           (x >> n) & 1
    - Set the n-th bit:                (1 << n) | x
    - Reset (unset) the n-th bit:      ~(1 << n) & x
    - Ceiling division:                -(n // -d)
    - Floor division and modulo:       divmod(n, d)

Model of bitarray built on a bytearray

     0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23      <= i or index
     ------------------------------|-------------------------------|------------------------------
     0   0   0   0   0   0   0   0 | 1   1   1   1   1   1   1   1 | 2   2   2   2   2   2   2   2      <== i // 8
     0   1   2   3   4   5   6   7 | 0   1   2   3   4   5   6   7 | 0   1   2   3   4   5   6   7      <== i % 8

'''

def ceiling_division(n, d):
    '''Return *n* divided by *d* but rounded up if there is a remainder

        To provision 16 eggs in cartons that hold 12 eggs,
        you need two cartons:

            >>> ceiling_division(16, 12)
            2

    '''
    # https://www.amazon.com/Hackers-Delight-2nd-Henry-Warren/dp/0321842685
    return -(n // -d)

class BitArray:
    'An array of bits models after the bytearray'

    def _check_and_adjust_index(self, index):
        if index < 0:
            index += len(self)
        if index < 0 or index >= len(self):
            raise IndexError('bitarray index out of range')
        return index

    def __init__(self, numbits):
        self.numbits = numbits
        numbytes = ceiling_division(numbits, 8)
        self.data = bytearray(numbytes)

    def __len__(self):
        return self.numbits

    def __getitem__(self, int index):
        cdef int bytenum, bitnum

        index = self._check_and_adjust_index(index)
        # bytenum, bitnum = divmod(index, 8)
        bytenum = index >> 3
        bitnum = index & 7
        return (self.data[bytenum] >> bitnum) & 1

    def __setitem__(self, index, value):
        index = self._check_and_adjust_index(index)
        if not isinstance(value, int):
            raise TypeError('an integer of size 1 is required')
        if value not in (0, 1):
            raise ValueError('bit must be a 0 or 1')
        bytenum, bitnum = divmod(index, 8)
        mask = 1 << bitnum
        if value:
            self.data[bytenum] |= mask
        else:
            self.data[bytenum] &= ~mask

    def __repr__(self):
        size = min(len(self), 30)
        bits = ''.join([str(self[i]) for i in range(size)])
        if len(self) > size:
            bits += ' ...'
        return 'BitArray(%r)' % bits

if __name__ == '__main__':

    import doctest

    print doctest.testmod()

    b = BitArray(20)
    print len(b)
    b[11] = 1
    b[13] = 1
    b[5] = 1
    b[6] = 1
    b[13] = 0
    print b[11]
    print b[13]
    print b[5]
    print b[6]
    print b[13]
    print list(b)
    print b
