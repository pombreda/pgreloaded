"""
Wrapper methods around the SDL 2 endian routines.
"""
import sys
import ctypes
from pygame2.sdl import sdltype, dll

__all__ = ["SDL_BYTEORDER", "SDL_LIL_ENDIAN", "SDL_BIG_ENDIAN", "swap16",
           "swap32", "swap64", "swap_float", "swap_le_16", "swap_le_32",
           "swap_le_64", "swap_float_le", "swap_float_be", "swap_be_16",
           "swap_be_32", "swap_be_64"
           ]

SDL_LIL_ENDIAN = 1234
SDL_BIG_ENDIAN = 4321

SDL_BYTEORDER = SDL_LIL_ENDIAN
if sys.byteorder != 'little':
    SDL_BYTEORDER = SDL_BIG_ENDIAN


def swap16(x):
    """Swaps the byte order of a 16-bit value."""
    return ((x << 8 & 0xFF00) | (x >> 8 & 0x00FF))


def swap32(x):
    """Swaps the byte order of a 32-bit value."""
    return (((x << 24) & 0xFF000000) |
            ((x <<  8) & 0x00FF0000) |
            ((x >>  8) & 0x0000FF00) |
            ((x >> 24) & 0x000000FF))


def swap64(x):
    """Swaps the byte order of a 64-bit value."""
    return (swap32(x & 0xFFFFFFFF) << 32) | (swap32(x >> 32 & 0xFFFFFFFF))


def swap_float(x):
    """Swaps the byte order of a float value."""
    raise NotImplementedError("not yet implemented")


def _nop(x):
    """No operation handler for little/big endian wrappers on the specific
    platform.
    """
    return x

if SDL_BYTEORDER == SDL_LIL_ENDIAN:
    swap_le_16 = _nop
    swap_le_32 = _nop
    swap_le_64 = _nop
    swap_float_le = _nop
    swap_be_16 = swap16
    swap_be_32 = swap32
    swap_be_64 = swap64
    swap_float_be = swap_float  # TODO
else:
    swap_be_16 = _nop
    swap_be_32 = _nop
    swap_be_64 = _nop
    swap_float_be = _nop
    swap_le_16 = swap16
    swap_le_32 = swap32
    swap_le_64 = swap64
    swap_float_le = swap_float  # TODO
