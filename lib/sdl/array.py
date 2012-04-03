"""
Conversion routines for sequences.
"""
import ctypes
from pygame2.compat import *


__all__ = ["to_ctypes"]


class CTypesView(object):
    """A proxy for byte-wise accessible data types to be used in ctypes
    bindings.
    """
    def __init__(self, obj, docopy=False):
        """Creates a new CTypesView for the passed object.

        Unless docopy is True, the CTypesView tries to let ctypes
        bindings and other callers access the object's contents
        directly.

        For certain types, such as the bytearray, the object must not be
        reassigned after being encapsuled and used in ctypes bindings,
        if the contents are not copied.
        """
        self._obj = obj
        self._view = None
        if bool(docopy):
            raise NotImplementedError("copying is not implemented yet")

    def _create_view(self):
        if isinstance(self._obj, bytearray):
            self._view = ctypes.from_buffer(self._obj)
            self._allowchange = False
        elif isinstance(self._obj, memoryview):
            # TODO: we should respect the memoryview layout here...
            self._view = ctypes.from_buffer(self._obj)
            self._allowchange = False
        else:
            # No memory view or bytearray, let's check, if we can create
            # an accessible buffer
            # TODO
            pass

    @property
    def view(self):
        """Gets the ctypes view of the object."""
        if self._view is None:
            self._create_view()
        return self._view

    @property
    def allow_change(self):
        """Indicates, if changes to the underlying object (reassigning,
        resizing, etc.) are allowed.
        """
        if self._view is None:
            self._allowchange = True
        return self._allowchange

    def to_bytes(self):
        """Returns a byte representation of the underlying object."""
        if hasattr(self._obj, "bytes") and callable(self._obj.bytes):
            return self._obj.bytes()
        if hasattr(self._obj, "tobytes") and callable(self._obj.tobytes):
            return self._obj.tobytes()
        if hasattr(self._obj, "to_bytes") and callable(self._obj.to_bytes):
            return self._obj.to_bytes()
        # TODO
        if self._view is None:
            self._create_view()
            castval = POINTER(ctypes.c_ubyte * self.bytesize)
            return ctypes.cast(self._view, castval).contents
        return None

    def to_uint16(self):
        """Returns a 16-bit unsigned integer array of the object data."""
        if self._view is None:
            self._create_view()
        castval = POINTER(ctypes.c_ushort * self.bytesize)
        return ctypes.cast(self._view, castval).contents

    def to_uint32(self):
        """Returns a 32-bit unsigned integer array of the object data."""
        if self._view is None:
            self._create_view()
        castval = POINTER(ctypes.c_uint * self.bytesize)
        return ctypes.cast(self._view, castval).contents

    def to_uint64(self):
        """Returns a 64-bit unsigned integer array of the object data."""
        if self._view is None:
            self._create_view()
        castval = POINTER(ctypes.c_ulonglong * self.bytesize)
        return ctypes.cast(self._view, castval).contents


def to_ctypes(array, dtype):
    """Converts an arbitrary sequence to a ctypes array of the specified type
    and returns the ctypes array and amount of items as two-value tuple.

    Raises a TypeError, if one or more elements in the passed array do not
    match the passed type.
    """
    count = len(array)
    valset = (count * dtype)(*array)
    return valset, count
