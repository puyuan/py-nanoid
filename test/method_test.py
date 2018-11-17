# coding: utf-8

from sys import maxsize
from unittest import TestCase

from nanoid.method import method
from nanoid.resources import size


class TestMethod(TestCase):
    def test_generates_random_string(self):
        sequence = [2, 255, 3, 7, 7, 7, 7, 7, 0, 1]

        def rand(size=size):
            random_bytes = []
            for i in range(0, size, len(sequence)):
                random_bytes += sequence[0:size-i]
            return random_bytes
        self.assertEqual(method(rand, 'abcde', 4), 'cdac')
