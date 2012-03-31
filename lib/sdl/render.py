"""
Wrapper methods around the SDL2 platform routines.
"""
import ctypes
from pygame2.compat import *
from pygame2.sdl import sdltype, dll, SDL_TRUE
from pygame2.sdl.error import SDLError
from pygame2.sdl.video import SDL_Window
from pygame2.sdl.surface import SDL_Surface
from pygame2.sdl.rect import SDL_Rect

SDL_RENDERER_SOFTWARE       = 0x00000001
SDL_RENDERER_ACCELERATED    = 0x00000002
SDL_RENDERER_PRESENTVSYNC   = 0x00000004
SDL_RENDERER_TARGETTEXTURE  = 0x00000008

SDL_TEXTUREACCESS_STATIC    = 0
SDL_TEXTUREACCESS_STREAMING = 1
SDL_TEXTUREACCESS_TARGET    = 2

SDL_TEXTUREMODULATE_NONE    = 0x00000000
SDL_TEXTUREMODULATE_COLOR   = 0x00000001
SDL_TEXTUREMODULATE_ALPHA   = 0x00000002

class SDL_RendererInfo (ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("flags", ctypes.c_uint),
                ("num_texture_formats", ctypes.c_uint),
                ("texture_formats", (ctypes.c_uint * 16)),
                ("max_texture_width", ctypes.c_int),
                ("max_texture_height", ctypes.c_int),
                ]

class SDL_Renderer (ctypes.Structure):
    pass
    
class SDL_Texture (ctypes.Structure):
    pass
    

@sdltype("SDL_GetNumRenderDrivers", None, ctypes.c_int)
def get_num_render_drivers ():
    """
    """
    return dll.SDL_GetNumRenderDrivers ()

@sdltype("SDL_GetRenderDriverInfo",
         [ctypes.c_int, ctypes.POINTER(SDL_RendererInfo)], ctypes.c_int)
def get_render_driver_info (index):
    """
    """
    info = SDL_RendererInfo ()
    retval = dll.SDL_GetRenderDriverInfo (index, ctypes.byref (info))
    if retval == -1:
        raise SDLError ()
    return info

@sdltype("SDL_CreateWindowAndRenderer",
         [ctypes.c_int, ctypes.c_int, ctypes.c_uint,
          ctypes.POINTER(ctypes.POINTER(SDL_Window)),
          ctypes.POINTER(ctypes.POINTER(SDL_Renderer))], ctypes.c_int)
def create_window_and_renderer (width, height, windowflags):
    """
    """
    window = ctypes.POINTER(SDL_Window)()
    renderer = ctypes.POINTER(SDL_Renderer)()
    retval = SDL_CreateWindowAndRenderer (width, height, ctypes.byref (window),
                                          ctypes.byref (renderer))
    if retval == -1:
        raise SDLError ()
    return window.value, renderer.value
    
@sdltype("SDL_CreateRenderer", [ctypes.POINTER(SDL_Window), ctypes.c_int,
                                ctypes.c_uint], ctypes.POINTER(SDL_Renderer))
def create_renderer (window, index, flags):
    """
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    renderer = SDL_CreateRenderer (ctypes.byref (window), index, flags)
    if renderer is None or not bool(renderer):
        raise SDLError ()
    return renderer.value

@sdltype("SDL_CreateSoftwareRenderer", [ctypes.POINTER(SDL_Surface)],
         ctypes.POINTER(SDL_Renderer))
def create_software_renderer (surface):
    """
    """
    if not isinstance (surface, SDL_Surface):
        raise TypeError ("surface must be a SDL_Surface")
    renderer = dll.SDL_CreateSoftwareRenderer (ctypes.byref (surface))
    if renderer is None or not bool(renderer):
        raise SDLError ()
    return renderer.value
    
@sdltype("SDL_GetRenderer", [ctypes.POINTER(SDL_Window)],
         ctypes.POINTER(SDL_Renderer))
def get_renderer (window):
    """
    """
    if not isinstance (window, SDL_Window):
        raise TypeError ("window must be a SDL_Window")
    renderer = dll.SDL_GetRenderer (ctypes.byref (window))
    if renderer is None or not bool(renderer):
        raise SDLError ()
    return renderer.value

@sdltype("SDL_GetRendererInfo", [ctypes.POINTER(SDL_Renderer),
                                 ctypes.POINTER(SDL_RenderInfo)], ctypes.c_int)
def get_renderer_info (renderer):
    """
    """
    if not isinstance (renderer, SDL_Renderer):
        raise TypeError ("renderer must be a SDL_Renderer")
    info = SDL_RenderInfo ()
    retval = dll.SDL_GetRendererInfo (ctypes.byref (renderer),
                                      ctypes.byref (info))
    if retval == -1:
        raise SDLError ()
    return info

@sdltype("SDL_CreateTexture", [ctypes.POINTER(SDL_Renderer), ctypes.c_uint,
                               ctypes.c_int, ctypes.c_int, ctypes.c_int],
         ctypes.POINTER(SDL_Texture))
def create_texture (renderer, format, access, w, h):
    """
    """
    if not isinstance (renderer, SDL_Renderer):
        raise TypeError ("renderer must be a SDL_Renderer")
    retval = dll.SDL_CreateTexture (ctypes.byref (renderer), access, w, h)
    if retval is None or not bool (retval):
        raise SDLError ()
    return retval.contents

@sdltype("SDL_CreateTextureFromSurface", [ctypes.POINTER(SDL_Renderer),
                                          ctypes.POINTER(SDL_Surface)],
         ctypes.POINTER(SDL_Texture))
def create_texture_from_surface (renderer, surface):
    """
    """
    if not isinstance (renderer, SDL_Renderer):
        raise TypeError ("renderer must be a SDL_Renderer")
    if not isinstance (surface, SDL_Surface):
        raise TypeError ("surface must be a SDL_Surface")
    retval = dll.SDL_CreateTextureFromSurface (ctypes.byref(renderer),
                                               ctypes.byref(surface))
    if retval is None or not bool (retval):
        raise SDLError ()
    return retval.contents

@sdltype("SDL_QueryTexture", [ctypes.POINTER(SDL_Texture),
                              ctypes.POINTER(ctypes.c_uint),
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int)], ctypes.c_int)
def query_texture (texture):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    flags = ctypes.c_uint (0)
    access = ctypes.c_int (0)
    w = ctypes.c_int (0)
    h = ctypes.c_int (0)
    retval = dll.SDL_QueryTexture (ctypes.byref(texture), ctypes.byref(flags),
                                   ctypes.byref(access), ctypes.byref(w),
                                   ctypes.byref(h))
    if retval == -1:
        raise SDLError ()
    return flags, access, w, h
    
@sdltype("SDL_SetTextureColorMod", [ctypes.POINTER(SDL_Texture),
                                    ctypes.c_ubyte, ctypes.c_ubyte,
                                    ctypes.c_ubyte], ctypes.c_int)
def set_texture_color_mod (texture, r, g, b):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    retval = dll.SDL_SetTextureColorMod (ctypes.byref(texture), r, g, b)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GetTextureColorMod", [ctypes.POINTER(SDL_Texture),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte)],
         ctypes.c_int)
def get_texture_color_mod (texture):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    r = ctypes.c_ubyte (0)
    g = ctypes.c_ubyte (0)
    b = ctypes.c_ubyte (0)
    retval = dll.SDL_GetTextureColorMod (ctypes.byref(texture),
                                         ctypes.byref(r), ctypes.byref(g),
                                         ctypes.byref(b))
    if retval == -1:
        raise SDLError ()
    return r, g, b

@sdltype("SDL_SetTextureAlphaMod", [ctypes.POINTER(SDL_Texture),
                                    ctypes.c_ubyte], ctypes.c_int)
def set_texture_alpha_mod (texture, alpha):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    retval = dll.SDL_SetTextureAlphaMod (ctypes.byref(texture), alpha)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GetTextureAlphaMod", [ctypes.POINTER(SDL_Texture),
                                    ctypes.POINTER(ctypes.c_ubyte)],
         ctypes.c_int)
def get_texture_alpha_mod (texture):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    alpha = ctypes.c_ubyte (0)
    retval = dll.SDL_GetTextureAlphaMod (ctypes.byref(texture),
                                         ctypes.byref(alpha))
    if retval == -1:
        raise SDLError ()
    return alpha

@sdltype("SDL_SetTextureBlendMode", [ctypes.POINTER(SDL_Texture), ctypes.c_int],
         ctypes.c_int)
def set_texture_blend_mode (texture, mode):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    retval = dll.SDL_SetTextureBlendMode (ctypes.byref(texture), mode)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_GetTextureBlendMode", [ctypes.POINTER(SDL_Texture),
                                     ctypes.POINTER(ctypes.c_ubyte)],
         ctypes.c_int)
def get_texture_blend_mode (texture):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    mode = ctypes.c_int (0)
    retval = dll.SDL_GetTextureBlendMode (ctypes.byref(texture),
                                          ctypes.byref(mode))
    if retval == -1:
        raise SDLError ()
    return mode

@sdltype("SDL_UpdateTexture", [ctypes.POINTER(SDL_Texture),
                               ctypes.POINTER(SDL_Rect), ctypes.c_void_p,
                               ctypes.c_int], ctypes.c_int)
def update_texture (texture, pixels, pitch):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    retval = dll.SDL_UpdateTexture (ctypes.byref(texture),
                                    ctypes.byref(pixels), pitch)
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_LockTexture", [ctypes.POINTER(SDL_Texture),
                             ctypes.POINTER(SDL_Rect),
                             ctypes.POINTER(ctypes.c_void_p),
                             ctypes.POINTER(ctypes.c_int)], ctypes.c_int)
def lock_texture (texture, rect=None):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    if rect is not None and not isinstance (rect, SDL_Rect):
        raise TypeError ("rect must be a SDL_Rect or None")
    pixels = ctypes.POINTER(ctypes.c_void_p)()
    pitch = ctypes.c_int(0)
    if rect:
        retval = dll.SDL_LockTexture (ctypes.byref(texture), None,
                                      ctypes.byref(pixels), ctypes.byref(pitch))
    else:
        retval = dll.SDL_LockTexture (ctypes.byref(texture), ctypes.byref(rect),
                                      ctypes.byref(pixels), ctypes.byref(pitch))
    if retval == -1:
        raise SDLError ()
    return pixels.contents, pitch

@sdltype("SDL_UnlockTexture", [ctypes.POINTER(SDL_Texture)], None)
def unlock_texture (texture):
    """
    """
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    dll.SDL_UnlockTexture (ctypes.byref(texture))

@sdltype("SDL_RenderTargetSupported", [ctypes.POINTER(SDL_Renderer)],
         ctypes.c_int)
def render_target_supported (renderer):
    """
    """
    if not isinstance (renderer, SDL_Renderer):
        raise TypeError ("renderer is not a SDL_Renderer")
    return dll.SDL_RenderTargetSupported (ctypes.byref(renderer)) == SDL_TRUE

@sdltype("SDL_SetRenderTarget", [ctypes.POINTER(SDL_Renderer),
                                 ctypes.POINTER(SDL_Texture)], ctypes.c_int)
def set_render_target (renderer, texture):
    """
    """
    if not isinstance (renderer, SDL_Renderer):
        raise TypeError ("renderer is not a SDL_Renderer")
    if not isinstance (texture, SDL_Texture):
        raise TypeError ("texture must be a SDL_Texture")
    retval = dll.SDL_SetRenderTarget (ctypes.byref(renderer),
                                      ctypes.byref(texture))
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_RenderSetViewport", [ctypes.POINTER(SDL_Renderer),
                                   ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def render_set_viewport (renderer, rect):
    """
    """
    if not isinstance (renderer, SDL_Renderer):
        raise TypeError ("renderer is not a SDL_Renderer")
    if not isinstance (rect, SDL_Rect):
        raise TypeError ("rect must be a SDL_Rect")
    retval = dll.SDL_RenderSetViewport (ctypes.byref(renderer),
                                        ctypes.byref(rect))
    if retval == -1:
        raise SDLError ()

@sdltype("SDL_RenderGetViewport", [ctypes.POINTER(SDL_Renderer),
                                   ctypes.POINTER(SDL_Rect)], None)
def render_get_viewport (renderer):
    """
    """
    if not isinstance (renderer, SDL_Renderer):
        raise TypeError ("renderer is not a SDL_Renderer")
    rect = SDL_Rect()
    dll.SDL_RenderGetViewport (ctypes.byref(renderer), ctypes.byref(rect))
    return rect

# @sdltype("SDL_SetRenderDrawColor", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
# @sdltype("", [], None)
