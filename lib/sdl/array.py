"""
Conversion routines for sequences.
"""
import ctypes
from pygame2.sdl import sdltype, dll

def to_ctypes (array, type):
    """to_ctypes (array, type) -> ctypes_array, size
    
    Converts an arbitrary sequence to a ctypes array of the specified type.
    
    Raises a TypeError, if one or more elements in the passed array do not match
    the passed type.
    """
    count = len (array)
    valset = (count * type)(*array)
    return valset, count
