"""Image loaders."""
from pygame2.compat import UnsupportedError, experimental
from pygame2.sdl.endian import SDL_BYTEORDER, SDL_LIL_ENDIAN
import pygame2.sdl.surface as sdlsurface
import pygame2.sdl.pixels as sdlpixels
from . import sprite

_HASPIL = True
try:
    from PIL import Image
except ImportError:
    _HASPIL = False

_HASSDLIMAGE = True
try:
    import pygame2.sdlimage as sdlimage
except ImportError:
    _HASSDLIMAGE = False

__all__ = ["get_image_formats", "load_image"]


def get_image_formats():
    """Gets the formats supported by pygame2 in the default
    installation.
    """
    return ("bmp", "cur", "gif", "ico", "jpg", "lbm", "pbm", "pcx", "pgm",
            "png", "pnm", "ppm", "tga", "tif", "webp", "xcf", "xpm")


def load_image(fname, assurface=False, enforce=None):
    """Creates a Sprite from an image file.

    If assurface is True, an SDL_Surface will be returned instead of a Sprite
    object.

    This function makes use of the Python Imaging Library, if it is available
    on the target execution environment. The function will try to load the
    file via pygame2.sdlimage first. If the file could not be looaded, it will
    try to load it via PIL.

    You can force the function to use only one of them, by passing the enforce
    as either "PIL" or "SDL".

    Note: This will call pygame2.sdlimage.init() implicitly with the
    default arguments, if the module is available.
    """
    if enforce is not None and enforce not in ("PIL", "SDL"):
        raise ValueError("enforce must be either 'PIL' or 'SDL', if set")

    surface = None
    if enforce != "PIL" and _HASSDLIMAGE:
        try:
            sdlimage.init()
            surface = sdlimage.load(fname)
        except:
            # An error occured - if we do not try PIL, break out now
            if not _HASPIL or enforce == "SDL":
                raise

    if enforce != "SDL" and _HASPIL and surface is None:
        image = Image.open(fname)
        mode = image.mode
        width, height = image.size
        rmask = gmask = bmask = amask = 0
        if mode in ("1", "L", "P"):
            # 1 = B/W, 1 bit per byte
            # "L" = greyscale, 8-bit
            # "P" = palette-based, 8-bit
            pitch = width
            depth = 8
        elif mode in ("I", "F"):
            # 32-bit signed integer or float
            # TODO
            raise TypeError("unsupported image format")
        elif mode == "RGB":
            # 3x8-bit, 24bpp
            if SDL_BYTEORDER == SDL_LIL_ENDIAN:
                rmask = 0x0000FF
                gmask = 0x00FF00
                bmask = 0xFF0000
            else:
                rmask = 0xFF0000
                gmask = 0x00FF00
                bmask = 0x0000FF
            depth = 24
            pitch = width * 3
        elif mode in ("RGBA", "RGBX"):
            # RGBX: 4x8-bit, no alpha
            # RGBA: 4x8-bit, alpha
            if SDL_BYTEORDER == SDL_LIL_ENDIAN:
                rmask = 0x000000FF
                gmask = 0x0000FF00
                bmask = 0x00FF0000
                if mode == "RGBA":
                    amask = 0xFF000000
            else:
                rmask = 0xFF000000
                gmask = 0x00FF0000
                bmask = 0x0000FF00
                if mode == "RGBA":
                    amask = 0x000000FF
            depth = 32
            pitch = width * 4
        else:
            # We do not support CMYK or YCbCr for now
            raise TypeError("unsupported image format")

        pxbuf = image.tostring()
        surface = sdlsurface.create_rgb_surface_from(pxbuf, width, height,
                                                     depth, pitch, rmask,
                                                     gmask, bmask, amask)

        if mode == "P":
            # Create a SDL_Palette for the SDL_Surface
            def _chunk(seq, size):
                for x in range(0, len(seq), size):
                    yield seq[x:x + size]

            rgbcolors = image.getpalette()
            sdlpalette = sdlpixels.alloc_palette(len(rgbcolors) // 3)
            SDL_Color = sdlpixels.SDL_Color
            for idx, (r, g, b) in enumerate(_chunk(rgbcolors, 3)):
                sdlpalette.colors[idx] = SDL_Color(r, g, b)

            try:
                sdlsurface.set_surface_palette(surface, sdlpalette)
            except:
                sdlsurface.free_surface(surface)
                raise
            finally:
                # This will decrease the refcount on the palette, so it gets
                # freed properly on releasing the SDL_Surface.
                sdlpixels.free_palette(sdlpalette)
    if assurface:
        return surface
    else:
        return sprite.Sprite(source=surface, freesf=True)
