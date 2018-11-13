# coding: utf-8

from sys import maxsize
from unittest import TestCase

from nanoid import generate
from nanoid.resources import alphabet


class TestNanoID(TestCase):
    def test_generates_url_friendly_id(self):
        for _ in range(10):
            id = generate()
            self.assertEqual(len(id), 21)
            for j in range(len(id)):
                self.assertIn(id[j], alphabet)

    def test_flat_distribution(self):
        count = 100 * 1000
        length = 5
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        chars = {}
        for _ in range(count):
            id = generate(alphabet, length)
            for j in range(len(id)):
                char = id[j]
                if not chars.get(char):
                    chars[char] = 0
                chars[char] += 1

        self.assertEqual(len(chars.keys()), len(alphabet))

        max = 0
        min = maxsize
        for k in chars:
            distribution = (chars[k] * len(alphabet)) / float((count * length))
            if distribution > max:
                max = distribution
            if distribution < min:
                min = distribution
        self.assertLessEqual(max - min, 0.05)

    def test_has_no_collisions(self):
        count = 100 * 1000
        used = {}
        for _ in range(count):
            id = generate()
            self.assertIsNotNone(used.has_key(id))
            used[id] = True

    def test_has_options(self):
        self.assertEqual(generate('a', 5), 'aaaaa')
