from __future__ import unicode_literals
from __future__ import division

from math import ceil, log


def method(algorithm, alphabet, size):
    # Integral floats previously worked here; retain that behavior while rejecting
    # fractional/non-finite values before the rejection-sampling loop (#34).
    from numbers import Integral, Real
    from math import isinf, isnan

    if not isinstance(size, Integral):
        if (not isinstance(size, Real) or not size >= 0 or isinf(size)
                or isnan(size) or size != int(size)):
            raise ValueError('size must be a non-negative integer')
        size = int(size)
    if size < 0:
        raise ValueError('size must be a non-negative integer')
    if size == 0:
        return ''

    alphabet_len = len(alphabet)
    if not alphabet_len:
        raise ValueError('alphabet must not be empty')

    mask = 1
    if alphabet_len > 1:
        mask = (2 << int(log(alphabet_len - 1) / log(2))) - 1
    step = int(ceil(1.6 * mask * size / alphabet_len))

    id = ''
    while True:
        random_bytes = algorithm(step)

        for i in range(step):
            random_byte = random_bytes[i] & mask
            if random_byte < alphabet_len:
                if alphabet[random_byte]:
                    id += alphabet[random_byte]

                    if len(id) == size:
                        return id
