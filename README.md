# Nano ID

A tiny, secure, URL-friendly, unique string ID generator for Python.

* __Safe__. It uses cryptographically strong random APIs and tests distribution of symbols.
* __Compact__. It uses a larger alphabet than UUID (A-Za-z0-9_-). So ID size was reduced from 36 to 21 symbols.

## Usage

Install Nano ID using pip:

```
pip install nanoid2
```

### Normal

The main module uses URL-friendly symbols (A-Za-z0-9_-) and returns an ID with 21 characters (to have a collision probability similar to UUID v4).

```python
import nanoid

nanoid.generate() # => NDzkGoTCdRcaRyt7GOepg
```

Symbols `-,.()` are not encoded in the URL. If used at the end of a link they could be identified as a punctuation symbol.

If you want to reduce ID length (and increase collisions probability), you can pass the length as an argument.

```python
nanoid.generate(size=10) # => "IRFa-VaY2b"
```
Don’t forget to check the safety of your ID length in ID [collision probability calculator](https://zelark.github.io/nano-id-cc/).

## Custom Alphabet or Length

If you want to change the ID's alphabet or length you can use the internal generate module.

```python
import nanoid
import nanoid_dictionary

nanoid.generate(nanoid_dictionary.human_alphabet, 10) # => "4f9zd13a42"
```

Non-secure API is also available:

```python
import nanoid.non_secure
import nanoid_dictionary

nanoid.non_secure.generate(nanoid_dictionary.alphabet_std, 10)
```

## Nano ID dictionary

Nano ID dictionary has `alphabet_std` and `human_alphabet` alphabets.

The dictionary also provides many useful sets of strings and functions to use: `lookalikes`, `lowercase`, `numbers`, `uppercase`, `prevent_misreadings(string, unsafe_chars)`.

`prevent_misreadings(string, unsafe_chars)` accepts a string and removes all the characters that look similar. You can pass your own optional character set if you want.

```python
from nanoid_dictionary import *

alphabet_std # => _-0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
human_alphabet # => _-23456789abcdefghijkmnpqrstuvwxyzABCDEFGHIJKMNPQRSTUVWXYZ

lookalikes # => 1l0o
lowercase # => abcdefghijklmnopqrstuvwxyz
numbers # => 0123456789
prevent_misreadings('a1l0o', lookalikes)) # => a
uppercase # => ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

## Tools

* [ID size calculator](https://zelark.github.io/nano-id-cc/) to choice smaller ID size depends on your case.
nanoid-dictionary with popular alphabets to use with nanoid/generate.
* [`nanoid-dictionary`](https://github.com/aidarkhanov/nanoid-dictionary) with popular alphabets to use.

## Thanks to
* Andrey Sitnik for [Nano ID](https://github.com/ai/nanoid);
* Stanislav Lashmanov for [Nano ID dictionary](https://github.com/CyberAP/nanoid-dictionary);
* Aleksandr Zhuravlev for [ID collision probability](https://zelark.github.io/nano-id-cc/).

## Other Programming Languages

* [C#](https://github.com/codeyu/nanoid-net)
* [Clojure and ClojureScript](https://github.com/zelark/nano-id)
* [Crystal](https://github.com/mamantoha/nanoid.cr)
* [Dart](https://github.com/pd4d10/nanoid)
* [Go](https://github.com/matoous/go-nanoid)
* [Elixir](https://github.com/railsmechanic/nanoid)
* [Haskell](https://github.com/4e6/nanoid-hs)
* [Java](https://github.com/aventrix/jnanoid)
* [JavaScript](https://github.com/ai/nanoid)
* [Nim](https://github.com/icyphox/nanoid.nim)
* [PHP](https://github.com/hidehalo/nanoid-php)
* [Ruby](https://github.com/radeno/nanoid.rb)
* [Rust](https://github.com/nikolay-govorov/nanoid)
* [Swift](https://github.com/antiflasher/NanoID)
