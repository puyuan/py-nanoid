from os import urandom
import math

def nanoid(alphabet='_~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', size=22, random=urandom):
    url = '_~0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_bytes = urandom(size)
    id_list = [url[random_bytes[i] & 63] for i in range(size)]
    id = "".join(id_list)
    return id

def format(random, alphabet, size):
    masks = [15, 31, 63, 127, 255]
    mask = None
    for m in masks:
        if m >= len(alphabet) - 1:
            mask = m
            break
    step = math.ceil(1.6*mask*size/len(alphabet))
    id = None
    while True:
        random_bytes = random(step)
        for i in range(step):
            byte = random_bytes[i] & mask
            if alphabet[byte]:
                id += alphabet[byte]
                if len(id) == size:
                    return id


if __name__ == "__main__":
    print(nanoid())

