# coding: utf-8

from random import random

from alphabet import alphabet


def non_secure_generate(alphabet=alphabet, size=21):
    alphabet_len = len(alphabet)

    return ''.join([
        alphabet[int(alphabet_len * random())]
        for _ in range(size)
    ])


if __name__ == '__main__':
    print(non_secure_generate())
