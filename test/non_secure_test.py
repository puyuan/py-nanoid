from sys import maxsize
from unittest import TestCase

from nanoid import non_secure_generate
from nanoid.resources import alphabet


class TestNonSecure(TestCase):
    def test_changes_id_length(self):
        self.assertEqual(len(non_secure_generate(size=10)), 10)
        self.assertEqual(non_secure_generate('', 0), '')
        self.assertEqual(non_secure_generate('a', -1), '')
        self.assertEqual(non_secure_generate(['a'], 3), 'aaa')

    def test_generates_url_friendly_id(self):
        for _ in range(10):
            id = non_secure_generate()
            self.assertEqual(len(id), 21)
            for j in range(len(id)):
                self.assertNotEqual(alphabet.find(id[j]), -1)

    def test_has_flat_distribution(self):
        count = 100 * 1000
        length = len(non_secure_generate())

        chars = {}
        for _ in range(count):
            id = non_secure_generate()
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
            id = non_secure_generate()
            self.assertNotIn(id, used)
            used[id] = True

    def test_custom_alphabet(self):
        for _ in range(10):
            identifier = non_secure_generate('12345a', 3)
            self.assertEqual(len(identifier), 3)
            for character in identifier:
                self.assertIn(character, '12345a')
