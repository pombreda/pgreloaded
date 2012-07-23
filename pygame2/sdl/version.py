"""
Wrapper methods around the SDL2 version info routines.
"""
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll

__all__ = ["SDL_version", "SDL_VERSIONNUM", "SDL_VERSION_ATLEAST",
           "get_version", "get_revision", "get_revision_number"]


class SDL_version(ctypes.Structure):
    """A SDL_version instance containing the SDL library version.
    """
    _fields_ = [("major", ctypes.c_ubyte),
                ("minor", ctypes.c_ubyte),
                ("patch", ctypes.c_ubyte),
                ]

    def __init__(self, major=0, minor=0, patch=0):
        self.major = major
        self.minor = minor
        self.patch = patch

    def __repr__(self):
        return '%d.%d.%d' % (self.major, self.minor, self.patch)


def SDL_VERSIONNUM(major, minor, patch):
    """Calculates the passed version number as integer in the form
    major * 1000 + minor * 100 + patch.
    """
    return major * 1000 + minor * 100 + patch


def SDL_VERSION_ATLEAST(major, minor, patch):
    """Checks, if the used SDL library has at least the passed version."""
    lversion = get_version()
    return SDL_VERSIONNUM(lversion.major, lversion.minor, lversion.patch) >= \
        SDL_VERSIONNUM(major, minor, patch)


@sdltype("SDL_GetVersion", [ctypes.POINTER(SDL_version)], None)
def get_version():
    """Returns a SDL_version object containing the version of the used SDL
    library.
    """
    version = SDL_version()
    dll.SDL_GetVersion(ctypes.byref(version))
    return version


@sdltype("SDL_GetRevision", None, ctypes.c_char_p)
def get_revision():
    """Returns the unique revision of the used SDL library."""
    return stringify(dll.SDL_GetRevision(), "utf-8")


@sdltype("SDL_GetRevisionNumber", None, ctypes.c_int)
def get_revision_number():
    """Returns the revision number of the used SDL library."""
    return dll.SDL_GetRevisionNumber()
