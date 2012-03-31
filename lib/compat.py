"""
Python compatibility helpers.
"""
import sys


if sys.version_info[0] < 3:
    __all__ = ["stringify", "byteify"]
    # Wrapper around bytes() and decode() for Python 2.x
    byteify = lambda x, enc: x.encode(enc)
    stringify = lambda x, enc: str(x)
else:
    __all__ = ["stringify", "byteify", "long", "unichr", "callable"]
    byteify = bytes
    stringify = lambda x, enc: x.decode(enc)
    long = int
    unichr = chr
    from collections import Callable
    callable = lambda x: isinstance(x, Callable)
