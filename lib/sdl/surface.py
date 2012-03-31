"""
Wrapper methods around the SDL2 surface routines.
"""
import ctypes
from pygame2.sdl import sdltype, dll, SDL_FALSE, SDL_TRUE
from pygame2.sdl.pixels import SDL_PixelFormat, SDL_Palette
from pygame2.sdl.rect import SDL_Rect
from pygame2.sdl.error import SDLError

class SDL_Surface (ctypes.Structure):
    """
    """
    _fields_ = [("flags", ctypes.c_uint),
                ("format", ctypes.POINTER(SDL_PixelFormat)),
                ("w", ctypes.c_int),
                ("h", ctypes.c_int),
                ("pitch", ctypes.c_int),
                ("pixels", ctypes.POINTER(ctypes.c_ubyte)),
                ("userdata", ctypes.c_void_p),
                ("_locked", ctypes.c_int),
                ("_locked_data", ctypes.c_void_p),
                ("_clip_rect", SDL_Rect),
                ("_map", ctypes.c_void_p),
                ("_refcount", ctypes.c_int)
                ]
    @property
    def locked (self):
        return self._locked
    
    @property
    def locked_data (self):
        return self._locked_data
    
    @property
    def clip_rect (self):
        return self._clip_rect
        
                
def SDL_MUSTLOCK (s):
    """SDL_MUSTLOCK (s) -> bool
    
    Checks, if a SDL_Surface must be locked before accessing its pixels.
    """
    return ((s.flags & SDL_RLEACCEL) != 0)

@sdltype("SDL_ConvertPixels", [ctypes.c_int, ctypes.c_int, ctypes.c_uint,
                               ctypes.POINTER(ctypes.c_ubyte), ctypes.c_int,
                               ctypes.c_uint, ctypes.POINTER(ctypes.c_ubyte),
                               ctypes.c_int], ctypes.c_int)
def convert_pixels (width, height, srcformat, src, srcpitch, dstformat,
    dstpitch):
    """
    """
    srcp = array.to_ctypes (src, ctypes.c_ubyte)
    dst = ctypes.c_ubyte * width * height * dstpitch
    ret = dll.SDL_ConvertPixels (width, height, srcformat, srcp, srcpitch,
                                 dstformat, dst, dspitch)
    if ret == 0:
        return dst
    return None

@sdltype("SDL_ConvertSurface", [ctypes.POINTER(SDL_Surface),
                                ctypes.POINTER(SDL_PixelFormat),
                                ctypes.c_uint], ctypes.POINTER(SDL_Surface))
def convert_surface (src, format, flags):
    """
    """
    ret = dll.SDL_ConvertSurface (src, format, flags)
    return ret.contents

@sdltype("SDL_ConvertSurfaceFormat", [ctypes.POINTER(SDL_Surface),
                                      ctypes.c_uint, ctypes.c_uint],
         ctypes.POINTER(SDL_Surface))
def convert_surface_format (src, format, flags):
    """
    """
    ret = dll.SDL_ConvertSurfaceFormat (src, format, flags)
    return ret.contents

@sdltype("SDL_CreateRGBSurface", [ctypes.c_uint, ctypes.c_int, ctypes.c_int,
                                  ctypes.c_int, ctypes.c_uint, ctypes.c_uint,
                                  ctypes.c_uint, ctypes.c_uint], 
         ctypes.POINTER(SDL_Surface))
def create_rgb_surface (flags, width, height, depth, rmask, gmask, bmask,
                        amask):
    """
    """
    ret = dll.SDL_CreateRGBSurface (flags, width, height, depth, rmask, gmask,
        bmask, amask)
    return ret.contents

@sdltype("SDL_CreateRGBSurfaceFrom", [ctypes.POINTER(ctypes.c_ubyte),
                                      ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                      ctypes.c_uint, ctypes.c_uint,
                                      ctypes.c_uint, ctypes.c_uint],
         ctypes.POINTER(SDL_Surface))
def create_rgb_surface_from (pixels, width, height, depth, rmask, gmask, bmask,
    amask):
    """
    """
    ret = dll.SDL_CreateRGBSurfaceFrom (pixels, width, height, depth,
                                        rmask, gmask, bmask, amask)
    return ret.contents

@sdltype("SDL_FillRect", [ctypes.POINTER(SDL_Surface),
                          ctypes.POINTER(SDL_Rect), ctypes.c_uint],
         ctypes.c_int)
def fill_rect (dst, rect, color):
    """
    """
    return dll.SDL_FillRect (dst, rect, color)

@sdltype("SDL_FillRects", [ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect), ctypes.c_int,
                           ctypes.c_uint], ctypes.c_int)
def fill_rects (dst, rects, count, color):
    """
    """
    return dll.SDL_FillRects (dst, rects, count, color)

@sdltype("SDL_FreeSurface", [ctypes.POINTER(SDL_Surface)], None)
def free_surface (surface):
    """
    """
    dll.SDL_FreeSurface (surface)

@sdltype("SDL_GetClipRect", [ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(SDL_Rect)], None)
def get_clip_rect (surface):
    """
    """
    rect = SDL_Rect ()
    dll.SDL_GetClipRect (surface, ctypes.byref(rect))
    return rect

@sdltype("SDL_SetClipRect", [ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(SDL_Rect)], None)
def set_clip_rect (surface, rect):
    """
    """
    ret = dll.SDL_SetClipRect (surface, rect)
    return ret == SDL_TRUE
    
@sdltype("SDL_GetColorKey", [ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(ctypes.c_uint)], ctypes.c_int)
def get_color_key (surface):
    """
    """
    key = ctypes.c_uint ()
    ret = dll.SDL_GetColorKey (surface, ctypes.byref(key))
    if ret == 0:
        return key
    return None

@sdltype("SDL_SetColorKey", [ctypes.POINTER(SDL_Surface), ctypes.c_int,
                             ctypes.c_uint], ctypes.c_int)
def set_color_key (surface, flag, key):
    """
    """
    ret = dll.SDL_SetColorKey (surface, flag, key)
    if ret != 0:
        raise SDLError ()

@sdltype("SDL_GetSurfaceAlphaMod", [ctypes.POINTER(SDL_Surface),
                                    ctypes.POINTER(ctypes.c_ubyte)],
    ctypes.c_int)
def get_surface_alpha_mod (surface):
    """
    """
    alpha = ctypes.c_ubyte ()
    ret = dll.SDL_GetSurfaceAlphaMod (surface, ctypes.byref(alpha))
    if ret == 0:
        return alpha
    return None

@sdltype("SDL_SetSurfaceAlphaMod", [ctypes.POINTER(SDL_Surface),
                                    ctypes.c_ubyte], ctypes.c_int)
def set_surface_alpha_mod (surface, alpha):
    """
    """
    ret = dll.SDL_SetSurfaceAlphaMod (surface, alpha)
    if ret != 0:
        raise SDLError ()
    
@sdltype("SDL_SetSurfaceBlendMode", [ctypes.POINTER(SDL_Surface),
                                     ctypes.c_uint], ctypes.c_int)
def set_surface_blend_mode (surface, blend):
    """
    """
    ret = dll.SDL_SetSurfaceBlendMode (surface, blend)
    if ret != 0:
        raise SDLError ()

@sdltype("SDL_GetSurfaceColorMod", [ctypes.POINTER(SDL_Surface),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte)],
         ctypes.c_int)
def get_surface_color_mod (surface):
    """
    """
    r, g, b = ctypes.c_ubyte (), ctypes.c_ubyte (), ctypes.c_ubyte ()
    ret = dll.SDL_GetSurfaceColorMod (surface, ctypes.byref(r), ctypes.byref(g),
                                      ctypes.byref(b))
    if ret == 0:
        return (r, g, b)
    return None

@sdltype("SDL_SetSurfaceColorMod", [ctypes.POINTER(SDL_Surface),
                                    ctypes.c_ubyte, ctypes.c_ubyte,
                                    ctypes.c_ubyte], ctypes.c_int)
def set_surface_color_mod (surface, r, g, b):
    """
    """
    ret = dll.SDL_SetSurfaceColorMod (surface, r, g, b)
    if ret != 0:
        raise SDLError ()
    

#@sdltype("SDL_LoadBMP", [ctypes.c_char_p], ctypes.POINTER(SDL_Surface))
#def load_bmp (filename):
#    """
#    """
#    sf = dll.SDL_LoadBMP (filename)
#   return sf.contents
# TODO: load_bmp_rw

#@sdltype("SDL_SaveBMP", [ctypes.POINTER(SDL_Surface), ctypes.c_char_p],
#         ctypes.c_int)
#def save_bmp (surface, filename):
#    """
#    """
#    ret = dll.SDL_SaveBMP (surface, filename)
#    if ret != 0:
#        raise SDLError ()
#
# TODO: save_bmp_rw

@sdltype("SDL_LockSurface", [ctypes.POINTER(SDL_Surface)], ctypes.c_int)
def lock_surface (surface):
    """
    """
    ret = dll.SDL_LockSurface (surface)
    if ret != 0:
        raise SDLError ()

def SDL_MUSTLOCK(surface):
    """
    """
    return (surface.flags & 0x00000002) != 0 # 0x00000002 == SDL_RLEACCEL

@sdltype("SDL_UnlockSurface", [ctypes.POINTER(SDL_Surface)], None)
def unlock_surface (surface):
    """
    """
    dll.SDL_UnlockSurface (surface)

@sdltype("SDL_LowerBlit", [ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect),
                           ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def lower_blit (src, srcrect, dst, dstrect):
    """
    """
    if srcrect is not None:
        srcrect = ctypes.byref (srcrect)
    ret = dll.SDL_LowerBlit (src, srcrect, dst, dstrect)
    if ret != 0:
        raise SDLError ()

@sdltype("SDL_LowerBlitScaled", [ctypes.POINTER(SDL_Surface),
                                 ctypes.POINTER(SDL_Rect),
                                 ctypes.POINTER(SDL_Surface),
                                 ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def lower_blit_scaled (src, srcrect, dst, dstrect):
    """
    """
    ret = dll.SDL_LowerBlitScaled (src, srcrect, dst, dstrect)
    if ret != 0:
        raise SDLError ()

@sdltype("SDL_UpperBlit", [ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect),
                           ctypes.POINTER(SDL_Surface),
                           ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def upper_blit (src, srcrect, dst, dstrect):
    """
    """
    ret = 0
    if srcrect is not None:
        srcrect = ctypes.byref (srcrect)
    ret = dll.SDL_UpperBlit (src, srcrect, dst, dstrect)
    if ret != 0:
        raise SDLError ()

blit_surface = upper_blit
        
@sdltype("SDL_LowerBlitScaled", [ctypes.POINTER(SDL_Surface),
                                 ctypes.POINTER(SDL_Rect),
                                 ctypes.POINTER(SDL_Surface),
                                 ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def upper_blit_scaled (src, srcrect, dst, dstrect):
    """
    """
    ret = dll.SDL_UpperBlitScaled (src, srcrect, dst, dstrect)
    if ret != 0:
        raise SDLError ()

@sdltype("SDL_SoftStretch", [ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(SDL_Rect),
                             ctypes.POINTER(SDL_Surface),
                             ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def soft_stretch (src, srcrect, dst, dstrect):
    """
    """
    ret = 0
    if srcrect is not None:
        srcrect = ctypes.byref (srcrect)
    if dstrect is not None:
        dstrect = ctypes.byref (dstrect)
    ret = dll.SDL_SoftStretch (src, srcrect, dst, dstrect)
    if ret != 0:
        raise SDLError ()
        
@sdltype("SDL_SetSurfacePalette", [ctypes.POINTER(SDL_Surface),
                                   ctypes.POINTER(SDL_Palette)], ctypes.c_int)
def set_surface_palette (surface, palette):
    """
    """
    ret = dll.SDL_SetSurfacePalette (surface, palette)
    if ret != 0:
        raise SDLError ()

@sdltype("SDL_SetSurfaceRLE", [ctypes.POINTER(SDL_Surface), ctypes.c_int],
         ctypes.c_int)
def set_surface_rle (surface, flag):
    """
    """
    ret = dll.SDL_SetSurfaceRLE (surface, flag)
    if ret != 0:
        raise SDLError ()
