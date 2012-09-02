"""
Wrapper methods around the SDL2 platform routines.
"""
import ctypes
from pygame2.compat import *
from pygame2.sdl import dll, sdltype, SDL_TRUE, SDLError
from pygame2.sdl.video import SDL_Window
from pygame2.sdl.surface import SDL_Surface
from pygame2.sdl.rect import SDL_Point, SDL_Rect
import pygame2.array as array

__all__ = ["SDL_RendererInfo", "SDL_Renderer", "SDL_Texture",
           "get_num_render_drivers", "get_render_driver_info",
           "create_window_and_renderer", "create_renderer",
           "create_software_renderer", "get_renderer", "get_renderer_info",
           "create_texture", "create_texture_from_surface", "query_texture",
           "set_texture_color_mod", "get_texture_color_mod",
           "set_texture_alpha_mod", "get_texture_alpha_mod",
           "set_texture_blend_mode", "get_texture_blend_mode",
           "update_texture", "lock_texture", "unlock_texture",
           "render_target_supported", "set_render_target",
           "render_set_viewport", "render_get_viewport",
           "set_render_draw_color", "get_render_draw_color",
           "set_render_draw_blend_mode", "get_render_draw_blend_mode",
           "render_clear", "render_draw_point", "render_draw_points",
           "render_draw_line", "render_draw_lines", "render_draw_rect",
           "render_draw_rects", "render_fill_rect", "render_fill_rects",
           "render_copy", "render_read_pixels", "render_present",
           "destroy_texture", "destroy_renderer"
           ]

SDL_RENDERER_SOFTWARE      = 0x00000001
SDL_RENDERER_ACCELERATED   = 0x00000002
SDL_RENDERER_PRESENTVSYNC  = 0x00000004
SDL_RENDERER_TARGETTEXTURE = 0x00000008

SDL_TEXTUREACCESS_STATIC    = 0
SDL_TEXTUREACCESS_STREAMING = 1
SDL_TEXTUREACCESS_TARGET    = 2
_ALLOWED_ACCESS = (SDL_TEXTUREACCESS_STATIC, SDL_TEXTUREACCESS_STREAMING,
                   SDL_TEXTUREACCESS_TARGET)

SDL_TEXTUREMODULATE_NONE  = 0x00000000
SDL_TEXTUREMODULATE_COLOR = 0x00000001
SDL_TEXTUREMODULATE_ALPHA = 0x00000002


class SDL_RendererInfo(ctypes.Structure):
    """TODO"""
    _fields_ = [("_name", ctypes.c_char_p),
                ("flags", ctypes.c_uint),
                ("num_texture_formats", ctypes.c_uint),
                ("texture_formats", (ctypes.c_uint * 16)),
                ("max_texture_width", ctypes.c_int),
                ("max_texture_height", ctypes.c_int),
                ]

    @property
    def name(self):
        """The name of the rendering context driver."""
        return stringify(self._name, "utf-8")

    def __repr__(self):
        return """SDL_RendererInfo(name=%s, flags=%d, num_texture_formats=%d,
max_texture_width=%d, max_texture_height=%d)
""" % (self.name, self.flags, self.num_texture_formats,
       self.max_texture_width, self.max_texture_height)


class SDL_Renderer(ctypes.Structure):
    """TODO"""
    pass


class SDL_Texture(ctypes.Structure):
    """TODO"""
    pass


SDL_Texture._fields_ = [
    ("_magic", ctypes.c_void_p),
    ("_format", ctypes.c_uint),
    ("_access", ctypes.c_int),
    ("_w", ctypes.c_int),
    ("_h", ctypes.c_int),
    ("_modMode", ctypes.c_int),
    ("_blendMode", ctypes.c_int),
    ("_r", ctypes.c_ubyte),
    ("_g", ctypes.c_ubyte),
    ("_b", ctypes.c_ubyte),
    ("_a", ctypes.c_ubyte),
    ("_renderer", ctypes.POINTER(SDL_Renderer)),
    ("_native", ctypes.POINTER(SDL_Texture)),
    ("_yuv", ctypes.c_void_p),  # SDL_SW_YUVTexture
    ("_pixels", ctypes.c_void_p),
    ("_pitch", ctypes.c_int),
    ("_locked_rect", SDL_Rect),
    ("_driverdata", ctypes.c_void_p),
    ("_prev", ctypes.POINTER(SDL_Texture)),
    ("_next", ctypes.POINTER(SDL_Texture)),
    ]


SDL_Renderer._fields_ = [
    ("_magic", ctypes.c_void_p),
    ("_WindowEvent", ctypes.c_void_p),
    ("_CreateTexture", ctypes.POINTER(ctypes.c_int)),
    ("_SetTextureColorMod", ctypes.POINTER(ctypes.c_int)),
    ("_SetTextureAlphaMod", ctypes.POINTER(ctypes.c_int)),
    ("_SetTextureBlendMode", ctypes.POINTER(ctypes.c_int)),
    ("_UpdateTexture", ctypes.POINTER(ctypes.c_int)),
    ("_LockTexture", ctypes.POINTER(ctypes.c_int)),
    ("_UnlockTexture", ctypes.c_void_p),
    ("_SetRenderTarget", ctypes.POINTER(ctypes.c_int)),
    ("_UpdateViewPort", ctypes.POINTER(ctypes.c_int)),
    ("_RenderClear", ctypes.POINTER(ctypes.c_int)),
    ("_RenderDrawPoints", ctypes.POINTER(ctypes.c_int)),
    ("_RenderDrawLines", ctypes.POINTER(ctypes.c_int)),
    ("_RenderFillRects", ctypes.POINTER(ctypes.c_int)),
    ("_RenderCopy", ctypes.POINTER(ctypes.c_int)),
    ("_RenderReadPixels", ctypes.POINTER(ctypes.c_int)),
    ("_RenderPresent", ctypes.c_void_p),
    ("_DestroyTexture", ctypes.c_void_p),
    ("_DestroyRenderer", ctypes.c_void_p),
    ("info", SDL_RendererInfo),
    ("window", ctypes.POINTER(SDL_Window)),
    ("_hidden", ctypes.c_int),
    ("_resized", ctypes.c_int),
    ("_viewport", SDL_Rect),
    ("_viewport_backup", SDL_Rect),
    ("_textures", ctypes.POINTER(SDL_Texture)),
    ("_target", ctypes.POINTER(SDL_Texture)),
    ("_r", ctypes.c_ubyte),
    ("_g", ctypes.c_ubyte),
    ("_b", ctypes.c_ubyte),
    ("_a", ctypes.c_ubyte),
    ("_blendMode", ctypes.c_int),
    ("_driverdata", ctypes.c_void_p),
    ]


@sdltype("SDL_GetNumRenderDrivers", None, ctypes.c_int)
def get_num_render_drivers():
    """Gets the number of 2D renderering drivers available for the
    current display.
    """
    return dll.SDL_GetNumRenderDrivers()


@sdltype("SDL_GetRenderDriverInfo",
         [ctypes.c_int, ctypes.POINTER(SDL_RendererInfo)], ctypes.c_int)
def get_render_driver_info(index):
    """Retrieves information about a 2D rendering driver for the current
    display.

    Returns a SDL_RendererInfo on success and raises a SDLError on
    failure.
    """
    if type(index) is not int:
        raise TypeError("index must be an int")
    info = SDL_RendererInfo()
    retval = dll.SDL_GetRenderDriverInfo(index, ctypes.byref(info))
    if retval == -1:
        raise SDLError()
    return info


@sdltype("SDL_CreateWindowAndRenderer",
         [ctypes.c_int, ctypes.c_int, ctypes.c_uint,
          ctypes.POINTER(ctypes.POINTER(SDL_Window)),
          ctypes.POINTER(ctypes.POINTER(SDL_Renderer))], ctypes.c_int)
def create_window_and_renderer(width, height, windowflags):
    """Creates a SDL_Window and a default renderer for the window and
    returns them as tuple.

    Raises a SDLError on failure.
    """
    window = ctypes.POINTER(SDL_Window)()
    renderer = ctypes.POINTER(SDL_Renderer)()
    retval = dll.SDL_CreateWindowAndRenderer(width, height, windowflags,
                                             ctypes.byref(window),
                                             ctypes.byref(renderer))
    if retval == -1:
        raise SDLError()
    return window.contents, renderer.contents


@sdltype("SDL_CreateRenderer", [ctypes.POINTER(SDL_Window), ctypes.c_int,
                                ctypes.c_uint], ctypes.POINTER(SDL_Renderer))
def create_renderer(window, index, flags):
    """Creates a 2D rendering context for a SDL_Window.

    index denotes the index if the rendering driver to initialize, or -1
    to initialize the first one supporting the requested flags.

    Raises a SDLError on failure
    """
    if not isinstance(window, SDL_Window):
        raise TypeError("window must be a SDL_Window")
    renderer = dll.SDL_CreateRenderer(ctypes.byref(window), index, flags)
    if renderer is None or not bool(renderer):
        raise SDLError()
    return renderer.contents


@sdltype("SDL_CreateSoftwareRenderer", [ctypes.POINTER(SDL_Surface)],
         ctypes.POINTER(SDL_Renderer))
def create_software_renderer(surface):
    """Creates a 2D software rendering context for a surface.

    Raises a SDLError on failure.
    """
    if not isinstance(surface, SDL_Surface):
        raise TypeError("surface must be a SDL_Surface")
    renderer = dll.SDL_CreateSoftwareRenderer(ctypes.byref(surface))
    if renderer is None or not bool(renderer):
        raise SDLError()
    return renderer.contents


@sdltype("SDL_GetRenderer", [ctypes.POINTER(SDL_Window)],
         ctypes.POINTER(SDL_Renderer))
def get_renderer(window):
    """Retrieves the rendering context for the passed window.
    """
    if not isinstance(window, SDL_Window):
        raise TypeError("window must be a SDL_Window")
    renderer = dll.SDL_GetRenderer(ctypes.byref(window))
    if renderer is None or not bool(renderer):
        return None
    return renderer.contents


@sdltype("SDL_GetRendererInfo", [ctypes.POINTER(SDL_Renderer),
                                 ctypes.POINTER(SDL_RendererInfo)],
         ctypes.c_int)
def get_renderer_info(renderer):
    """Retrieves the information about a rendering context.

    Raises a SDLError on failure.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer must be a SDL_Renderer")
    info = SDL_RendererInfo()
    retval = dll.SDL_GetRendererInfo(ctypes.byref(renderer),
                                     ctypes.byref(info))
    if retval == -1:
        raise SDLError()
    return info


@sdltype("SDL_CreateTexture", [ctypes.POINTER(SDL_Renderer), ctypes.c_uint,
                               ctypes.c_int, ctypes.c_int, ctypes.c_int],
         ctypes.POINTER(SDL_Texture))
def create_texture(renderer, format_, access, w, h):
    """Creates a texture for the specified rendering context.

    Raises an error, if the format is unsupported or the width and
    height are out of range.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer must be a SDL_Renderer")
    if type(format_) not in (int, long):
        raise TypeError("format must be a valid SDL_PIXELFORMAT value")
    if format_ < 0:
        raise ValueError("format must be a valid SDL_PIXELFORMAT value")
    if access not in _ALLOWED_ACCESS:
        raise ValueError("access must be a valid SDL_TEXTUREACCESS value")

    retval = dll.SDL_CreateTexture(ctypes.byref(renderer), format_, access,
                                   w, h)
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


@sdltype("SDL_CreateTextureFromSurface", [ctypes.POINTER(SDL_Renderer),
                                          ctypes.POINTER(SDL_Surface)],
         ctypes.POINTER(SDL_Texture))
def create_texture_from_surface(renderer, surface):
    """Creates a texture from an existing surface.

    The surface is not modified or freed by this function.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer must be a SDL_Renderer")
    if not isinstance(surface, SDL_Surface):
        raise TypeError("surface must be a SDL_Surface")
    retval = dll.SDL_CreateTextureFromSurface(ctypes.byref(renderer),
                                              ctypes.byref(surface))
    if retval is None or not bool(retval):
        raise SDLError()
    return retval.contents


@sdltype("SDL_QueryTexture", [ctypes.POINTER(SDL_Texture),
                              ctypes.POINTER(ctypes.c_uint),
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int),
                              ctypes.POINTER(ctypes.c_int)], ctypes.c_int)
def query_texture(texture):
    """Queries the attributes of the texture and returns them as tuple.

    This returns the texture flags, access mode and width and height.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    flags = ctypes.c_uint(0)
    access = ctypes.c_int(0)
    w = ctypes.c_int(0)
    h = ctypes.c_int(0)
    retval = dll.SDL_QueryTexture(ctypes.byref(texture), ctypes.byref(flags),
                                  ctypes.byref(access), ctypes.byref(w),
                                  ctypes.byref(h))
    if retval == -1:
        raise SDLError()
    return flags.value, access.value, w.value, h.value


@sdltype("SDL_SetTextureColorMod", [ctypes.POINTER(SDL_Texture),
                                    ctypes.c_ubyte, ctypes.c_ubyte,
                                    ctypes.c_ubyte], ctypes.c_int)
def set_texture_color_mod(texture, r, g, b):
    """Sets the additional color value to be used in render copy operations.

    The color value will be multiplied into copy operations.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    retval = dll.SDL_SetTextureColorMod(ctypes.byref(texture), r, g, b)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_GetTextureColorMod", [ctypes.POINTER(SDL_Texture),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte)],
         ctypes.c_int)
def get_texture_color_mod(texture):
    """Gets the additional color value used in render copy operations.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    r = ctypes.c_ubyte(0)
    g = ctypes.c_ubyte(0)
    b = ctypes.c_ubyte(0)
    retval = dll.SDL_GetTextureColorMod(ctypes.byref(texture), ctypes.byref(r),
                                        ctypes.byref(g), ctypes.byref(b))
    if retval == -1:
        raise SDLError()
    return r.value, g.value, b.value


@sdltype("SDL_SetTextureAlphaMod", [ctypes.POINTER(SDL_Texture),
                                    ctypes.c_ubyte], ctypes.c_int)
def set_texture_alpha_mod(texture, alpha):
    """Sets the additional alpha value used in render copy operations.

    The alpha value will be multiplied into copy operations.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    retval = dll.SDL_SetTextureAlphaMod(ctypes.byref(texture), alpha)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_GetTextureAlphaMod", [ctypes.POINTER(SDL_Texture),
                                    ctypes.POINTER(ctypes.c_ubyte)],
         ctypes.c_int)
def get_texture_alpha_mod(texture):
    """Gets the additional alpha value used in render copy operations.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    alpha = ctypes.c_ubyte(0)
    retval = dll.SDL_GetTextureAlphaMod(ctypes.byref(texture),
                                        ctypes.byref(alpha))
    if retval == -1:
        raise SDLError()
    return alpha.value


@sdltype("SDL_SetTextureBlendMode", [ctypes.POINTER(SDL_Texture),
                                     ctypes.c_int], ctypes.c_int)
def set_texture_blend_mode(texture, mode):
    """Sets the blend mode to be used for textures copy operations.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    retval = dll.SDL_SetTextureBlendMode(ctypes.byref(texture), mode)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_GetTextureBlendMode", [ctypes.POINTER(SDL_Texture),
                                     ctypes.POINTER(ctypes.c_int)],
         ctypes.c_int)
def get_texture_blend_mode(texture):
    """Gets the blend mode used for texture copy operations.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    mode = ctypes.c_int(0)
    retval = dll.SDL_GetTextureBlendMode(ctypes.byref(texture),
                                         ctypes.byref(mode))
    if retval == -1:
        raise SDLError()
    return mode.value


@sdltype("SDL_UpdateTexture", [ctypes.POINTER(SDL_Texture),
                               ctypes.POINTER(SDL_Rect), ctypes.c_void_p,
                               ctypes.c_int], ctypes.c_int)
def update_texture(texture, rect, pixels, pitch):
    """Update the given texture with new pixel data.

    The passed rect can be None, if the entire texture's pixel data
    should be updated (see lock_texture()).
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    if not isinstance(rect, SDL_Rect):
        raise TypeError("rect must be a SDL_Rect")
    retval = dll.SDL_UpdateTexture(ctypes.byref(texture), ctypes.byref(rect),
                                   ctypes.byref(pixels), pitch)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_LockTexture", [ctypes.POINTER(SDL_Texture),
                             ctypes.POINTER(SDL_Rect),
                             ctypes.POINTER(ctypes.c_void_p),
                             ctypes.POINTER(ctypes.c_int)], ctypes.c_int)
def lock_texture(texture, rect=None):
    """Locks a texture for pixel access and returns the raw pixel data
    and pitch.

    If the rect argument is None, the entire texture will be locked.

    The texture must have been created with SDL_TEXTUREACCESS_STREAMING.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    if rect is not None and not isinstance(rect, SDL_Rect):
        raise TypeError("rect must be a SDL_Rect or None")
    pixels = ctypes.POINTER(ctypes.c_void_p)()
    pitch = ctypes.c_int(0)
    if rect:
        retval = dll.SDL_LockTexture(ctypes.byref(texture), None,
                                     ctypes.byref(pixels), ctypes.byref(pitch))
    else:
        retval = dll.SDL_LockTexture(ctypes.byref(texture), ctypes.byref(rect),
                                     ctypes.byref(pixels), ctypes.byref(pitch))
    if retval == -1:
        raise SDLError()
    return pixels.contents, pitch


@sdltype("SDL_UnlockTexture", [ctypes.POINTER(SDL_Texture)], None)
def unlock_texture(texture):
    """Unlocks a texture and uploads the changed pixel data to the video
    memory, if necessary.
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    dll.SDL_UnlockTexture(ctypes.byref(texture))


@sdltype("SDL_RenderTargetSupported", [ctypes.POINTER(SDL_Renderer)],
         ctypes.c_int)
def render_target_supported(renderer):
    """Determines whether the window of the renderer supports the use of
    render targets.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    return dll.SDL_RenderTargetSupported(ctypes.byref(renderer)) == SDL_TRUE


@sdltype("SDL_SetRenderTarget", [ctypes.POINTER(SDL_Renderer),
                                 ctypes.POINTER(SDL_Texture)], ctypes.c_int)
def set_render_target(renderer, texture=None):
    """Sets a texture as the current rendering target.

    If the passed texture is None, the default render target will be
    used. If a SDL_Texture is passed, it must have been created with the
    SDL_TEXTUREACCESS_TARGET flag.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    if texture is not None and not isinstance(texture, SDL_Texture):
        raise TypeError("texture must be a SDL_Texture")
    if texture is None:
        retval = dll.SDL_SetRenderTarget(ctypes.byref(renderer), None)
    else:
        retval = dll.SDL_SetRenderTarget(ctypes.byref(renderer),
                                         ctypes.byref(texture))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderSetViewport", [ctypes.POINTER(SDL_Renderer),
                                   ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def render_set_viewport(renderer, rect=None):
    """Sets the drawing area for rendering on the current target.

    If the passed SDL_Rect is None, the entire target will be used as
    drawing area.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    if rect is not None and not isinstance(rect, SDL_Rect):
        raise TypeError("rect must be a SDL_Rect")
    if rect is None:
        retval = dll.SDL_RenderSetViewport(ctypes.byref(renderer), None)
    else:
        retval = dll.SDL_RenderSetViewport(ctypes.byref(renderer),
                                           ctypes.byref(rect))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderGetViewport", [ctypes.POINTER(SDL_Renderer),
                                   ctypes.POINTER(SDL_Rect)], None)
def render_get_viewport(renderer):
    """Gets the drawing area for the current target.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    rect = SDL_Rect()
    dll.SDL_RenderGetViewport(ctypes.byref(renderer), ctypes.byref(rect))
    return rect


@sdltype("SDL_SetRenderDrawColor", [ctypes.POINTER(SDL_Renderer),
                                    ctypes.c_ubyte, ctypes.c_ubyte,
                                    ctypes.c_ubyte, ctypes.c_ubyte],
         ctypes.c_int)
def set_render_draw_color(renderer, r, g, b, a):
    """Sets the color used for drawing operations (rect, line and clear).
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    retval = dll.SDL_SetRenderDrawColor(ctypes.byref(renderer), r, g, b, a)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_GetRenderDrawColor", [ctypes.POINTER(SDL_Renderer),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte),
                                    ctypes.POINTER(ctypes.c_ubyte)],
         ctypes.c_int)
def get_render_draw_color(renderer):
    """Gets the color used for drawing operations (rect, line and clear)
    as RGBA tuple.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    r = ctypes.c_ubyte(0)
    g = ctypes.c_ubyte(0)
    b = ctypes.c_ubyte(0)
    a = ctypes.c_ubyte(0)
    retval = dll.SDL_GetRenderDrawColor(ctypes.byref(renderer),
                                        ctypes.byref(r), ctypes.byref(g),
                                        ctypes.byref(b), ctypes.byref(a))
    if retval == -1:
        raise SDLError()
    return r.value, g.value, b.value, a.value


@sdltype("SDL_SetRenderDrawBlendMode", [ctypes.POINTER(SDL_Renderer),
                                        ctypes.c_int], ctypes.c_int)
def set_render_draw_blend_mode(renderer, mode):
    """Sets the blend mode for drawing operations (fill and line).
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    retval = dll.SDL_SetRenderDrawBlendMode(ctypes.byref(renderer), mode)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_GetRenderDrawBlendMode", [ctypes.POINTER(SDL_Renderer),
                                        ctypes.POINTER(ctypes.c_int)],
         ctypes.c_int)
def get_render_draw_blend_mode(renderer):
    """Gets the blend mode for drawing operations (fill and line).
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    mode = ctypes.c_int(0)
    retval = dll.SDL_GetRenderDrawBlendMode(ctypes.byref(renderer),
                                            ctypes.byref(mode))
    if retval == -1:
        raise SDLError()
    return mode.value


@sdltype("SDL_RenderClear", [ctypes.POINTER(SDL_Renderer)], ctypes.c_int)
def render_clear(renderer):
    """Clears the current rendering target with the set drawing color.

    This clears the entire rendering target, ignoring any set viewport.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    retval = dll.SDL_RenderClear(ctypes.byref(renderer))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderDrawPoint", [ctypes.POINTER(SDL_Renderer), ctypes.c_int,
                                 ctypes.c_int], ctypes.c_int)
def render_draw_point(renderer, x, y):
    """Draws a point on the current rendering target.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    retval = dll.SDL_RenderDrawPoint(ctypes.byref(renderer), x, y)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderDrawPoints", [ctypes.POINTER(SDL_Renderer),
                                  ctypes.POINTER(SDL_Point), ctypes.c_int],
         ctypes.c_int)
def render_draw_points(renderer, points):
    """Draws multiple points on the current rendering target.
    """
    points, count = array.to_ctypes(points, SDL_Point)
    retval = dll.SDL_RenderDrawPoints(ctypes.byref(renderer),
                                      ctypes.byref(points), count)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderDrawLine", [ctypes.POINTER(SDL_Renderer), ctypes.c_int,
                                ctypes.c_int, ctypes.c_int, ctypes.c_int],
         ctypes.c_int)
def render_draw_line(renderer, x1, y1, x2, y2):
    """Draws a line on the current rendering target.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    retval = dll.SDL_RenderDrawLine(ctypes.byref(renderer), x1, y1, x2, y2)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderDrawLines", [ctypes.POINTER(SDL_Renderer),
                                 ctypes.POINTER(SDL_Point), ctypes.c_int],
         ctypes.c_int)
def render_draw_lines(renderer, points):
    """Draws a series of connected lines on the current rendering target.
    """
    points, count = array.to_ctypes(points, SDL_Point)
    retval = dll.SDL_RenderDrawLines(ctypes.byref(renderer),
                                     ctypes.byref(points), count)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderDrawRect", [ctypes.POINTER(SDL_Renderer),
                                ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def render_draw_rect(renderer, rect=None):
    """Draws a rectangle on the current rendering target.

    If the passed rect is None, the entire rendering target will be
    outlined.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    if rect is not None and not isinstance(rect, SDL_Rect):
        raise TypeError("rect is not a SDL_Rect")
    if rect is None:
        retval = dll.SDL_RenderDrawRect(ctypes.byref(renderer), None)
    else:
        retval = dll.SDL_RenderDrawRect(ctypes.byref(renderer),
                                        ctypes.byref(rect))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderDrawRects", [ctypes.POINTER(SDL_Renderer),
                                 ctypes.POINTER(SDL_Rect), ctypes.c_int],
         ctypes.c_int)
def render_draw_rects(renderer, rects):
    """Draw multiple rectangles on the current rendering target.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    rects, count = array.to_ctypes(rects, SDL_Rect)
    retval = dll.SDL_RenderDrawRects(ctypes.byref(renderer),
                                     ctypes.byref(rects), count)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderFillRect", [ctypes.POINTER(SDL_Renderer),
                                ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def render_fill_rect(renderer, rect=None):
    """Fill a rectangle on the current rendering target with the set
    drawing color.

    If the passed rect is None, the entire rendering target will be filled.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    if rect is not None and not isinstance(rect, SDL_Rect):
        raise TypeError("rect is not a SDL_Rect")
    if rect is None:
        retval = dll.SDL_RenderFillRect(ctypes.byref(renderer), None)
    else:
        retval = dll.SDL_RenderFillRect(ctypes.byref(renderer),
                                        ctypes.byref(rect))
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderFillRects", [ctypes.POINTER(SDL_Renderer),
                                 ctypes.POINTER(SDL_Rect), ctypes.c_int],
         ctypes.c_int)
def render_fill_rects(renderer, rects):
    """Fills multiple rectangles on the current rendering target with
    the set drawing color.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    rects, count = array.to_ctypes(rects, SDL_Rect)
    retval = dll.SDL_RenderFillRects(ctypes.byref(renderer),
                                     ctypes.byref(rects), count)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderCopy", [ctypes.POINTER(SDL_Renderer),
                            ctypes.POINTER(SDL_Texture),
                            ctypes.POINTER(SDL_Rect),
                            ctypes.POINTER(SDL_Rect)], ctypes.c_int)
def render_copy(renderer, texture, srcrect=None, dstrect=None):
    """Copy a portion of the passed texture to the current rendering target.

    If srcrect is None, the entire texture will be copied. If dstrect
    is None, the entire rendering target will be used as area to copy
    the texture to.
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture is not a SDL_Texture")
    if srcrect is not None and not isinstance(srcrect, SDL_Rect):
        raise TypeError("srcrect must be a SDL_Rect")
    if dstrect is not None and not isinstance(dstrect, SDL_Rect):
        raise TypeError("dstrect must be a SDL_Rect")
    srcval = None
    if srcrect is not None:
        srcval = ctypes.byref(srcrect)
    dstval = None
    if dstrect is not None:
        dstval = ctypes.byref(dstrect)
    retval = dll.SDL_RenderCopy(ctypes.byref(renderer), ctypes.byref(texture),
                                srcval, dstval)
    if retval == -1:
        raise SDLError()


@sdltype("SDL_RenderReadPixels", [ctypes.POINTER(SDL_Renderer),
                                  ctypes.POINTER(SDL_Rect), ctypes.c_uint,
                                  ctypes.POINTER(ctypes.c_uint), ctypes.c_int],
         ctypes.c_int)
def render_read_pixels(renderer, rect, format_, bufsize, pitch):
    """TODO
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    if not isinstance(rect, SDL_Rect):
        raise TypeError("rect is not a SDL_Rect")
    pixelbuf = (bufsize * ctypes.c_uint)()
    retval = dll.SDL_RenderReadPixels(ctypes.byref(renderer),
                                      ctypes.byref(rect), format_,
                                      ctypes.byref(pixelbuf), pitch)
    if retval == -1:
        raise SDLError()
    return pixelbuf


@sdltype("SDL_RenderPresent", [ctypes.POINTER(SDL_Renderer)], None)
def render_present(renderer):
    """TODO
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    dll.SDL_RenderPresent(ctypes.byref(renderer))


@sdltype("SDL_DestroyTexture", [ctypes.POINTER(SDL_Texture)], None)
def destroy_texture(texture):
    """TODO
    """
    if not isinstance(texture, SDL_Texture):
        raise TypeError("texture is not a SDL_Texture")
    dll.SDL_DestroyTexture(ctypes.byref(texture))


@sdltype("SDL_DestroyRenderer", [ctypes.POINTER(SDL_Renderer)], None)
def destroy_renderer(renderer):
    """TODO
    """
    if not isinstance(renderer, SDL_Renderer):
        raise TypeError("renderer is not a SDL_Renderer")
    dll.SDL_DestroyRenderer(ctypes.byref(renderer))
