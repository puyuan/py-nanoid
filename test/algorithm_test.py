from unittest import TestCase

from nanoid.algorithm import algorithm_generate


class TestAlgorithm(TestCase):
    def test_generates_random_buffers(self):
        numbers = {}
        random_bytes = algorithm_generate(10000)
        self.assertEqual(len(random_bytes), 10000)
        for i in range(len(random_bytes)):
            if not numbers.get(random_bytes[i]):
                numbers[random_bytes[i]] = 0
            numbers[random_bytes[i]] += 1
            self.assertEqual(type(random_bytes[i]), int)
            self.assertLessEqual(random_bytes[i], 255)
            self.assertGreaterEqual(random_bytes[i], 0)

    def test_generates_small_random_buffers(self):
        self.assertEqual(len(algorithm_generate(10)), 10)
