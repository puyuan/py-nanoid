# coding: utf-8

from algorithm import algorithm_generate
from method import method
from resources import alphabet, size


def generate(alphabet=alphabet, size=size):
    return method(algorithm_generate, alphabet, size)


if __name__ == '__main__':
    print(generate())
