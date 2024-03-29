"""
Pygame2 is a cross-platform multimedia framework for the excellent
Python programming language. Its purpose is to make writing multimedia
applications, such as games, with Python as easy as possible, while
providing the developer a reliable and extensible programming interface.
"""

import os
import sys
from . import compat

__all__ = ["set_dll_path", "get_dll_path", "version_info"]


# Manipulate the PATH environment, so that the DLLs are loaded correctly.
_DLLPATH = None
if sys.platform in ("win32", "cli"):
    _PATH = os.path.dirname(os.path.abspath(__file__))
    if compat.platform_is_64bit():
        _DPATH = os.path.join("dll", "64bit")
    else:
        _DPATH = os.path.join("dll", "32bit")
    os.environ['PATH'] += ";%s" % (os.path.join(_PATH, _DPATH))
    _DLLPATH = os.path.join(_PATH, _DPATH)


def set_dll_path(path):
    """Sets the path to the DLLs to be used."""
    if not os.path.exists(path) or not os.path.isdir(path):
        raise ValueError("path must be a directory path")
    global _DLLPATH
    _DLLPATH = path


def get_dll_path():
    """Returns the path to the DLLs to be used."""
    return _DLLPATH

__version__ = "2.0.0-beta2"
version_info = (2, 0, 0, "beta2")
