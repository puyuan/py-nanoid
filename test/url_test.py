from unittest import TestCase

from nanoid.resources import alphabet


class TestURL(TestCase):
    def test_has_no_duplicates(self):
        for i in range(len(alphabet)):
            self.assertEqual(alphabet.rindex(alphabet[i]), i)

    def test_is_string(self):
        self.assertEqual(type(alphabet), str)
