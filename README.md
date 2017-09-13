# Python Nanoid

This is python's copy of [nanoid](https://github.com/ai/nanoid)!

**Safe.** It uses cryptographically strong random generator ([urandom](https://docs.python.org/3/library/os.html#os.urandom)).

**Compact.** It uses more symbols than UUID (`A-Za-z0-9_~`)
and has the same number of unique options in just 22 symbols instead of 36.

## Usage

Generate ID using defaults

``` python
import nanoid
id = nanoid()
```

Change ID length

``` python
id = nanoid(size=3)
```

Change ID alphabet

``` python
id = nanoid(alphabet="abcde12345")
```

Change ID length and alphabet

``` python
nanoid(alphabet="abcde12345", size="3")
```


## Credits

- [ai](https://github.com/ai) - [nanoid](https://github.com/ai/nanoid)


## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.
