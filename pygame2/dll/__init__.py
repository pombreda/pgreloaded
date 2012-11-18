"""
DLL loading helpers.
"""
import os
import sys
import ctypes
import warnings
from ctypes.util import find_library
from pygame2 import get_dll_path

__all__ = ["DLL"]


def _findlib(path, libnames):
    """."""
    platform = sys.platform
    if platform in ("win32", "cli"):
        prefix = ""
        suffix = ".dll"
    elif platform == "darwin":
        prefix = "lib"
        suffix = ".dylib"
    else:
        prefix = "lib"
        suffix = ".so"

    searchfor = libnames
    if type(libnames) is dict:
        # different library names for the platforms
        if platform == "cli" and platform not in libnames:
            # if not explicitly specified, use the Win32 libs for IronPython
            platform = "win32"
        if platform not in libnames:
            platform = "DEFAULT"
        searchfor = libnames[platform]

    results = []
    if path:
        for libname in searchfor:
            dll = os.path.join(path, "%s%s%s" % (prefix, libname, suffix))
            if os.path.exists(dll):
                results.append(dll)
    for libname in searchfor:
        dll = find_library(libname)
        if dll:
            results.append(dll)
    return results


class DLL(object):
    """Function wrapper around the different DLL functions. Do not use or
    instantiate this one directly from your user code.
    """
    def __init__(self, libinfo, libnames):
        self._dll = None
        foundlibs = _findlib(get_dll_path(), libnames)
        if len(foundlibs) == 0:
            raise RuntimeError("could not find any library for %s" % libinfo)
        for libfile in foundlibs:
            try:
                self._dll = ctypes.CDLL(libfile)
                self._libfile = libfile
                break
            except Exception as exc:
                # Could not load it, silently ignore that issue and move
                # to the next one.
                warnings.warn(exc, ImportWarning)
        if self._dll is None:
            raise RuntimeError("could not load any library for %s" % libinfo)

    def has_dll_function(self, name):
        """Checks, if a function identified by name exists in the bound
        DLL.
        """
        return hasattr(self._dll, name)

    def get_dll_function(self, name):
        """Tries to retrieve the function identified by name from the
        bound DLL.
        """
        func = getattr(self._dll, name)
        return func

    def add_function(self, name, func):
        """Adds the passed function to the DLL instance.

        The function will be identified by the passed name, so that a
        invocation of mydll.name (...) will invoke the bound function.
        """
        self.__dict__[name] = func

    def get_decorator(self):
        """Gets the decorator binding for the DLL."""
        class dlltype(object):
            """Decorator class used to wrap DLL related functions.

            You should not use this decorator in user code.
            """
            dll = None

            def __init__(self_, funcname=None, args=None, returns=None):
                func = self_.dll.get_dll_function(funcname)
                func.argtypes = args
                func.restype = returns
                self_.dll.add_function(funcname, func)

            def __call__(self_, func):
                return func
        dlltype.dll = self
        return dlltype

    @property
    def libfile(self):
        """Gets the filename of the loaded library."""
        return self._libfile
