# coding: utf-8

from alphabet import alphabet
from random import random


def _non_secure_generate(alphabet, size):
    alphabet_len = len(alphabet)

    return ''.join([
        alphabet[int(alphabet_len * random())]
        for _ in range(size)
    ])


def fast_generate(alphabet=alphabet, size=21):
    return _non_secure_generate(alphabet=alphabet, size=size)


if __name__ == '__main__':
    print(fast_generate())
