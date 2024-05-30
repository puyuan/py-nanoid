# coding: utf-8

from unittest import TestCase
from typing import List

from nanoid.method import method
from nanoid.resources import size


class TestMethod(TestCase):
    def test_generates_random_string(self) -> None:
        sequence = [2, 255, 3, 7, 7, 7, 7, 7, 0, 1]

        def rand(size: int = size) -> List[int]:
            random_bytes: List[int] = []
            for i in range(0, size, len(sequence)):
                random_bytes += sequence[0:size-i]
            return random_bytes
        self.assertEqual(method(rand, 'abcde', 4), 'cdac')
