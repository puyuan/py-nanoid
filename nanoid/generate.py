# coding: utf-8
from __future__ import unicode_literals
from __future__ import division

from nanoid.algorithm import algorithm_generate
from nanoid.method import method
from nanoid.resources import alphabet, size


def generate(alphabet: str = alphabet, size: int = size) -> str:
    return method(algorithm_generate, alphabet, size)
