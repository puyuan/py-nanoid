from __future__ import unicode_literals
from __future__ import division

from math import ceil, log


def method(algorithm, alphabet, size):
    alphabet_len = len(alphabet)

    mask = 1
    if alphabet_len > 1:
        mask = (1 << int(ceil(log(alphabet_len) / log(2)))) - 1
    step = int(ceil(1.6 * mask * size / alphabet_len))

    id = ''
    while True:
        for random_byte in algorithm(step):
            random_byte = random_byte & mask
            if random_byte < alphabet_len:
                id += alphabet[random_byte]
                if len(id) == size:
                    return id
