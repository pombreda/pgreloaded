"""
Conversion routines for sequences.
"""

__all__ = ["to_ctypes"]


def to_ctypes(array, dtype):
    """Converts an arbitrary sequence to a ctypes array of the specified type
    and returns the ctypes array and amount of items as two-value tuple.

    Raises a TypeError, if one or more elements in the passed array do not
    match the passed type.
    """
    count = len(array)
    valset = (count * dtype)(*array)
    return valset, count
