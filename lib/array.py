"""
Conversion routines for sequences.
"""
import struct
import ctypes
from pygame2.compat import *

__all__ = ["CTypesView", "to_ctypes"]


# Hack around an import error using relative import paths in Python 2.7
_array = __import__("array")


class CTypesView(object):
    """A proxy for byte-wise accessible data types to be used in ctypes
    bindings.
    """
    def __init__(self, obj, itemsize=1, docopy=False):
        """Creates a new CTypesView for the passed object.

        Unless docopy is True, the CTypesView tries to let ctypes
        bindings and other callers access the object's contents
        directly.

        For certain types, such as the bytearray, the object must not be
        reassigned after being encapsuled and used in ctypes bindings,
        if the contents are not copied.
        """
        self._obj = obj
        self._isshared = True
        self._view = None
        self._itemsize = itemsize
        self._create_view(itemsize, bool(docopy))

    def _create_view(self, itemsize, docopy):
        self._isshared = not docopy
        bsize = len(self._obj) * itemsize

        if docopy:
            self._obj = self._create_copy(self._obj, itemsize)
        try:
            self._view = (ctypes.c_ubyte * bsize).from_buffer(self._obj)
        except AttributeError:
            # pypy ctypes arrays do not feature a from_buffer() method.
            self._isshared = False
            # in case we requested a copy earlier, we do not need to recreate
            # the array, since we have it already. In any other case, create
            # a byte array.
            if not docopy:
                # Try to determine the itemsize again for array
                # instances, just in case the user assumed it to work.
                if isinstance(self._obj, _array.array):
                    itemsize = self._obj.itemsize
                    bsize = len(self._obj) * itemsize
                self._obj = self._create_copy(self._obj, itemsize)
            self._view = (ctypes.c_ubyte * bsize)(*bytearray(self._obj))

    def _create_copy(self, obj, itemsize):
        if itemsize == 1:
            return _array.array("B", obj)
        elif itemsize == 2:
            return _array.array("H", obj)
        elif itemsize == 4:
            return _array.array("I", obj)
        elif itemsize == 8:
            return _array.array("d", obj)
        else:
            raise TypeError("unsupported data type")

    def __repr__(self):
        dtype = type(self._obj).__name__
        bsize = self.bytesize
        return "CTypesView(type=%s, bytesize=%d, shared=%s)" % (dtype, bsize,
                                                                self.is_shared)

    def __len__(self):
        return self.bytesize

    def to_bytes(self):
        """Returns a byte representation of the underlying object."""
        castval = ctypes.POINTER(ctypes.c_ubyte * self.bytesize)
        return ctypes.cast(self.view, castval).contents

    def to_uint16(self):
        """Returns a 16-bit unsigned integer array of the object data."""
        castval = ctypes.POINTER(ctypes.c_ushort * (self.bytesize // 2))
        return ctypes.cast(self.view, castval).contents

    def to_uint32(self):
        """Returns a 32-bit unsigned integer array of the object data."""
        castval = ctypes.POINTER(ctypes.c_uint * (self.bytesize // 4))
        return ctypes.cast(self.view, castval).contents

    def to_uint64(self):
        """Returns a 64-bit unsigned integer array of the object data."""
        castval = ctypes.POINTER(ctypes.c_ulonglong * (self.bytesize // 8))
        return ctypes.cast(self.view, castval).contents

    @property
    def bytesize(self):
        """The size in bytes of the underlying object."""
        return ctypes.sizeof(self.view)

    @property
    def view(self):
        """The ctypes view of the object."""
        return self._view

    @property
    def is_shared(self):
        """Indicates, if changes on the CTypesView data affect the underlying
        object directly.
        """
        return self._isshared

    @property
    def object(self):
        """The underlying object."""
        return self._obj


def to_ctypes(array, dtype):
    """Converts an arbitrary sequence to a ctypes array of the specified type
    and returns the ctypes array and amount of items as two-value tuple.

    Raises a TypeError, if one or more elements in the passed array do not
    match the passed type.
    """
    count = len(array)
    if isinstance(array, CTypesView):
        itemsize = ctypes.sizeof(dtype)
        if itemsize == 1:
            array = array.to_bytes()
        elif itemsize == 2:
            array = array.to_uint16()
        elif itemsize == 4:
            array = array.to_uint32()
        elif itemsize == 8:
            array = array.to_uint64()
        else:
            raise TypeError("unsupported data type for the passed CTypesView")
    valset = (count * dtype)(*array)
    return valset, count
