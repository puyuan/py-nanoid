# Python Nanoid

[![CircleCI](https://circleci.com/gh/puyuan/py-nanoid/tree/master.svg?style=svg)](https://circleci.com/gh/puyuan/py-nanoid/tree/master)


A tiny, secure, URL-friendly, unique string ID generator for Python.

This is python's implementation of [nanoid](https://github.com/ai/nanoid)!


* **Safe.** It uses cryptographically strong random generator. ([urandom](https://docs.python.org/3/library/os.html#os.urandom)).

* **Compact.** It uses a larger alphabet than UUID (`A-Za-z0-9_-`).
So ID size was reduced from 36 to 21 symbols.

##  Install

```
pip install nanoid
```


## Usage

Generate ID using defaults

``` python
import nanoid
id = nanoid.generate()
```

Change ID length

``` python
id = nanoid.generate(size=3)
```

Change ID alphabet

``` python
id = nanoid.generate(alphabet="1234567890abcdef")
```

Change ID length and alphabet

``` python
nanoid.generate(alphabet="1234567890abcdef", size=3)
```

Support for Non-secure random generator

```python
nanoid.generate(secure=False)
```


## Credits

- [ai](https://github.com/ai) - [nanoid](https://github.com/ai/nanoid)


## License

The MIT License (MIT). Please see [License File](LICENSE) for more information.

## Change Log

1. v0.3.0 
    - Fix array out of bound error.
2. v2.0.0 
    -  Replace ~ to - in default alphabet
    - Add non-secure fast generator
    - Reduce default characters from 22 to 21