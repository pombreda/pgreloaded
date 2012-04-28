"""Sprite, texture and pixel surface routines."""
import os
import ctypes
from pygame2.array import MemoryView
from pygame2.ebs import Component, System
import pygame2.sdl.surface as sdlsurface
import pygame2.sdl.rect as rect
import pygame2.sdl.video as video
import pygame2.sdl.rwops as rwops

__all__ = ["SpriteRenderer", "Sprite", "PixelView"]


class SpriteRenderer(System):
    """A rendering system for Sprite components.

    The SpriteRenderer class uses a Window as drawing device to display
    Sprite surfaces. It uses the Window's internal SDL surface as
    drawing context, so that GL operations, such as texture handling or
    using SDL renderers is not possible.
    """
    def __init__(self, window):
        """Creates a new SpriteRenderer for a specific Window."""
        self.window = window
        self.surface = video.get_window_surface(window.window)

    def render(self, sprite):
        """Draws the passed sprite on the Window's surface."""
        r = rect.SDL_Rect(sprite.x, sprite.y, 0, 0)
        sdlsurface.blit_surface(sprite.surface, None, self.surface, r)
        video.update_window_surface(self.window.window)

    def process(self, world, components):
        """Draws the passed Sprite objects on the Window's surface."""
        r = rect.SDL_Rect(0, 0, 0, 0)
        for sprite in components:
            r.x = sprite.x
            r.y = sprite.y
            sdlsurface.blit_surface(sprite.surface, None, self.surface, r)
        video.update_window_surface(self.window.window)


class Sprite(Component):
    """A simple, visible, pixel-based 2D object."""
    def __init__(self, source=None, size=(0, 0), bpp=32):
        """Creates a new Sprite.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided a size tuple, containing the width and
        height of the sprite, and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        if source is not None:
            if type(source) is str:
                if os.path.exists(source):
                    # Load from file
                    self.surface = sdlsurface.load_bmp(source)
                else:
                    # TODO: string buffer
                    raise NotImplementedError("string buffers not supported")
            else:
                rw = rwops.rw_from_object(source)
                self.surface = sdlsurface.load_bmp_rw(rw, True)
        else:
            self.surface = sdlsurface.create_rgb_surface(size[0], size[1],
                                                         bpp)
        self.x = 0
        self.y = 0

    @property
    def position(self):
        """The top-left position of the Sprite as tuple."""
        return self.x, self.y

    @position.setter
    def position(self, value):
        self.x = value[0]
        self.y = value[1]

    @property
    def size(self):
        """The size of the Sprite as tuple."""
        return self.surface.size


class PixelView(MemoryView):
    """2D memory view for Sprite and surface pixel access."""
    def __init__(self, source):
        """Creates a new PixelView from a Sprite or SDL_Surface.

        If necessary, the surface will be locked for accessing its pixel data.
        The lock will be removed once the PixelView is garbage-collected or
        deleted.
        """
        target = None
        if isinstance(source, Sprite):
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
        strides = self._surface.size
        srcsize = self._surface.size[1] * self._surface.pitch
        super(PixelView, self).__init__(pxbuf, itemsize, strides,
                                        getfunc=self._getitem,
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
            # return byte-wise
            return self.source[start:end]
        elif self.itemsize == 4:
            casttype = ctypes.c_uint
        return ctypes.cast(src, ctypes.POINTER(casttype)).contents.value

    def __del__(self):
        if self._surface is not None:
            if sdlsurface.SDL_MUSTLOCK(self._surface):
                sdlsurface.unlock_surface(self._surface)
