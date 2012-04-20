"""Sprite, texture and pixel surface routines
."""
import os
from pygame2.ebs import Component, System
import pygame2.sdl.surface as sdlsurface
import pygame2.sdl.rect as rect
import pygame2.sdl.video as video
import pygame2.sdl.rwops as rwops


class SpriteRenderer(System):
    """TODO"""
    def __init__(self, window):
        self.window = window
        self.surface = video.get_window_surface(window.window)

    def render(self, sprite):
        r = rect.SDL_Rect(sprite.x, sprite.y, 0, 0)
        sdlsurface.blit_surface(sprite.surface, None, self.surface, r)
        video.update_window_surface(self.window.window)

    def process(self, world, components):
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

        TODO
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
