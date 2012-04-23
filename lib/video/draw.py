"""Drawing routines."""

from pygame2.color import convert_to_color
import pygame2.sdl.surface as sdlsurface
import pygame2.sdl.pixels as sdlpixels
from . import sprite

__all__ = ["prepare_color"]


def prepare_color(color, target):
    """Prepares the passed color for the passed target.
    """
    color = convert_to_color(color)
    if isinstance(target, sdlpixels.SDL_PixelFormat):
        return sdlpixels.map_rgb(target, color.r, color.g, color.b)
    if isinstance(target, sdlsurface.SDL_Surface):
        return sdlpixels.map_rgb(target.format, color.r, color.g, color.b)
    if isinstance(target, sprite.Sprite):
        return sdlpixels.map_rgb(sprite.surface.format, color.r, color.g,
                                 color.b)
    raise ValueError("unsupported target")
