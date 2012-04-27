"""
Python compatibility helpers.
"""
import sys
import collections

if sys.version_info[0] < 3:
    __all__ = ["stringify", "byteify", "isiterable"]
    # Wrapper around bytes() and decode() for Python 2.x
    byteify = lambda x, enc: x.encode(enc)
    stringify = lambda x, enc: str(x)
else:
    __all__ = ["stringify", "byteify", "long", "unichr", "callable",
               "isiterable"
               ]
    byteify = bytes
    stringify = lambda x, enc: x.decode(enc)
    long = int
    unichr = chr
    callable = lambda x: isinstance(x, collections.Callable)

isiterable = lambda x: isinstance(x, collections.Iterable)
