# coding: utf-8

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

    def test_rejects_fractional_negative_and_nonfinite_sizes(self):
        for invalid_size in (12.5, -1, float('nan'), float('inf'), '3', None):
            with self.assertRaises(ValueError):
                method(lambda count: self.fail('randomness requested'), 'abc', invalid_size)

    def test_zero_does_not_request_randomness(self):
        self.assertEqual(method(lambda count: self.fail('randomness requested'), '', 0), '')

    def test_empty_alphabet_fails_before_randomness(self):
        with self.assertRaises(ValueError):
            method(lambda count: self.fail('randomness requested'), '', 1)
