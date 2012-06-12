"""
A thin wrapper package around the OpenAL library.
"""
import os
import sys
import ctypes
from pygame2.dll import DLL

dll = DLL("OpenAL", {"win32": ["OpenAL", "OpenAL32", "soft_oal"],
                     "darwin": ["OpenAL"],
                     "DEFAULT": ["openal"]}
          )
openaltype = dll.get_decorator()

def get_dll_file():
    """Gets the file name of the loaded OpenAL library."""
    return dll.libfile
