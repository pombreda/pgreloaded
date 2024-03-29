"""
Wrapper methods around the SDL2 surface routines.
"""
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll, SDL_TRUE, SDLError
from pygame2.sdl.pixels import SDL_PixelFormat, SDL_Palette
from pygame2.sdl.rect import SDL_Rect
import pygame2.sdl.rwops as rwops
import pygame2.array as array

__all__ = ["SDL_Surface", "SDL_MUSTLOCK", "convert_pixels", "convert_surface",
           "convert_surface_format", "create_rgb_surface",
           "create_rgb_surface_from", "fill_rect", "fill_rects",
           "free_surface", "get_clip_rect", "set_clip_rect", "get_color_key",
           "set_color_key", "get_surface_alpha_mod", "set_surface_alpha_mod",
           "set_surface_blend_mode", "get_surface_color_mod",
           "set_surface_color_mod", "lock_surface", "unlock_surface",
           "lower_blit", "lower_blit_scaled", "upper_blit", "blit_surface",
           "upper_blit_scaled", "soft_stretch", "set_surface_palette",
           "set_surface_rle"
           ]

SDL_SWSURFACE = 0
SDL_PREALLOC  = 0x00000001
SDL_RLEACCEL  = 0x00000002
SDL_DONTFREE  = 0x00000004


class SDL_Surface(ctypes.Structure):
    """2D pixel buffer used for software blitting operations."""
    _fields_ = [("_flags", ctypes.c_uint),
                ("_format", ctypes.POINTER(SDL_PixelFormat)),
                ("_w", ctypes.c_int),
                ("_h", ctypes.c_int),
                ("_pitch", ctypes.c_int),
                ("_pixels", ctypes.POINTER(ctypes.c_ubyte)),
                ("_userdata", ctypes.c_void_p),
                ("_locked", ctypes.c_int),
                ("_locked_data", ctypes.c_void_p),
                ("_clip_rect", SDL_Rect),
                ("_map", ctypes.c_void_p),
                ("_refcount", ctypes.c_int)
                ]

    @property
    def flags(self):
        """The flags of the SDL_Surface"""
        return self._flags

    @property
    def size(self):
        """The size of the SDL_Surface."""
        return self._w, self._h

    @property
    def locked(self):
        """Indicates, if the SDL_Surface is locked."""
        return self._locked

    @property
    def locked_data(self):
        """Data that belongs to the lock"""
        return self._locked_data

    @property
    def clip_rect(self):
        """The currently applied clipping area of the SDL_Surface"""
        return self._clip_rect

    @property
    def format(self):
        """The SDL_PixelFormat of the SDL_Surface."""
        if self._format:
            return self._format.contents

    @property
    def pixels(self):
        """The raw pixel buffer as ctypes byte pointer."""
        if SDL_MUSTLOCK(self) and not self._locked:
            raise SDLError("must be locked before accessing the pixels")
        return self._pixels

    @property
    def pitch(self):
        """The pitch of a single pixel row."""
        return self._pitch


@sdltype("SDL_ConvertPixels", [ctypes.c_int, ctypes.c_int, ctypes.c_uint,
                               ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int,
                               ctypes.c_uint, ctypes.POINTER(ctypes.c_ubyte),
                               ctypes.c_int], ctypes.c_int)
def convert_pixels(width, height, srcformat, src, srcpitch, dstformat,
                   dstpitch):
    """Converts the passed pixel pixel buffer and returns a new buffer.

    The pixels of the passed src buffer will be converted from srcformat
    to values of dstformat. The size of the result buffer will be
    height * dstpitch.
    """
    srcp = src
    srcsize = len(src)
    if isinstance(src, array.CTypesView):
        srcp = src.to_bytes()
    else:
        srcp, srcsize = array.to_ctypes(src, ctypes.c_ubyte)
    srcp = ctypes.cast(srcp, ctypes.POINTER(ctypes.c_ubyte))
    dst = (ctypes.c_ubyte * (height * dstpitch))()
    dstp = ctypes.cast(dst, ctypes.POINTER(ctypes.c_ubyte))
    ret = dll.SDL_ConvertPixels(width, height, srcformat, srcp, srcpitch,
                                dstformat, dstp, dstpitch)
    if ret == -1:
        raise SDLError()
    return dst


@sdltype("SDL_ConvertSurface", [ctypes.POINTER(SDL_Surface),
                                ctypes.POINTER(SDL_PixelFormat),
                                ctypes.c_uint], ctypes.POINTER(SDL_Surface))
def convert_surface(src, pformat, flags):
    """Creates a new surface with the specified format and copies and maps the
    passed surface to it.
    """
    ret = dll.SDL_ConvertSurface(ctypes.byref(src), ctypes.byref(pformat),
                                 flags)
    if ret is None or not bool(ret):
        raise SDLError()
    return ret.contents


@sdltype("SDL_ConvertSurfaceFormat", [ctypes.POINTER(SDL_Surface),
                                      ctypes.c_uint, ctypes.c_uint],
         ctypes.POINTER(SDL_Surface))
def convert_surface_format(src, pformat, flags):
    """Creates a new surface with the specified format and copies and maps the
    passed surface to it.
    """
    ret = dll.SDL_ConvertSurfaceFormat(ctypes.byref(src), pformat, flags)
    if ret is None or not bool(ret):
        raise SDLError()
    return ret.contents


@sdltype("SDL_CreateRGBSurface", [ctypes.c_uint, ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_uint, ctypes.c_uint,
                                  ctypes.c_uint, ctypes.c_uint],
         ctypes.POINTER(SDL_Surface))
def create_rgb_surface(width, height, depth, rmask=0, gmask=0, bmask=0,
                       amask=0):
    """Creates a RGB surface.

    If the depth is 4 or 8 bits, an empty palette is allocated for the
    surface. If the depth is greater than 8 bits, the pixel format is set
    using the passed RGBA mask.
    """
    # TODO: this check should be done by SDL
    if width < 0 or height < 0:
        raise ValueError("width and height must not be negative")
    ret = dll.SDL_CreateRGBSurface(0, width, height, depth, rmask, gmask,
                                   bmask, amask)
    if ret is None or not bool(ret):
        raise SDLError()
    return ret.contents


@sdltype("SDL_CreateRGBSurfaceFrom", [ctypes.POINTER(ctypes.c_ubyte),
                                      ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                      ctypes.c_uint, ctypes.c_uint,
                                      ctypes.c_uint, ctypes.c_uint],
         ctypes.POINTER(SDL_Surface))
def create_rgb_surface_from(pixels, width, height, depth, pitch, rmask, gmask,
                            bmask, amask):
    """Creates a RGB surface from a pixel buffer.

    Note: this will add a SDL_Surface._refdata attribute, to which pixels gets
    assigned to. This allows the caller to forget about pixels without actually
    having to manage them elsewhere. The calling code SHOULD NOT FREE pixels
    or otherwise deallocate them, since the SDL_Surface uses pixels as buffer
    backend.

    The referenced pixels will not be deleted automatically on releasing
    the SDL_Surface, either. Hence the caller needs to ensure to free
    pixels properly, once the SDL_Surface has been freed.
    """
    # TODO: this check should be done by SDL
    if width < 0 or height < 0:
        raise ValueError("width and height must not be negative")
    pptr = ctypes.cast(pixels, ctypes.POINTER(ctypes.c_ubyte))
    ret = dll.SDL_CreateRGBSurfaceFrom(pptr, width, height, depth, pitch,
                                       rmask, gmask, bmask, amask)
    if ret is None or not bool(ret):
        raise SDLError()
    ret._refdata = pixels
    return ret.contents


@sdltype("SDL_FillRect", [ctypes.POINTER(SDL_Surface),
                          ctypes.POINTER(SDL_Rect), ctypes.c_uint],
         ctypes.c_int)
def fill_rect(dst, rect, color):
    """Fills an area with a certain color on the surface.

    if rect is None, the entire surface will be filled.
    """
    rptr = None
    if rect is not None:
        rptr = ctypes.byref(rect)
    retval = dll.SDL_FillRect(ctypes.byref(dst), rptr, color)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_FillRects", [ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect), ctypes.c_int,
                           ctypes.c_uint], ctypes.c_int)
def fill_rects(dst, rects, color):
    """Fills multiple areas with a certain color on the surface."""
    rects, count = array.to_ctypes(rects, SDL_Rect)
    rects = ctypes.cast(rects, ctypes.POINTER(SDL_Rect))
    retval = dll.SDL_FillRects(ctypes.byref(dst), rects, count, color)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_FreeSurface", [ctypes.POINTER(SDL_Surface)], None)
def free_surface(surface):
    """Frees the resources hold by a surface.

    Once freed, the surface should not be accessed anymore.
    """
    dll.SDL_FreeSurface(ctypes.byref(surface))


@sdltype("SDL_GetClipRect", [ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(SDL_Rect)], None)
def get_clip_rect(surface):
    """Gets the clipping area for blitting operations.
    """
    rect = SDL_Rect()
    dll.SDL_GetClipRect(ctypes.byref(surface), ctypes.byref(rect))
    return rect


@sdltype("SDL_SetClipRect", [ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def set_clip_rect(surface, rect):
    """Sets the clipping area for blitting operations.
    """
    ret = dll.SDL_SetClipRect(ctypes.byref(surface), ctypes.byref(rect))
    return ret == SDL_TRUE


@sdltype("SDL_GetColorKey", [ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(ctypes.c_uint)], ctypes.c_int)
def get_color_key(surface):
    """Gets the set colorkey for transparent pixels on the surface.

    If no colorkey is set, None will be returned.
    """
    key = ctypes.c_uint()
    ret = dll.SDL_GetColorKey(ctypes.byref(surface), ctypes.byref(key))
    if ret == -1:
        return None
    return key.value


@sdltype("SDL_SetColorKey", [ctypes.POINTER(SDL_Surface), ctypes.c_int,
                             ctypes.c_uint], ctypes.c_int)
def set_color_key(surface, flag, key):
    """Sets the colorkey for transparent pixels on the surface.

    You can pass SDL_RLEACCEL to enable RLE accelerated blits.
    """
    ret = dll.SDL_SetColorKey(ctypes.byref(surface), flag, key)
    if ret != 0:
        raise SDLError()


@sdltype("SDL_GetSurfaceAlphaMod", [ctypes.POINTER(SDL_Surface),
                                    ctypes.POINTER(ctypes.c_ubyte)],
    ctypes.c_int)
def get_surface_alpha_mod(surface):
    """Gets the additional alpha value to be used in blit operations.
    """
    alpha = ctypes.c_ubyte()
    ret = dll.SDL_GetSurfaceAlphaMod(ctypes.byref(surface),
                                     ctypes.byref(alpha))
    if ret == 0:
        return alpha.value
    return None


@sdltype("SDL_SetSurfaceAlphaMod", [ctypes.POINTER(SDL_Surface),
                                    ctypes.c_ubyte], ctypes.c_int)
def set_surface_alpha_mod(surface, alpha):
    """Sets the additional alpha value used in blit operations.
    """
    ret = dll.SDL_SetSurfaceAlphaMod(ctypes.byref(surface), alpha)
    if ret != 0:
        raise SDLError()


@sdltype("SDL_SetSurfaceBlendMode", [ctypes.POINTER(SDL_Surface),
                                     ctypes.c_int], ctypes.c_int)
def set_surface_blend_mode(surface, blend):
    """Sets the blend mode to be used in blit operations.
    """
    ret = dll.SDL_SetSurfaceBlendMode(ctypes.byref(surface), blend)
    if ret != 0:
        raise SDLError()


@sdltype("SDL_GetSurfaceBlendMode", [ctypes.POINTER(SDL_Surface),
                                     ctypes.POINTER(ctypes.c_int)],
         ctypes.c_int)
def get_surface_blend_mode(surface):
    """Gets the blend mode used in blit operations.
    """
    mode = ctypes.c_int()
    ret = dll.SDL_GetSurfaceBlendMode(ctypes.byref(surface),
                                      ctypes.byref(mode))
    if ret != 0:
        raise SDLError()
    return mode.value


@sdltype("SDL_GetSurfaceColorMod", [ctypes.POINTER(SDL_Surface),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte)],
         ctypes.c_int)
def get_surface_color_mod(surface):
    """Gets the additional color value used for blit operations.
    """
    r, g, b = ctypes.c_ubyte(), ctypes.c_ubyte(), ctypes.c_ubyte()
    ret = dll.SDL_GetSurfaceColorMod(ctypes.byref(surface), ctypes.byref(r),
                                     ctypes.byref(g), ctypes.byref(b))
    if ret == 0:
        return(r.value, g.value, b.value)
    return None


@sdltype("SDL_SetSurfaceColorMod", [ctypes.POINTER(SDL_Surface),
                                    ctypes.c_ubyte, ctypes.c_ubyte,
                                    ctypes.c_ubyte], ctypes.c_int)
def set_surface_color_mod(surface, r, g, b):
    """Sets the additional color value to be used for blit operations.
    """
    ret = dll.SDL_SetSurfaceColorMod(ctypes.byref(surface), r, g, b)
    if ret != 0:
        raise SDLError()


@sdltype("SDL_LoadBMP_RW", [ctypes.POINTER(rwops.SDL_RWops), ctypes.c_int],
         ctypes.POINTER(SDL_Surface))
def load_bmp_rw(src, freesrc):
    """Load a surface from a seekable data stream.

    If freesrc evaluates to True, the passed stream will be closed after
    being read.
    """
    if bool(freesrc):
        retval = dll.SDL_LoadBMP_RW(ctypes.byref(src), 1)
    else:
        retval = dll.SDL_LoadBMP_RW(ctypes.byref(src), 0)
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


def load_bmp(filename):
    """Loads a surface from a BMP file.
    """
    rw = rwops.rw_from_file(str(filename), "rb")
    return load_bmp_rw(rw, True)


@sdltype("SDL_SaveBMP_RW", [ctypes.POINTER(SDL_Surface),
                            ctypes.POINTER(rwops.SDL_RWops), ctypes.c_int],
         ctypes.c_int)
def save_bmp_rw(surface, dst, freedst):
    """Saves a surface to a seekable data stream.

    If freedst evaluates to True, the passed stream will be closed after
    being written.
    """
    if bool(freedst):
        retval = dll.SDL_SaveBMP_RW(ctypes.byref(surface), ctypes.byref(dst), 1)
    else:
        retval = dll.SDL_SaveBMP_RW(ctypes.byref(surface), ctypes.byref(dst), 0)
    if retval == -1:
        raise SDLError()


def save_bmp(surface, filename):
    """Saves a surface to a file.
    """
    rw = rwops.rw_from_file(filename, "wb")
    save_bmp_rw(surface, rw, True)


@sdltype("SDL_LockSurface", [ctypes.POINTER(SDL_Surface)], ctypes.c_int)
def lock_surface(surface):
    """Locks the surface to allow a direct acces to its pixels.
    """
    ret = dll.SDL_LockSurface(ctypes.byref(surface))
    if ret != 0:
        raise SDLError()


def SDL_MUSTLOCK(surface):
    """Checks, if the surface must be locked prior to access its
    pixels.
    """
    return (surface._flags & SDL_RLEACCEL) != 0


@sdltype("SDL_UnlockSurface", [ctypes.POINTER(SDL_Surface)], None)
def unlock_surface(surface):
    """Unlocks the surface."""
    dll.SDL_UnlockSurface(ctypes.byref(surface))


@sdltype("SDL_LowerBlit", [ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect),
                           ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def lower_blit(src, srcrect, dst, dstrect):
    """Copy pixels from the source surface to the destination surface
    with now argument or rectangle validation or clipping.
    """
    ret = dll.SDL_LowerBlit(ctypes.byref(src), ctypes.byref(srcrect),
                            ctypes.byref(dst), ctypes.byref(dstrect))
    if ret != 0:
        raise SDLError()


@sdltype("SDL_LowerBlitScaled", [ctypes.POINTER(SDL_Surface),
                                 ctypes.POINTER(SDL_Rect),
                                 ctypes.POINTER(SDL_Surface),
                                 ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def lower_blit_scaled(src, srcrect, dst, dstrect):
    """Performs a scaled pixel copy operation from the source surface to
    the destination surface, without argument checks or clipping.
    """
    ret = dll.SDL_LowerBlitScaled(ctypes.byref(src), ctypes.byref(srcrect),
                                  ctypes.byref(dst), ctypes.byref(dstrect))
    if ret != 0:
        raise SDLError()


@sdltype("SDL_UpperBlit", [ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect),
                           ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def upper_blit(src, srcrect, dst, dstrect):
    """Copy pixels from the source surface to the destination surface,
    performing argument and rectangle validation as well as clipping.
    """
    srptr = None
    if srcrect is not None:
        srptr = ctypes.byref(srcrect)
    ret = dll.SDL_UpperBlit(ctypes.byref(src), srptr,
                            ctypes.byref(dst), ctypes.byref(dstrect))
    if ret != 0:
        raise SDLError()


blit_surface = upper_blit


@sdltype("SDL_UpperBlitScaled", [ctypes.POINTER(SDL_Surface),
                                 ctypes.POINTER(SDL_Rect),
                                 ctypes.POINTER(SDL_Surface),
                                 ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def upper_blit_scaled(src, srcrect, dst, dstrect):
    """Performs a scaled pixel copy operation from the source surface to
    the destination surface, including argument checks and clipping.
    """
    srptr = None
    if srcrect is not None:
        srptr = ctypes.byref(srcrect)
    ret = dll.SDL_UpperBlitScaled(ctypes.byref(src), srptr,
                                  ctypes.byref(dst), ctypes.byref(dstrect))
    if ret != 0:
        raise SDLError()


@sdltype("SDL_SoftStretch", [ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(SDL_Rect),
                             ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def soft_stretch(src, srcrect, dst, dstrect):
    """perform a fast, low quality, stretched copy operation between two
    surfaces of the same pixel format.
    """
    ret = dll.SDL_SoftStretch(ctypes.byref(src), ctypes.byref(srcrect),
                              ctypes.byref(dst), ctypes.byref(dstrect))
    if ret != 0:
        raise SDLError()


@sdltype("SDL_SetSurfacePalette", [ctypes.POINTER(SDL_Surface),
                                   ctypes.POINTER(SDL_Palette)], ctypes.c_int)
def set_surface_palette(surface, palette):
    """Sets the palette used by the surface."""
    pptr = None
    if palette is not None:
        pptr = ctypes.byref(palette)
    ret = dll.SDL_SetSurfacePalette(ctypes.byref(surface), pptr)
    if ret != 0:
        raise SDLError()


@sdltype("SDL_SetSurfaceRLE", [ctypes.POINTER(SDL_Surface), ctypes.c_int],
         ctypes.c_int)
def set_surface_rle(surface, flag):
    """Sets the RLE acceleration hint for the surface.

    If RLE is enabled, colorkey and alpha blending blits are much
    faster, but the surface must be locked before directly accessing the
    pixels.
    """
    if bool(flag):
        ret = dll.SDL_SetSurfaceRLE(ctypes.byref(surface), 1)
    else:
        ret = dll.SDL_SetSurfaceRLE(ctypes.byref(surface), 0)
    if ret != 0:
        raise SDLError()
