"""Drawing routines."""
from pygame2.compat import *
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
        pformat = sprite.surface.format
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
        rtarget = targt.surface

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
