"""
DLL loading helpers.
"""
import os
import ctypes
from ctypes.util import find_library
from pygame2 import get_dll_path

__all__ = ["DLL"]


class DLL(object):
    """Function wrapper around the different DLL functions. Do not use or
    instantiate this one directly from your user code.
    """
    def __init__(self, libname):
        self._dll = None
        lib = None
        path = get_dll_path()
        if path:
            # Explicit path provided by the user or Win32
            lib = os.path.join(path, libname)
            if not os.path.exists(lib):
                lib = find_library(libname)
        else:
            lib = find_library(libname)
        if lib is None:
            raise RuntimeError("could not find libary %s" % libname)
        self._dll = ctypes.CDLL(lib)

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
