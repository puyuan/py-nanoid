# coding: utf-8

from nanoid import generate
from pytest import approx

alphabet = '_-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


def test_generates_url_friendly_id():
    for _ in range(10):
        id = generate()
        assert len(id) == 21
        for j in range(len(id)):
            assert id[j] in alphabet


def test_flat_distribution():
    count = 100 * 1000
    length = 5
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    chars = {}
    for _ in range(count):
        id = generate(alphabet, length)
        for j in range(len(id)):
            char = id[j]
            if chars.get(char) == None:
                chars[char] = 0
            chars[char] += 1

    assert len(chars.keys()) == len(alphabet)

    for k in chars:
        distribution = (chars[k] * len(alphabet)) / (count * length)
        assert distribution == approx(1, 1)


def test_has_no_collisions():
    count = 100 * 1000
    used = {}
    for _ in range(count):
        id = generate()
        assert not used.has_key(id)
        used[id] = True


def test_has_options():
    assert generate('a', 5) == 'aaaaa'
