from random import random

from nanoid.resources import alphabet, size


def non_secure(alphabet=alphabet, size=size):
    alphabet_len = len(alphabet)

    id = ''
    for _ in range(size):
        id += alphabet[int(random() * alphabet_len) | 0]
    return id


if __name__ == '__main__':
    print(non_secure())
