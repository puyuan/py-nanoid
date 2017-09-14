# Python Nanoid

This is python's copy of [nanoid](https://github.com/ai/nanoid)!

**Safe.** It uses cryptographically strong random generator ([urandom](https://docs.python.org/3/library/os.html#os.urandom)).

**Compact.** It uses more symbols than UUID (`A-Za-z0-9_~`)
and has the same number of unique options in just 22 symbols instead of 36.

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

``` pythonma
id = nanoid.generate(size=3)
```

Change ID alphabet

``` python
id = nanoid.generate(alphabet="abcde12345")
```

Change ID length and alphabet

``` python
nanoid.generate(alphabet="abcde12345", size="3")
```


## Credits

- [ai](https://github.com/ai) - [nanoid](https://github.com/ai/nanoid)


## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
