"""Pixel-wise access routines."""
import ctypes
from pygame2.compat import UnsupportedError, experimental
from pygame2.array import MemoryView
import pygame2.sdl.surface as sdlsurface
from . import sprite
from . import draw


__all__ = ["PixelView", "pixels2d", "pixels3d"]


class PixelView(MemoryView):
    """2D memory view for Sprite and surface pixel access."""
    def __init__(self, source):
        """Creates a new PixelView from a Sprite or SDL_Surface.

        If necessary, the surface will be locked for accessing its pixel data.
        The lock will be removed once the PixelView is garbage-collected or
        deleted.
        """
        if isinstance(source, sprite.Sprite):
            self._surface = source.surface
            # keep a reference, so the Sprite's not GC'd
            self._sprite = source
        elif isinstance(source, sdlsurface.SDL_Surface):
            self._surface = source
        else:
            raise TypeError("source must be a Sprite or SDL_Surface")

        if sdlsurface.SDL_MUSTLOCK(self._surface):
            sdlsurface.lock_surface(self._surface)

        pxbuf = self._surface.pixels
        itemsize = self._surface.format.BytesPerPixel
        strides = (self._surface.size[1], self._surface.size[0])
        srcsize = self._surface.size[1] * self._surface.pitch
        super(PixelView, self).__init__(pxbuf, itemsize, strides,
                                        getfunc=self._getitem,
                                        setfunc=self._setitem,
                                        srcsize=srcsize)

    def _getitem(self, start, end):
        if self.itemsize == 1:
            # byte-wise access
            return self.source[start:end]
        # move the pointer to the correct location
        src = ctypes.byref(self.source.contents, start)
        casttype = ctypes.c_ubyte
        if self.itemsize == 2:
            casttype = ctypes.c_ushort
        elif self.itemsize == 3:
            # TODO
            raise NotImplementedError("unsupported bpp")
        elif self.itemsize == 4:
            casttype = ctypes.c_uint
        return ctypes.cast(src, ctypes.POINTER(casttype)).contents.value

    def _setitem(self, start, end, value):
        target = None
        if self.itemsize == 1:
            target = ctypes.cast(self.source, ctypes.POINTER(ctypes.c_ubyte))
        elif self.itemsize == 2:
            target = ctypes.cast(self.source, ctypes.POINTER(ctypes.c_ushort))
        elif self.itemsize == 3:
            # TODO
            raise NotImplementedError("unsupported bpp")
        elif self.itemsize == 4:
            target = ctypes.cast(self.source, ctypes.POINTER(ctypes.c_uint))
        value = draw.prepare_color(value, self._surface)
        target[start // self.itemsize] = value

    def __del__(self):
        if self._surface is not None:
            if sdlsurface.SDL_MUSTLOCK(self._surface):
                sdlsurface.unlock_surface(self._surface)

_HASNUMPY = True
try:
    import numpy

    class SurfaceArray(numpy.ndarray):
        """Wrapper class around numpy.ndarray.

        Used to keep track of the original source object for pixels2d()
        and pixels3d() to avoid the deletion of the source object.
        """
        def __new__(subtype, shape, dtype=float, buffer_=None, offset=0,
                    strides=None, order=None, source=None, surface=None):
            sfarray = numpy.ndarray.__new__(subtype, shape, dtype, buffer_,
                                            offset, strides, order)
            sfarray._source = source
            sfarray._surface = surface
            return sfarray

        def __array_finalize__(self, sfarray):
            if sfarray is None:
                return
            self._source = getattr(sfarray, '_source', None)
            self._surface = getattr(sfarray, '_surface', None)

        def __del__(self):
            if self._surface:
                if sdlsurface.SDL_MUSTLOCK(self._surface):
                    sdlsurface.unlock_surface(self._surface)

except ImportError:
    _HASNUMPY = False


@experimental
def pixels2d(source):
    """Creates a 2D pixel array from the passed source."""
    if not _HASNUMPY:
        raise UnsupportedError("numpy module could not be loaded")
    if isinstance(source, sprite.Sprite):
        surface = source.surface
    elif isinstance(source, sdlsurface.SDL_Surface):
        surface = source
    else:
        raise TypeError("source must be a Sprite or SDL_Surface")

    bpp = surface.format.BytesPerPixel
    if bpp < 1 or bpp > 4:
        raise ValueError("unsupported bpp")
    strides = (surface.pitch, bpp)
    srcsize = surface.size[1] * surface.pitch
    shape = surface.size[1], surface.pitch // bpp

    dtypes = {1: numpy.uint8,
              2: numpy.uint16,
              3: numpy.uint32,
              4: numpy.uint32
              }

    if sdlsurface.SDL_MUSTLOCK(surface):
        sdlsurface.lock_surface(surface)
    pxbuf = ctypes.cast(surface.pixels,
                        ctypes.POINTER(ctypes.c_ubyte * srcsize)).contents
    return SurfaceArray(shape, dtypes[bpp], pxbuf, 0, strides, "C", source,
                        surface)


@experimental
def pixels3d(source):
    """Creates a 3D pixel array from the passed source.
    """
    if not _HASNUMPY:
        raise UnsupportedError("numpy module could not be loaded")
    if isinstance(source, sprite.Sprite):
        surface = source.surface
    elif isinstance(source, sdlsurface.SDL_Surface):
        surface = source
    else:
        raise TypeError("source must be a Sprite or SDL_Surface")

    bpp = surface.format.BytesPerPixel
    if bpp < 1 or bpp > 4:
        raise ValueError("unsupported bpp")
    strides = (surface.pitch, bpp, 1)
    srcsize = surface.size[1] * surface.pitch
    shape = surface.size[1], surface.pitch // bpp, bpp

    if sdlsurface.SDL_MUSTLOCK(surface):
        sdlsurface.lock_surface(surface)
    pxbuf = ctypes.cast(surface.pixels,
                        ctypes.POINTER(ctypes.c_ubyte * srcsize)).contents
    return SurfaceArray(shape, numpy.uint8, pxbuf, 0, strides, "C", source,
                        surface)
