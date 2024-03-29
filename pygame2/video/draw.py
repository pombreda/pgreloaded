"""Drawing routines for software surfaces."""
import ctypes
from pygame2.compat import isiterable, UnsupportedError
from pygame2.color import convert_to_color
import pygame2.sdl.surface as sdlsurface
import pygame2.sdl.pixels as sdlpixels
import pygame2.sdl.rect as rect
from pygame2.algorithms import clipline
from pygame2.video.sprite import SoftwareSprite

__all__ = ["prepare_color", "fill", "line"]


def _get_target_surface(target):
    """Gets the SDL_surface from the passed target."""
    if isinstance(target, sdlsurface.SDL_Surface):
        rtarget = target
    elif isinstance(target, SoftwareSprite):
        rtarget = target.surface
    else:
        raise TypeError("unsupported target type")
    return rtarget


def prepare_color(color, target):
    """Prepares the passed color for the passed target.
    """
    color = convert_to_color(color)
    pformat = None
    # Software surfaces
    if isinstance(target, sdlpixels.SDL_PixelFormat):
        pformat = target
    elif isinstance(target, sdlsurface.SDL_Surface):
        pformat = target.format
    elif isinstance(target, SoftwareSprite):
        pformat = target.surface.format
    if pformat is None:
        raise TypeError("unsupported target type")
    if pformat.Amask != 0:
        # Target has an alpha mask
        return sdlpixels.map_rgba(pformat, color.r, color.g, color.b, color.a)
    return sdlpixels.map_rgb(pformat, color.r, color.g, color.b)


def fill(target, color, area=None):
    """Fills a certain rectangular area on the passed target with a color.

    If no area is provided, the entire target will be filled with
    the passed color. If an iterable item is provided as area (such as a list
    or tuple), it will be first checked, if the item denotes a single
    rectangular area (4 integer values) before assuming it to be a sequence
    of rectangular areas.
    """
    color = prepare_color(color, target)
    rtarget = _get_target_surface(target)

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


def line(target, color, line, width=1):
    """Draws one or multiple lines on the passed target.

    line can be a sequence of four integers for a single line in the
    form (x1, y1, x2, y2) or a sequence of a multiple of 4 for drawing
    multiple lines at once, e.g. (x1, y1, x2, y2, x3, y3, x4, y4, ...).
    """
    if width < 1:
        raise ValueError("width must be greater than 0")
    color = prepare_color(color, target)
    rtarget = _get_target_surface(target)

    # line: (x1, y1, x2, y2) OR (x1, y1, x2, y2, ...)
    if (len(line) % 4) != 0:
        raise ValueError("line does not contain a valid set of points")
    pcount = len(line)
    SDLRect = rect.SDL_Rect
    fillrect = sdlsurface.fill_rect

    pitch = rtarget.pitch
    bpp = rtarget.format.BytesPerPixel
    clip_rect = rtarget.clip_rect
    left, right = clip_rect.x, clip_rect.x + clip_rect.w
    top, bottom = clip_rect.y, clip_rect.y + clip_rect.h

    if bpp == 3:
        raise UnsupportedError("24bpp are currently not supported")
    if bpp == 2:
        pxbuf = ctypes.cast(rtarget.pixels, ctypes.POINTER(ctypes.c_uint16))
    elif bpp == 4:
        pxbuf = ctypes.cast(rtarget.pixels, ctypes.POINTER(ctypes.c_uint32))
    else:
        pxbuf = rtarget.pixels  # byte-wise access.

    for idx in range(0, pcount, 4):
        x1, y1, x2, y2 = line[idx:idx + 4]
        if x1 == x2:
            # Vertical line
            yh = abs(y2 - y1)
            varea = SDLRect(x1 - width // 2, y1, width, yh)
            fillrect(rtarget, varea, color)
            continue
        if y1 == y2:
            # Horizontal line
            xw = abs(x2 - x1)
            varea = SDLRect(x1, y1 - width // 2, xw, width)
            fillrect(rtarget, varea, color)
            continue
        if width != 1:
            raise UnsupportedError
        if width == 1:
            # Bresenham
            x1, y1, x2, y2 = clipline(left, top, right, bottom, x1, y1, x2, y2)
            if x1 is None:
                # not to be drawn
                continue
            dx = abs(x2 - x1)
            dy = abs(y2 - y1)
            err = dx - dy
            sx, sy = 1, 1
            if x1 > x2:
                sx = -sx
            if y1 > y2:
                sy = -sy
            mx = sx
            my = sy * pitch / bpp

            pxoff = y1 * pitch / bpp + x1
            while True:
                pxbuf[pxoff] = color
                if x1 == x2 and y1 == y2:
                    break
                de = 2 * err
                if de > - dy:
                    err -= dy
                    x1 += sx
                    pxoff += mx
                if de < dx:
                    err += dx
                    y1 += sy
                    pxoff += my
