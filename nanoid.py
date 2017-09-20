from __future__ import unicode_literals
from __future__ import division
from os import urandom
import math


def generate(alphabet='_~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', size=22):
    """
    Create a nanoid
    :param alphabet: optional, specify the alphabets for id generation
    :param size: optional,  specify the size of the id
    :return:
    """
    masks = [15, 31, 63, 127, 255]
    mask = None
    for m in masks:
        if m >= len(alphabet) - 1:
            mask = m
            break
    step = int(math.ceil(1.6 * mask * size / len(alphabet)))
    id = ""
    while True:
        random_bytes = bytearray(urandom(step))
        for i in range(step):
            byte = random_bytes[i] & mask
            if alphabet[byte]:
                id += alphabet[byte]
                if len(id) == size:
                    return id


if __name__ == "__main__":
    print(generate())

