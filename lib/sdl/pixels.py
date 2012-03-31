"""
Wrapper methods around the SDL2 pixel routines
"""
import sys
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll, SDL_FALSE, SDL_TRUE
from pygame2.sdl.error import SDLError

SDL_ALPHA_OPAQUE        = 255
SDL_ALPHA_TRANSPARENT   = 0

SDL_PIXELTYPE_UNKNOWN   = 0
SDL_PIXELTYPE_INDEX1    = 1
SDL_PIXELTYPE_INDEX4    = 2
SDL_PIXELTYPE_INDEX8    = 3
SDL_PIXELTYPE_PACKED8   = 4
SDL_PIXELTYPE_PACKED16  = 5
SDL_PIXELTYPE_PACKED32  = 6
SDL_PIXELTYPE_ARRAYU8   = 7
SDL_PIXELTYPE_ARRAYU16  = 8
SDL_PIXELTYPE_ARRAYU32  = 9
SDL_PIXELTYPE_ARRAYF16  = 10
SDL_PIXELTYPE_ARRAYF32  = 11

SDL_BITMAPORDER_NONE = 0
SDL_BITMAPORDER_4321 = 1
SDL_BITMAPORDER_1234 = 2

SDL_PACKEDORDER_NONE = 0
SDL_PACKEDORDER_XRGB = 1
SDL_PACKEDORDER_RGBX = 2
SDL_PACKEDORDER_ARGB = 3
SDL_PACKEDORDER_RGBA = 4
SDL_PACKEDORDER_XBGR = 5
SDL_PACKEDORDER_BGRX = 6
SDL_PACKEDORDER_ABGR = 7
SDL_PACKEDORDER_BGRA = 8

SDL_ARRAYORDER_NONE = 0
SDL_ARRAYORDER_RGB  = 1
SDL_ARRAYORDER_RGBA = 2
SDL_ARRAYORDER_ARGB = 3
SDL_ARRAYORDER_BGR  = 4
SDL_ARRAYORDER_BGRA = 5
SDL_ARRAYORDER_ABGR = 6

SDL_PACKEDLAYOUT_NONE       = 0
SDL_PACKEDLAYOUT_332        = 1
SDL_PACKEDLAYOUT_4444       = 2
SDL_PACKEDLAYOUT_1555       = 3
SDL_PACKEDLAYOUT_5551       = 4
SDL_PACKEDLAYOUT_565        = 5
SDL_PACKEDLAYOUT_8888       = 6
SDL_PACKEDLAYOUT_2101010    = 7
SDL_PACKEDLAYOUT_1010102    = 8

def SDL_FOURCC (a, b, c, d):
    """SDL_FOURCC (a, b, c, d) -> int
    SDL_DEFINE_PIXELFOURCC (a, b, c, d) -> int

    Calculates the four character code ordinal value of the passed
    characters.
    """
    return (ord(a) << 0) | (ord(b) << 8) | (ord(c) << 16) | (ord(d) << 24)
SDL_DEFINE_PIXELFOURCC = SDL_FOURCC

def SDL_DEFINE_PIXELFORMAT (type, order, layout, bits, bytes):
    """SDL_DEFINE_PIXELFORMAT (type, order, layout, bits, bytes) -> int

    Calculates a unique pixel format identifier based on the passed values.
    """
    return ((1 << 31) | ((type) << 24) | ((order) << 20) | ((layout) << 16) | \
        ((bits) << 8) | ((bytes) << 0))

def SDL_PIXELTYPE (x):
    """SDL_PIXELTYPE (x) -> int

    Determines the SDL_PIXELTYPE_* value for the passed format value.
    """
    return (((x) >> 24) & 0x0F)

def SDL_PIXELORDER (x):
    """SDL_PIXELORDER (x) -> int

    Determines the pixel order value for the passed format value. The
    return value will be one of (SDL_ARRAYORDER_*, SDL_PACKEDORDER_* or
    SDL_BITMAPORDER_*)
    """
    return (((x) >> 20) & 0x0F)

def SDL_PIXELLAYOUT (x):
    """SDL_PIXELLAYOUT (x) -> int

    Determines the SDL_PACKEDLAYOUT_* value for the passed format value.
    """
    return (((x) >> 16) & 0x0F)

def SDL_BITSPERPIXEL (x):
    """SDL_BITSPERPIXEL (x) -> int

    Determines the bits per pixel for the passed format value.
    """
    return (((x) >> 8) & 0xFF)

def SDL_BYTESPERPIXEL (x):
    """SDL_BYTESPERPIXEL (x) -> int

    Determines the bytes per pixel for the passed format value.
    """
    valid = (SDL_PIXELFORMAT_YUY2, SDL_PIXELFORMAT_UYVY, SDL_PIXELFORMAT_YVYU)
    if SDL_ISPIXELFORMAT_FOURCC (x):
        if x in valid:
            return 2
        else:
            return 1
    else:
        return (((x) >> 0) & 0xFF)

def SDL_ISPIXELFORMAT_INDEXED (format):
    """SDL_ISPIXELFORMAT_INDEXED (format) -> bool

    Checks, if the passed format value is an indexed format
    """
    return ((SDL_ISPIXELFORMAT_FOURCC (format) == False) and
            ((SDL_PIXELTYPE(format) == SDL_PIXELTYPE_INDEX1) or
             (SDL_PIXELTYPE(format) == SDL_PIXELTYPE_INDEX4) or
             (SDL_PIXELTYPE(format) == SDL_PIXELTYPE_INDEX8)))

def SDL_ISPIXELFORMAT_ALPHA (format):
    """SDL_ISPIXELFORMAT_ALPHA (format) -> bool

    Checks, if the passed format value is an alpha channel supporting format.
    """
    return ((SDL_ISPIXELFORMAT_FOURCC (format) == False) and
            ((SDL_PIXELORDER(format) == SDL_PACKEDORDER_ARGB) or
             (SDL_PIXELORDER(format) == SDL_PACKEDORDER_RGBA) or
             (SDL_PIXELORDER(format) == SDL_PACKEDORDER_ABGR) or
             (SDL_PIXELORDER(format) == SDL_PACKEDORDER_BGRA)))

def SDL_ISPIXELFORMAT_FOURCC (format):
    """SDL_ISPIXELFORMAT_FOURCC (format) -> bool

    Checks, if the passed format value is a FourCC based format.
    """
    return ((format != 0) and ((format) & 0x80000000 == 0))

SDL_PIXELFORMAT_UNKNOWN = 0
SDL_PIXELFORMAT_INDEX1LSB = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX1, SDL_BITMAPORDER_4321, 0, 1, 0)
SDL_PIXELFORMAT_INDEX1MSB = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX1, SDL_BITMAPORDER_1234, 0, 1, 0)
SDL_PIXELFORMAT_INDEX4LSB = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX4, SDL_BITMAPORDER_4321, 0, 4, 0)
SDL_PIXELFORMAT_INDEX4MSB = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX4, SDL_BITMAPORDER_1234, 0, 4, 0)
SDL_PIXELFORMAT_INDEX8 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_INDEX8, 0, 0, 8, 1)
SDL_PIXELFORMAT_RGB332 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED8, SDL_PACKEDORDER_XRGB, SDL_PACKEDLAYOUT_332, 8, 1)
SDL_PIXELFORMAT_RGB444 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XRGB, SDL_PACKEDLAYOUT_4444, 12, 2)
SDL_PIXELFORMAT_RGB555 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XRGB, SDL_PACKEDLAYOUT_1555, 15, 2)
SDL_PIXELFORMAT_BGR555 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XBGR, SDL_PACKEDLAYOUT_1555, 15, 2)
SDL_PIXELFORMAT_ARGB4444 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_ARGB, SDL_PACKEDLAYOUT_4444, 16, 2)
SDL_PIXELFORMAT_RGBA4444 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_RGBA, SDL_PACKEDLAYOUT_4444, 16, 2)
SDL_PIXELFORMAT_ABGR4444 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_ABGR, SDL_PACKEDLAYOUT_4444, 16, 2)
SDL_PIXELFORMAT_BGRA4444 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_BGRA, SDL_PACKEDLAYOUT_4444, 16, 2)
SDL_PIXELFORMAT_ARGB1555 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_ARGB, SDL_PACKEDLAYOUT_1555, 16, 2)
SDL_PIXELFORMAT_RGBA5551 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_RGBA, SDL_PACKEDLAYOUT_5551, 16, 2)
SDL_PIXELFORMAT_ABGR1555 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_ABGR, SDL_PACKEDLAYOUT_1555, 16, 2)
SDL_PIXELFORMAT_BGRA5551 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_BGRA, SDL_PACKEDLAYOUT_5551, 16, 2)
SDL_PIXELFORMAT_RGB565 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XRGB, SDL_PACKEDLAYOUT_565, 16, 2)
SDL_PIXELFORMAT_BGR565 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED16, SDL_PACKEDORDER_XBGR, SDL_PACKEDLAYOUT_565, 16, 2)
SDL_PIXELFORMAT_RGB24 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU8, SDL_ARRAYORDER_RGB, 0, 24, 3)
SDL_PIXELFORMAT_BGR24 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_ARRAYU8, SDL_ARRAYORDER_BGR, 0, 24, 3)
SDL_PIXELFORMAT_RGB888 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_XRGB, SDL_PACKEDLAYOUT_8888, 24, 4)
SDL_PIXELFORMAT_RGBX8888 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_RGBX, SDL_PACKEDLAYOUT_8888, 24, 4)
SDL_PIXELFORMAT_BGR888 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_XBGR, SDL_PACKEDLAYOUT_8888, 24, 4)
SDL_PIXELFORMAT_BGRX8888 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_BGRX, SDL_PACKEDLAYOUT_8888, 24, 4)
SDL_PIXELFORMAT_ARGB8888 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_ARGB, SDL_PACKEDLAYOUT_8888, 32, 4)
SDL_PIXELFORMAT_RGBA8888 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_RGBA, SDL_PACKEDLAYOUT_8888, 32, 4)
SDL_PIXELFORMAT_ABGR8888 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_ABGR, SDL_PACKEDLAYOUT_8888, 32, 4)
SDL_PIXELFORMAT_BGRA8888 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_BGRA, SDL_PACKEDLAYOUT_8888, 32, 4)
SDL_PIXELFORMAT_ARGB2101010 = SDL_DEFINE_PIXELFORMAT(SDL_PIXELTYPE_PACKED32, SDL_PACKEDORDER_ARGB, SDL_PACKEDLAYOUT_2101010, 32, 4)
SDL_PIXELFORMAT_YV12 = SDL_DEFINE_PIXELFOURCC('Y', 'V', '1', '2')
SDL_PIXELFORMAT_IYUV = SDL_DEFINE_PIXELFOURCC('I', 'Y', 'U', 'V')
SDL_PIXELFORMAT_YUY2 = SDL_DEFINE_PIXELFOURCC('Y', 'U', 'Y', '2')
SDL_PIXELFORMAT_UYVY = SDL_DEFINE_PIXELFOURCC('U', 'Y', 'V', 'Y')
SDL_PIXELFORMAT_YVYU = SDL_DEFINE_PIXELFOURCC('Y', 'V', 'Y', 'U')

class SDL_Color (ctypes.Structure):
    """SDL_Color (r=255, g=255, b=255) -> SDL_Color
    SDL_Colour (r=255, g=255, b=255) -> SDL_Color

    A simple RGB color class.
    """
    _fields_ = [("r", ctypes.c_ubyte),
                ("g", ctypes.c_ubyte),
                ("b", ctypes.c_ubyte),
                ("_unused", ctypes.c_ubyte),
                ]
    def __init__ (self, r=255, g=255, b=255):
        self.r = r
        self.g = g
        self.b = b
        self._unused = 0
    
    def __repr__ (self):
        return "SDL_Color (r=%d, g=%d, b=%d)" % (self.r, self.g, self.b)
    
    def __copy__ (self):
        return SDL_Color (self.r, self.g, self.b)

    def __deepcopy__ (self, memo):
        return SDL_Color (self.r, self.g, self.b)

    def __eq__ (self, color):
        return self.r == color.r and self.g == color.g and self.b == color.b

    def __ne__ (self, color):
        return self.r != color.r or self.g != color.g or self.b != color.b

SDL_Colour = SDL_Color

class SDL_Palette (ctypes.Structure):
    """SDL_Plalette () -> SDL_Palette

    A color palette class.
    """
    _fields_ = [("ncolors", ctypes.c_int),
                ("_colors", ctypes.POINTER(SDL_Color)),
                ("version", ctypes.c_uint),
                ("_refcount", ctypes.c_int),
                ]
    
    @property
    def colors (self):
        """Get the colors of the SDL_Palette."""
        if not hasattr (self, "_ctcolors"):
            self._ctcolors = ctypes.cast (self._colors,
                ctypes.POINTER(self.ncolors * SDL_Color)).contents
        return self._ctcolors

class SDL_PixelFormat (ctypes.Structure):
    """SDL_PixelFormat () -> SDL_PixelFormat

    A SDL pixel format class.
    """
    @property
    def palette (self):
        """Get the assigned SDL_Palette."""
        if self._palette:
            return self._palette.contents
        return None

    @property
    def next (self):
        """Get the next format linked to this."""
        if self._next:
            return self._next.contents
        return None
    
    def __copy__ (self):
        format = SDL_PixelFormat()
        format.format = self.format
        format._palette = self._palette
        format.BitsPerPixel = self.BitsPerPixel
        format.BytesPerPixel = self.BytesPerPixel
        format.padding = self.padding
        format.Rloss = self.Rloss
        format.Gloss = self.Gloss
        format.Bloss = self.Bloss
        format.Aloss = self.Aloss
        format.Rshift = self.Rshift
        format.Gshift = self.Gshift
        format.Bshift = self.Bshift
        format.Ashift = self.Ashift
        format.Rmask = self.Rmask
        format.Gmask = self.Gmask
        format.Bmask = self.Bmask
        format.Amask = self.Amask
        format._next = self._next
        return format
    
SDL_PixelFormat._fields_ = [("format", ctypes.c_uint),
                            ("_palette", ctypes.POINTER(SDL_Palette)),
                            ("BitsPerPixel", ctypes.c_ubyte),
                            ("BytesPerPixel", ctypes.c_ubyte),
                            ("_padding", ctypes.c_ubyte * 2),
                            ("Rmask", ctypes.c_uint),
                            ("Gmask", ctypes.c_uint),
                            ("Bmask", ctypes.c_uint),
                            ("Amask", ctypes.c_uint),
                            ("Rloss", ctypes.c_ubyte),
                            ("Gloss", ctypes.c_ubyte),
                            ("Bloss", ctypes.c_ubyte),
                            ("Aloss", ctypes.c_ubyte),
                            ("Rshift", ctypes.c_ubyte),
                            ("Gshift", ctypes.c_ubyte),
                            ("Bshift", ctypes.c_ubyte),
                            ("Ashift", ctypes.c_ubyte),
                            ("_refcount", ctypes.c_int),
                            ("_next", ctypes.POINTER(SDL_PixelFormat)),
                            ]
    
@sdltype("SDL_GetPixelFormatName", [ctypes.c_uint], ctypes.c_char_p)
def get_pixelformat_name (format):
    """get_pixelformat_name (format) -> str

    Gets the name of a specific pixel format value.
    """
    retval = dll.SDL_GetPixelFormatName (format)
    return stringify (retval, "utf-8")

@sdltype("SDL_PixelFormatEnumToMasks", [ctypes.c_uint,
                                        ctypes.POINTER(ctypes.c_int),
                                        ctypes.POINTER(ctypes.c_uint),
                                        ctypes.POINTER(ctypes.c_uint),
                                        ctypes.POINTER(ctypes.c_uint),
                                        ctypes.POINTER(ctypes.c_uint)],
         ctypes.c_int)
def pixelformat_enum_to_masks (format):
    """pixelformat_enum_to_masks (format) -> (int, int, int, int, int)

    Gets the pixel masks for a specific pixel format value.

    The returned tuple consists of (bpp, red mask, green mask, blue mask,
    alpha mask).
    """
    bpp = ctypes.c_int ()
    rmask = ctypes.c_uint ()
    gmask = ctypes.c_uint ()
    bmask = ctypes.c_uint ()
    amask = ctypes.c_uint ()
    if dll.SDL_PixelFormatEnumToMasks (format, ctypes.byref(bpp),
                                       ctypes.byref(rmask), ctypes.byref(gmask),
                                       ctypes.byref(bmask),
                                       ctypes.byref(amask)) == SDL_TRUE:
        return (bpp.value, rmask.value, gmask.value, bmask.value, amask.value)
    raise SDLError ()

@sdltype("SDL_MasksToPixelFormatEnum", [ctypes.c_int, ctypes.c_uint,
                                        ctypes.c_uint, ctypes.c_uint,
                                        ctypes.c_uint],
         ctypes.c_uint)
def masks_to_pixelformat_enum (bpp, rmask, gmask, bmask, amask):
    """masks_to_pixelformat_enum (bpp, rmask, gmask, bmask, amask) -> int

    Gets the format for a set of pixel mask information.
    """
    return dll.SDL_MasksToPixelFormatEnum (bpp, rmask, gmask, bmask, amask)

@sdltype("SDL_AllocFormat", [ctypes.c_uint], ctypes.POINTER(SDL_PixelFormat))
def alloc_format (format):
    """alloc_format (format) -> SDL_PixelFormat

    Creates a SDL_PixelFormat from the passed format value.

    In case the passed format value is not valid or an error occurs on
    creation, a SDLError is raised.

    Once not used anymore, the SDL_PixelFormat must be freed using
    free_format().
    """    
    fmt = dll.SDL_AllocFormat (format)
    if not bool (fmt):
        raise SDLError ()
    return fmt.contents

@sdltype("SDL_FreeFormat", [ctypes.POINTER(SDL_PixelFormat)], None)
def free_format (format):
    """free_format (format) -> None

    Frees a previously allocated SDL_PixelFormat.
    """
    if type (format) is not SDL_PixelFormat:
        raise TypeError ("format must be a SDL_PixelFormat")
    dll.SDL_FreeFormat (ctypes.byref(format))

@sdltype("SDL_AllocPalette", [ctypes.c_int], ctypes.POINTER(SDL_Palette))
def alloc_palette (ncolors):
    """alloc_palette (ncolors) -> SDL_Palette

    Creates a SDL_palette with ncolors number of colors.

    Once not used anymore, the SDL_Palette must be freed using
    free_palette().
    """
    if type (ncolors) is not int:
        raise TypeError ("ncolors must be an int")
    if ncolors < 0:
        raise ValueError ("ncolors must not be smaller than 0")
    palette = dll.SDL_AllocPalette (ncolors)
    return palette.contents

@sdltype("SDL_FreePalette", [ctypes.POINTER(SDL_Palette)], None)
def free_palette (palette):
    """free_palette (palette) -> None

    Frees a previously allocated SDL_Palette.
    """
    if type (palette) is not SDL_Palette:
        raise TypeError ("palette must be a SDL_Palette")
    dll.SDL_FreePalette (ctypes.byref(palette))

@sdltype("SDL_CalculateGammaRamp", [ctypes.c_float,
                                    ctypes.POINTER(ctypes.c_ushort)], None)
def calculate_gamma_ramp (gamma):
    """calculate_gamma_ramp (gamma) -> (int, int, ...)

    Calculates a set of 256 gamma values for a value in the range [0.0; 1.0].
    """
    if type (gamma) not in (float, int):
        raise TypeError ("gamma must be a float")
    gamme = float (gamma)
    if gamma < 0.0 or gamma > 1.0:
        raise ValueError ("gamma must be in the range [0.0; 1.0]")
    result = (ctypes.c_ushort * 256)()
    dll.SDL_CalculateGammaRamp (ctypes.c_float(gamma), ctypes.byref(result))
    return result

@sdltype("SDL_GetRGB", [ctypes.c_uint, ctypes.POINTER(SDL_PixelFormat),
                        ctypes.POINTER(ctypes.c_ubyte),
                        ctypes.POINTER(ctypes.c_ubyte),
                        ctypes.POINTER(ctypes.c_ubyte)], None)
def get_rgb (pixel, format):
    """get_rgb (pixel, format) -> (int, int, int)

    Gets the mapped RGB values for a specific pixel value and format.
    """
    if type (pixel) not in (int, long):
        raise TypeError ("pixel must be an int")
    if type (format) is not SDL_PixelFormat:
        raise TypeError ("format must be a SDL_PixelFormat")
    r = ctypes.c_ubyte()
    g = ctypes.c_ubyte()
    b = ctypes.c_ubyte()
    dll.SDL_GetRGB (pixel, ctypes.byref(format), ctypes.byref(r),
                    ctypes.byref(g), ctypes.byref(b))
    return (r.value, g.value, b.value)

@sdltype("SDL_GetRGBA", [ctypes.c_uint, ctypes.POINTER(SDL_PixelFormat),
                         ctypes.POINTER(ctypes.c_ubyte),
                         ctypes.POINTER(ctypes.c_ubyte),
                         ctypes.POINTER(ctypes.c_ubyte),
                         ctypes.POINTER(ctypes.c_ubyte)], None)
def get_rgba (pixel, format):
    """get_rgba (pixel, format) -> (int, int, int, int)

    Gets the mapped RGBA values for a specific pixel value and format.
    """
    if type (pixel) not in (int, long):
        raise TypeError ("pixel must be an int")
    if type (format) is not SDL_PixelFormat:
        raise TypeError ("format must be a SDL_PixelFormat")
    r = ctypes.c_ubyte()
    g = ctypes.c_ubyte()
    b = ctypes.c_ubyte()
    a = ctypes.c_ubyte()
    dll.SDL_GetRGBA (pixel, ctypes.byref(format), ctypes.byref(r),
                     ctypes.byref(g), ctypes.byref(b), ctypes.byref(a))
    return (r.value, g.value, b.value, a.value)

@sdltype("SDL_MapRGB", [ctypes.POINTER(SDL_PixelFormat), ctypes.c_ubyte,
                        ctypes.c_ubyte, ctypes.c_ubyte], ctypes.c_uint)
def map_rgb (format, r, g, b):
    """map_rgb (format, r, g, b) -> int

    Maps the passed RGB values to a specific pixel value using the
    passed format.
    """
    if type (r) is not int or type (g) is not int or type (b) is not int:
        raise TypeError ("r, g and b must be int values")
    if type (format) is not SDL_PixelFormat:
        raise TypeError ("format must be a SDL_PixelFormat")
    val = dll.SDL_MapRGB (ctypes.byref(format), r, g, b)
    return val

@sdltype("SDL_MapRGBA", [ctypes.POINTER(SDL_PixelFormat), ctypes.c_ubyte,
                         ctypes.c_ubyte, ctypes.c_ubyte, ctypes.c_ubyte],
         ctypes.c_uint)
def map_rgba (format, r, g, b, a):
    """map_rgba (format, r, g, b, a) -> int

    Maps the passed RGBA values to a specific pixel value using the
    passed format.
    """
    if type (r) is not int or type (g) is not int or type (b) is not int or \
            type (a) is not int:
        raise TypeError ("r, g, b and a must be int values")
    if type (format) is not SDL_PixelFormat:
        raise TypeError ("format must be a SDL_PixelFormat")
    val = dll.SDL_MapRGBA (ctypes.byref(format), r, g, b, a)
    return val

@sdltype("SDL_SetPaletteColors", [ctypes.POINTER(SDL_Palette),
                                  ctypes.POINTER(SDL_Color), ctypes.c_int,
                                  ctypes.c_int], ctypes.c_int)
def set_palette_colors (palette, colors, first, ncolors):
    """set_palette_colors (palette, colors, first, ncolors) -> int

    Sets the colors of a SDL_Palette to the passed values, starting at
    first in the colors array and setting ncolors.
    """
    if type (palette) is not SDL_Palette:
        raise TypeError ("palette must be a SDL_Palette")
    if type (first) is not int:
        raise TypeError ("first must be an int")
    if type (ncolors) is not int:
        raise TypeError ("ncolors must be an int")
    return dll.SDL_SetPaletteColors(palette, colors, first, ncolors)

@sdltype("SDL_SetPixelFormatPalette", [ctypes.POINTER(SDL_PixelFormat),
                                       ctypes.POINTER(SDL_Palette)],
         ctypes.c_int)
def set_pixelformat_palette (format, palette):
    """set_pixelformat_palette (format, palette) -> int

    Binds a palette to the passed SDL_PixelFormat.
    """
    if type (format) is not SDL_PixelFormat:
        raise TypeError ("format must be a SDL_PixelFormat")
    if type (palette) is not SDL_Palette:
        raise TypeError ("palette must be a SDL_Palette")
    return dll.SDL_SetPixelFormatPalette (ctypes.byref(format),
                                          ctypes.byref(palette))
