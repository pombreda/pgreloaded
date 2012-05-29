"""
A thin wrapper package around the OpenAL library.
"""
import os
import sys
import ctypes
from pygame2.dll import DLL

_LIBNAME = None
_FALLBACK = None
if sys.platform in ("win32", "cli"):
    _LIBNAME = "OpenAL32.dll"
    _FALLBACK = "soft_oal.dll"
elif sys.platform == "darwin":
    _LIBNAME = "OpenAL"
else:
    _LIBNAME = "openal"

dll = None
dll = DLL("OpenAL", {"win32" : ["OpenAL", "OpenAL32", "soft_oal"],
                     "darwin" : ["OpenAL"],
                     "DEFAULT" : ["openal"]}
          )
openaltype = dll.get_decorator()
