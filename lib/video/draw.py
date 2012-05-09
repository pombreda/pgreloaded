"""Drawing routines."""
import ctypes
from pygame2.compat import *
from pygame2.array import MemoryView
from pygame2.color import convert_to_color
import pygame2.sdl.surface as sdlsurface
import pygame2.sdl.pixels as sdlpixels
import pygame2.sdl.rect as rect
from . import sprite

__all__ = ["prepare_color", "fill"]


def prepare_color(color, target):
    """Prepares the passed color for the passed target.
    """
    color = convert_to_color(color)
    pformat = None
    if isinstance(target, sdlpixels.SDL_PixelFormat):
        pformat = target
    elif isinstance(target, sdlsurface.SDL_Surface):
        pformat = target.format
    elif isinstance(target, sprite.Sprite):
        pformat = target.surface.format
    if pformat is None:
        raise TypeError("unsupported target type")
    return sdlpixels.map_rgb(pformat, color.r, color.g, color.b)


def fill(target, color, area=None):
    """Fills a certain area on the passed target with a color.

    If no area is provided, the entire target will be filled with
    the passed color. If an iterable item is provided as area (such as a list
    or tuple), it will be first checked, if the item denotes a single
    rectangular area (4 integer values) before assuming it to be a sequence
    of rectangular areas
    """
    color = prepare_color(color, target)
    rtarget = None
    if isinstance(target, sdlsurface.SDL_Surface):
        rtarget = target
    elif isinstance(target, sprite.Sprite):
        rtarget = target.surface
    else:
        raise TypeError("unsupported target type")

    varea = None
    if area is not None and isiterable(area):
        # can be either a single rect or a list of rects)
        if len(area) == 4:
            # is it a rect?
            try:
                varea = rect.SDL_Rect(int(area[0]), int(area[1]),
                                      int(area[2]), int(area[3]))
            except:
                # No, not a rect, assume a seq of rects.
                pass
        if not varea:  # len(area) == 4 AND varea set.
            varea = []
            for r in area:
                varea.append(rect.SDL_Rect(r[0], r[1], r[2], r[3]))
    if varea is None or isinstance(varea, rect.SDL_Rect):
        sdlsurface.fill_rect(rtarget, varea, color)
    else:
        sdlsurface.fill_rects(rtarget, varea, color)


class PixelView(MemoryView):
    """2D memory view for Sprite and surface pixel access."""
    def __init__(self, source):
        """Creates a new PixelView from a Sprite or SDL_Surface.

        If necessary, the surface will be locked for accessing its pixel data.
        The lock will be removed once the PixelView is garbage-collected or
        deleted.
        """
        target = None
        if isinstance(source, sprite.Sprite):
            target = source.surface
        elif isinstance(source, sdlsurface.SDL_Surface):
            target = source
        else:
            raise TypeError("source must be a Sprite or SDL_Surface")
        self._surface = target
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
        value = prepare_color(value, self._surface)
        target[start // self.itemsize] = value

    def __del__(self):
        if self._surface is not None:
            if sdlsurface.SDL_MUSTLOCK(self._surface):
                sdlsurface.unlock_surface(self._surface)
