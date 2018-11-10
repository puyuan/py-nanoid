from unittest import TestCase

from nanoid import generate


class TestNanoId(TestCase):
    def test_secure_ids(self):
        for i in range(10000):
            nanoid = generate()
            self.assertEqual(len(nanoid), 21)

    def test_short_secure_ids(self):
        for i in range(10000):
            nanoid = generate(alphabet="12345a", size=3)
            self.assertEqual(len(nanoid), 3)

    def test_non_secure_ids(self):
        for i in range(10000):
            nanoid = generate(secure=False)
            self.assertEqual(len(nanoid), 21)

    def test_non_secure_short_ids(self):
        for i in range(10000):
            nanoid = generate(alphabet="12345a", size=3, secure=False)
            self.assertEqual(len(nanoid), 3)
