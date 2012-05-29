"""
A thin wrapper package around the SDL2_ttf library.
"""
import sys
import ctypes
from pygame2.dll import DLL
from pygame2.sdl import SDL_FALSE, SDL_TRUE, SDLError
from pygame2.compat import byteify, stringify
from pygame2.sdl.surface import SDL_Surface
from pygame2.sdl.rwops import SDL_RWops
from pygame2.sdl.render import SDL_Renderer, SDL_Texture
from pygame2.sdl.pixels import SDL_Color


__all__ = ["init", "quit", "open_font", "open_font_index", "open_font_rw",
           "open_font_index_rw", "get_font_style", "set_font_style",
           "get_font_outline", "set_font_outline", "get_font_hinting",
           "set_font_hinting", "font_height", "font_ascent", "font_descent",
           "font_line_skip", "get_font_kerning", "set_font_kerning",
           "font_faces", "font_face_is_fixed_width", "font_face_family_name",
           "font_face_style_name", "glyph_is_provided", "glyph_metrics",
           "size", "render_solid", "render_shaded", "render_blended",
           "get_kerning_size", "close_font",
           "TTF_STYLE_NORMAL", "TTF_STYLE_BOLD", "TTF_STYLE_ITALIC",
           "TTF_STYLE_UNDERLINE", "TTF_STYLE_STRIKETHROUGH",
           "TTF_HINTING_NORMAL", "TTF_HINTING_LIGHT", "TTF_HINTING_MONO",
           "TTF_HINTING_NONE"
           ]


dll = DLL("SDL2_ttf", ["SDL2_ttf"])
sdlttftype = dll.get_decorator()

SDL_Surface_p = ctypes.POINTER(SDL_Surface)
SDL_RWops_p = ctypes.POINTER(SDL_RWops)
c_int_p = ctypes.POINTER(ctypes.c_int)


class TTF_Font(ctypes.Structure):
    pass


TTF_Font_p = ctypes.POINTER(TTF_Font)


def _check_ptr(ret):
    if ret is None or not bool(ret):
        raise SDLError()
    return ret.contents


def _check_int(ret):
    if ret != 0:
        raise SDLError()
    return


# Set and retrieve the font style
TTF_STYLE_NORMAL        = 0x00
TTF_STYLE_BOLD          = 0x01
TTF_STYLE_ITALIC        = 0x02
TTF_STYLE_UNDERLINE     = 0x04
TTF_STYLE_STRIKETHROUGH = 0x08

# Set and retrieve FreeType hinter settings
TTF_HINTING_NORMAL = 0
TTF_HINTING_LIGHT  = 1
TTF_HINTING_MONO   = 2
TTF_HINTING_NONE   = 3


@sdlttftype("TTF_Init", None, ctypes.c_int)
def init():
    """ Initializes the SDL2_ttf library. """
    return _check_int(dll.TTF_Init())


@sdlttftype("TTF_Quit", None, None)
def quit():
    """Shuts down the SDL2_ttf library and releases all resources held by it.

    Calling SDL2_ttf related methods after quit() will wake the dragons, so
    do not do it.
    """
    dll.TTF_Quit()


@sdlttftype("TTF_OpenFont", [ctypes.c_char_p, ctypes.c_int], TTF_Font_p)
def open_font(fname, ptsize):
    """Opens a TTF font file with a defined size in points.

    Raises a SDLError, if the font could not be loaded.
    """
    return _check_ptr(dll.TTF_OpenFont(fname, ptsize))


@sdlttftype("TTF_OpenFontIndex", [ctypes.c_char_p, ctypes.c_int,
                                  ctypes.c_long], TTF_Font_p)
def open_font_index(fname, ptsize, idx):
    """Opens a TTF font file with a defined size in points, using the
    font type specified by idx.

    Raises a SDLError, if the font could not be loaded.
    """
    return _check_ptr(dll.TTF_OpenFontIndex(fname, ptsize, idx))


@sdlttftype("TTF_OpenFontRW", [SDL_RWops_p, ctypes.c_int, ctypes.c_int],
            TTF_Font_p)
def open_font_rw(src, freesrc, ptsize):
    """Opens a TTF font file from a seekable data stream with a defined
    size in points.

    Raises a SDLError, if the font could not be loaded.
    """
    if not isinstance(src, SDL_Rwops):
        raise TypeError("src must be a SDL_RWops")
    if bool(freesrc):
        freesrc = 1
    else:
        freesrc = 0
    return _check_ptr(dll.TTF_OpenFontRW(ctypes.byref(src), freesrc, ptsize))


@sdlttftype("TTF_OpenFontIndexRW", [SDL_RWops_p, ctypes.c_int, ctypes.c_int,
                                    ctypes.c_long], TTF_Font_p)
def open_font_index_rw(src, freesrc, ptsize, idx):
    """Opens a TTF font file using the font type specified by idx from a
    seekable data stream.

    Raises a SDLError, if the font could not be loaded.
    """
    if not isinstance(src, SDL_Rwops):
        raise TypeError("src must be a SDL_RWops")
    if bool(freesrc):
        freesrc = 1
    else:
        freesrc = 0
    return _check_ptr(dll.TTF_OpenFontIndexRW(ctypes.byref(src), freesrc,
                                              ptsize, idx))


@sdlttftype("TTF_GetFontStyle", [TTF_Font_p], ctypes.c_int)
def get_font_style(font):
    """Gets the style of the font as TTF_STYLE_* combination."""
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    retval = dll.TTF_GetFontStyle(ctypes.byref(font))
    if retval < 0:
        raise SDLError()
    return retval


@sdlttftype("TTF_SetFontStyle", [TTF_Font_p, ctypes.c_int], None)
def set_font_style(font, style):
    """Sets the style to be used for the passed font."""
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    retval = dll.TTF_SetFontStyle(ctypes.byref(font), style)
    if retval < 0:
        raise SDLError()
    return retval


@sdlttftype("TTF_GetFontOutline", [TTF_Font_p], ctypes.c_int)
def get_font_outline(font):
    """ extern DECLSPEC int SDLCALL TTF_GetFontOutline(const TTF_Font
    *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_GetFontOutline(ctypes.byref(font))


@sdlttftype("TTF_SetFontOutline", [TTF_Font_p, ctypes.c_int], None)
def set_font_outline(font, outline):
    """ extern DECLSPEC void SDLCALL TTF_SetFontOutline(TTF_Font *font,
    int outline); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_SetFontOutline(ctypes.byref(font), outline)


@sdlttftype("TTF_GetFontHinting", [TTF_Font_p], ctypes.c_int)
def get_font_hinting(font):
    """ extern DECLSPEC int SDLCALL TTF_GetFontHinting(const TTF_Font
    *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_GetFontHinting(ctypes.byref(font))


@sdlttftype("TTF_SetFontHinting", [TTF_Font_p, ctypes.c_int], None)
def set_font_hinting(font, hinting):
    """ extern DECLSPEC void SDLCALL TTF_SetFontHinting(TTF_Font *font,
    int hinting); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_SetFontHinting(ctypes.byref(font), style)


@sdlttftype("TTF_FontHeight", [TTF_Font_p], ctypes.c_int)
def font_height(font):
    """ /* Get the total height of the font - usually equal to point
        size */ extern DECLSPEC int SDLCALL TTF_FontHeight(const
        TTF_Font *font);"""
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_FontHeight(ctypes.byref(font))


@sdlttftype("TTF_FontAscent", [TTF_Font_p], ctypes.c_int)
def font_ascent(font):
    """ /* Get the offset from the baseline to the top of the font
           This is a positive value, relative to the baseline.
         */
        extern DECLSPEC int SDLCALL TTF_FontAscent(const TTF_Font *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_FontAscent(ctypes.byref(font))


@sdlttftype("TTF_FontDescent", [TTF_Font_p], ctypes.c_int)
def font_descent(font):
    """ /* Get the offset from the baseline to the bottom of the font
           This is a negative value, relative to the baseline.
         */
        extern DECLSPEC int SDLCALL TTF_FontDescent(const TTF_Font *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_FontDescent(ctypes.byref(font))


@sdlttftype("TTF_FontLineSkip", [TTF_Font_p], ctypes.c_int)
def font_line_skip(font):
    """ /* Get the recommended spacing between lines of text for this font */
        extern DECLSPEC int SDLCALL TTF_FontLineSkip(const TTF_Font *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_FontLineSkip(ctypes.byref(font))


@sdlttftype("TTF_GetFontKerning", [TTF_Font_p], ctypes.c_int)
def get_font_kerning(font):
    """ /* Get/Set whether or not kerning is allowed for this font */
        extern DECLSPEC int SDLCALL TTF_GetFontKerning(const TTF_Font
        *font);"""
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_GetFontKerning(ctypes.byref(font))


@sdlttftype("TTF_SetFontKerning", [TTF_Font_p, ctypes.c_int], None)
def set_font_kerning(font, allowed):
    """ extern DECLSPEC void SDLCALL TTF_SetFontKerning(TTF_Font *font,
    int allowed); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    dll.TTF_SetFontKerning(ctypes.byref(font), allowed)


@sdlttftype("TTF_FontFaces", [TTF_Font_p], ctypes.c_int)
def font_faces(font):
    """ /* Get the number of faces of the font */
        extern DECLSPEC long SDLCALL TTF_FontFaces(const TTF_Font *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_FontFaces(ctypes.byref(font))


@sdlttftype("TTF_FontFaceIsFixedWidth", [TTF_Font_p], ctypes.c_int)
def font_face_is_fixed_width(font):
    """ /* Get the font face attributes, if any */ extern DECLSPEC int
        SDLCALL TTF_FontFaceIsFixedWidth(const TTF_Font *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_FontFaceIsFixedWidth(ctypes.byref(font)) == 1


@sdlttftype("TTF_FontFaceFamilyName", [TTF_Font_p], ctypes.c_char_p)
def font_face_family_name(font):
    """ extern DECLSPEC char * SDLCALL TTF_FontFaceFamilyName(const
    TTF_Font *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_FontFaceFamilyName(ctypes.byref(font))


@sdlttftype("TTF_FontFaceStyleName", [TTF_Font_p], ctypes.c_char_p)
def font_face_style_name(font):
    """ extern DECLSPEC char * SDLCALL TTF_FontFaceStyleName(const
    TTF_Font *font); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_FontFaceStyleName(ctypes.byref(font))


@sdlttftype("TTF_GlyphIsProvided", [TTF_Font_p, ctypes.c_uint16], ctypes.c_int)
def glyph_is_provided(font, ch):
    """ /* Check whether a glyph is provided by the font or not */
        extern DECLSPEC int SDLCALL TTF_GlyphIsProvided(const TTF_Font
        *font, Uint16 ch);"""
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_GlyphIsProvided(ctypes.byref(font), ch)


@sdlttftype("TTF_GlyphMetrics", [TTF_Font_p, ctypes.c_uint16, c_int_p,
                                 c_int_p,  c_int_p,  c_int_p,  c_int_p],
            ctypes.c_int)
def glyph_metrics(font, ch):
    """ /* Get the metrics (dimensions) of a glyph To understand what
           these metrics mean, here is a useful link:
           http://freetype.sourceforge.net/freetype2/docs/tutorial/step2.html
           */ extern DECLSPEC int SDLCALL TTF_GlyphMetrics(TTF_Font
           *font, Uint16 ch, int *minx, int *maxx, int *miny, int *maxy,
           int *advance);"""
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    minx, maxx, miny, maxy, advance = ctypes.c_int(0), ctypes.c_int(0), \
        ctypes.c_int(0), ctypes.c_int(0), ctypes.c_int(0)
    _check_int(dll.TTF_GlyphMetrics(ctypes.byref(font), ch,
                                    ctypes.byref(minx),
                                    ctypes.byref(maxx),
                                    ctypes.byref(miny),
                                    ctypes.byref(maxy),
                                    ctypes.byref(advance)))
    return (minx.value, maxx.value, miny.value, maxy.value, advance.value)


@sdlttftype("TTF_SizeUTF8", [TTF_Font_p, ctypes.c_char_p, c_int_p, c_int_p],
            ctypes.c_int)
def size(font, s):
    """ /* Get the dimensions of a rendered string of text */ extern
        DECLSPEC int SDLCALL TTF_SizeUTF8(TTF_Font *font, const char
        *text, int *w, int *h);

        this wrapper expects a string object; returns tuple(w, h)
    """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    w = ctypes.c_int(0)
    h = ctypes.c_int(0)
    _check_int(dll.TTF_SizeUTF8(ctypes.byref(font), s.encode('utf-8'),
                                ctypes.byref(w), ctypes.byref(h)))
    return (w.value, h.value)


@sdlttftype("TTF_RenderUTF8_Solid", [TTF_Font_p, ctypes.c_char_p, SDL_Color],
            SDL_Surface_p)
def render_solid(font, s, color):
    """ /* Create an 8-bit palettized surface and render the given text
           at fast quality with the given font and color.  The 0 pixel
           is the colorkey, giving a transparent background, and the 1
           pixel is set to the text color.  This function returns the
           new surface, or NULL if there was an error.  */ extern
           DECLSPEC SDL_Surface * SDLCALL TTF_RenderUTF8_Solid(TTF_Font
           *font, const char *text, SDL_Color fg);"""
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    if not isinstance(color, SDL_Color):
        raise TypeError("color must be a SDL_Color")
    return _check_ptr(dll.TTF_RenderUTF8_Solid(ctypes.byref(font),
                                               s.encode("utf-8"), color))


@sdlttftype("TTF_RenderUTF8_Shaded", [TTF_Font_p, ctypes.c_char_p, SDL_Color,
                                      SDL_Color], SDL_Surface_p)
def render_shaded(font, s, fg, bg):
    """ /* Create an 8-bit palettized surface and render the given text
           at high quality with the given font and colors.  The 0 pixel
           is background, while other pixels have varying degrees of the
           foreground color.  This function returns the new surface, or
           NULL if there was an error.  */ extern DECLSPEC SDL_Surface *
           SDLCALL TTF_RenderUTF8_Shaded(TTF_Font *font, const char
           *text, SDL_Color fg, SDL_Color bg);
         """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    if not isinstance(fg, SDL_Color):
        raise TypeError("fg must be a SDL_Color")
    if not isinstance(bg, SDL_Color):
        raise TypeError("bg must be a SDL_Color")
    return _check_ptr(dll.TTF_RenderUTF8_Shaded(ctypes.byref(font),
                                                s.encode("utf-8"), fg, bg))


@sdlttftype("TTF_RenderUTF8_Blended", [TTF_Font_p, ctypes.c_char_p, SDL_Color],
            SDL_Surface_p)
def render_blended(font, s, color):
    """ /* Create a 32-bit ARGB surface and render the given text at
           high quality, using alpha blending to dither the font with
           the given color.  This function returns the new surface, or
           NULL if there was an error.  */ extern DECLSPEC SDL_Surface *
           SDLCALL TTF_RenderUTF8_Blended(TTF_Font *font, const char
           *text, SDL_Color fg);
         """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    if not isinstance(color, SDL_Color):
        raise TypeError("color must be a SDL_Color")
    return _check_ptr(dll.TTF_RenderUTF8_Blended(ctypes.byref(font),
                                                 s.encode("utf-8"), color))


@sdlttftype("TTF_GetFontKerningSize", [TTF_Font_p, ctypes.c_int, ctypes.c_int],
            ctypes.c_int)
def get_kerning_size(font, prev_index, index):
    """ /* Get the kerning size of two glyphs */ extern DECLSPEC int
        TTF_GetFontKerningSize(TTF_Font *font, int prev_index, int
        index); """
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    return dll.TTF_GetFontKerningSize(ctypes.byref(font), prev_index, index)


@sdlttftype("TTF_CloseFont", [TTF_Font_p], None)
def close_font(font):
    """Close an opened font file."""
    if not isinstance(font, TTF_Font):
        raise TypeError("font must be a TTF_Font")
    dll.TTF_CloseFont(ctypes.byref(font))