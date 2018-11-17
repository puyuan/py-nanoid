# coding: utf-8
from __future__ import unicode_literals
from __future__ import division

from random import random

from nanoid import resources


def non_secure_generate(alphabet=resources.alphabet, size=resources.size):
    alphabet_len = len(alphabet)

    return ''.join([
        alphabet[int(alphabet_len * random())]
        for _ in range(size)
    ])


if __name__ == '__main__':
    print(non_secure_generate())
