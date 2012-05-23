"""
Python compatibility helpers.
"""
import sys
import collections
import warnings

__all__ = ["stringify", "byteify", "isiterable", "ISPYTHON2", "ISPYTHON3"]

ISPYTHON2 = False
ISPYTHON3 = False

if sys.version_info[0] < 3:
    # Wrapper around bytes() and decode() for Python 2.x
    byteify = lambda x, enc: x.encode(enc)
    stringify = lambda x, enc: str(x)
    ISPYTHON2 = True
else:
    __all__ += ["long", "unichr", "callable"]
    byteify = bytes
    stringify = lambda x, enc: x.decode(enc)
    long = int
    unichr = chr
    callable = lambda x: isinstance(x, collections.Callable)
    ISPYTHON3 = True

isiterable = lambda x: isinstance(x, collections.Iterable)


class deprecated(object):
    """A simple decorator to mark functions and methods as deprecated."""
    def __init__(self):
        pass

    def __call__(self, func):
        def wrapper(*fargs, **kw):
            warnings.warn("%s is deprecated." % func.__name__,
                          category=DeprecationWarning, stackLevel=2)
            return func(*fargs, **kw)
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        wrapper.__dict__.update(func.__dict__)


def deprecation(message):
    """Prints a deprecation message."""
    warnings.warn(message, category=DeprecationWarning, stackLevel=2)


class UnsupportedError(Exception):
    """Indicates that a certain class, function or behaviour is not
    supported.
    """
    def __init__(self, obj, msg=None):
        """Creates an UnsupportedError for the specified obj.

        If a message is passed in msg, it will be printed instead of the
        default message.
        """
        super(UnsupportedError, self).__init__()
        self.obj = obj
        self.msg = msg

    def __str__(self):
        if self.msg is None:
            return "'%s' is not supported" % repr(self.obj)
        return repr(self.msg)
