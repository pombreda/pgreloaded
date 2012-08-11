"""Sprite, texture and pixel surface routines."""
import os
from pygame2.ebs import Component, System
import pygame2.sdl.surface as sdlsurface
import pygame2.sdl.rect as rect
import pygame2.sdl.video as video
import pygame2.sdl.rwops as rwops

__all__ = ["SpriteRenderer", "Sprite"]


class SpriteRenderer(System):
    """A rendering system for Sprite components.

    The SpriteRenderer class uses a Window as drawing device to display
    Sprite surfaces. It uses the Window's internal SDL surface as
    drawing context, so that GL operations, such as texture handling or
    using SDL renderers is not possible.
    """
    def __init__(self, window):
        """Creates a new SpriteRenderer for a specific Window."""
        super(SpriteRenderer, self).__init__()
        self.window = window
        self.surface = video.get_window_surface(window.window)
        self._sortfunc = lambda e1, e2: cmp(e1.depth, e2.depth)
        self.componenttypes = (Sprite, )

    def render(self, sprite, x=None, y=None):
        """Draws the passed sprite on the Window's surface."""
        if x is None or y is None:
            x = sprite.x
            y = sprite.y
        r = rect.SDL_Rect(x, y, 0, 0)
        sdlsurface.blit_surface(sprite.surface, None, self.surface, r)
        video.update_window_surface(self.window.window)

    def process(self, world, components):
        """Draws the passed Sprite objects on the Window's surface."""
        r = rect.SDL_Rect(0, 0, 0, 0)
        components = sorted(components, self._sortfunc)
        for sprite in components:
            r.x = sprite.x
            r.y = sprite.y
            sdlsurface.blit_surface(sprite.surface, None, self.surface, r)
        video.update_window_surface(self.window.window)

    @property
    def sortfunc(self):
        """Sort function for the component processing order.

        The default sort order is based on the depth attribute of every
        sprite. Lower depth values will cause sprites to be drawn below
        sprites with higher depth values.
        """
        return self._sortfunc

    @sortfunc.setter
    def sortfunc(self, value):
        if not callable(value):
            raise TypeError("sortfunc must be callable")
        self._sortfunc = value


class Sprite(Component):
    """A simple, visible, pixel-based 2D object."""
    def __init__(self, source=None, size=(0, 0), bpp=32, masks=None,
                 freesf=False):
        """Creates a new Sprite.

        If a source is provided, the constructor assumes it to be a
        readable buffer object or file path to load the pixel data from.
        The size and bpp will be ignored in those cases.

        If no source is provided, a size tuple containing the width and
        height of the sprite and a bpp value, indicating the bits per
        pixel to be used, need to be provided.
        """
        super(Sprite, self).__init__()
        self._freesf = True
        if source is not None:
            if isinstance(source, video.SDL_Surface):
                self.surface = source
                self._freesf = freesf
            elif type(source) is str:
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
            if masks:
                rmask, gmask, bmask, amask = masks
            else:
                rmask = gmask = bmask = amask = 0
            self.surface = sdlsurface.create_rgb_surface(size[0], size[1],
                                                         bpp, rmask, gmask,
                                                         bmask, amask)
        self.depth = 0
        self.x = 0
        self.y = 0

    def __del__(self):
        """Releases the bound SDL_Surface, if it was created by the Sprite."""
        if self._freesf:
            sdlsurface.free_surface(self.surface)
        self.surface = None

    @property
    def size(self):
        """The size of the Sprite as tuple."""
        return self.surface.size

    @property
    def position(self):
        """The top-left position of the Sprite as tuple."""
        return self.x, self.y

    @position.setter
    def position(self, value):
        self.x = value[0]
        self.y = value[1]

    @property
    def area(self):
        """The rectangular area occupied by the Sprite."""
        w, h = self.size
        return (self.x, self.y, self.x + w, self.y + h)
