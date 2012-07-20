.. module:: pygame2.sdlttf
   :synopsis: SDL2_ttf library wrapper

:mod:`pygame2.sdlttf` - SDL2_ttf library wrapper
====================================================

The :mod:`pygame2.sdlttf` module is a :mod:`ctypes`-based wrapper
around the SDL2_image library. It wraps nearly all publicly accessible
structures and functions of the SDL2_ttf library to be accessible from
Python code.

A detailled documentation about the behaviour of the different functions
can found within the `SDL2_ttf documentation <http://www.libsdl.org>`_.
The API documentation of :mod:`pygame2.ttf` will focus on a brief
description and outlines noteworthy specialities or - where necessary -
differences for Python.

SDL2_ttf API
------------

.. class:: TTF_Font

   A font object to be used for rendering text via :mod:`pygame2.sdlttf`.

.. function:: init() -> int

   Initializes the SDL2_ttf library.

   This wraps :c:func:`TTF_Init`.

.. function:: quit() -> None

   Shuts down the SDL2_ttf library and releases all resources held by it.
   Calling SDL2_ttf related methods after quit() will wake the dragons, so
   do not do it.

   This wraps :c:func:`TTF_Quit`.

.. function:: open_font(fname : string, ptsize : int) -> TTF_Font

   Opens a TTF font file with a defined size in points.

   Raises a :exc:`pygame2.sdl.SDLError`, if the font could not be loaded.

   This wraps :c:func:`TTF_OpenFont`.

.. function:: open_font_index(fname : string, ptsize : int, \
                              idx : int) -> TTF_Font

   Opens a TTF font file with a defined size in points, using the
   font type specified by *idx*.

   Raises a :exc:`pygame2.sdl.SDLError`, if the font could not be loaded.

   This wraps :c:func:`TTF_OpenFontIndex`.

.. function:: open_font_rw(src : SDL_RWops, freesrc : bool, \
                           ptsize : int) -> TTF_Font

   Opens a TTF font file from a seekable data stream with a defined
   size in points.

   Raises a :exc:`pygame2.sdl.SDLError`, if the font could not be loaded.

   This wraps :c:func:`TTF_OpenFontRW`.

.. function:: open_font_index_rw(src : SDL_RWops, freesrc : bool, \
                                 ptsize : int, idx : int) -> TTF_Font

   Opens a TTF font file using the font type specified by *idx* from a
   seekable data stream.

   Raises a :exc:`pygame2.sdl.SDLError`, if the font could not be loaded.

   This wraps :c:func:`TTF_OpenFontIndexRW`.

.. function:: get_font_style(font : TTF_Font) -> int

   Gets the style of the font as ``TTF_STYLE_*`` combination.

   This wraps :c:func:``TTF_GetFontStyle``.

.. function:: set_font_style(font : TTF_Font, style : int) -> None

   Sets the style to be used for the passed *font*.

   This wraps :c:func:`TTF_SetFontStyle`.

.. function:: get_font_outline(font : TTF_Font) -> int

   Get the outline width of the passed *font*.

   This wraps :c:func:`TTF_GetFontOutline`.

.. function:: set_font_outline(font : TTF_Font, outline : int) -> int

   Set the outline width for the passed *font* in pixels.

   This wraps :c:func:`TTF_SetFontOutline`.

.. function:: get_font_hinting(font : TTF_Font) -> int

   Get the current hinting setting for the passed *font*.

   This wraps :c:func:`TTF_GetFontHinting`.

.. function:: set_font_hinting(font : TTF_Font, hinting : int) -> int

   Set the hinting for the passed *font*. *hinting* must be a value of the
   ``TTF_HINTING_*`` constants.

   This wraps :c:func:`TTF_SetFontHinting`.

.. function:: font_height(font : TTF_Font) -> int

   Gets the height of the font in pixels. This will return the maximum
   height of the font, based on the maximum pixel height of all glyphs.

   This wraps :c:func:`TTF_FontHeight`.

.. function:: font_ascent(font :TTF_Font) -> int

   Get the maximum ascent of the font, based on the maximum ascent of
   all glyphs. The ascent is the difference between the top-most point
   of the font glyphs and the baseline.

   This wraps :c:func:`TTF_FontAscent`.

.. function:: font_descent(font : TTF_Font) -> int

   Get the maximum descent of the font, based on the maximum descent of
   all glyphs. The descent is the different between the bottom-most
   point of the font glyphs and the baseline.

   This wraps :c:func:`TTF_FontDescent`.

.. function:: font_line_skip(font : TTF_Font) -> int

   Get the recommended pixel height for line spacing.

   This wraps :c:func:`TTF_FontLineSkip`.

.. function:: get_font_kerning(font : TTF_Font) -> bool

   Get, whether kerning is allowed for the font.

   This wraps :c:func:`TTF_GetFontKerning`.

.. function:: set_font_kerning(font : TTF_Font[, allowed=True]) -> None

   Enable or disable the kerning of the font.

   This wraps :c:func:`TTF_SetFontKerning`.

.. function:: font_faces(font : TTF_Font) -> int

   Get the number of faces of the font.

   This wraps :c:func:`TTF_FontFaces`.

.. function:: font_face_is_fixed_width(font : TTF_Font) -> bool

   Get, whether the current font face is a fixed width font (monospace).

   This wraps :c:func:`TTF_FontFaceIsFixedWidth`.

.. function:: font_face_family_name(font : TTF_Font) -> string

   Get the current font face family name.

   This wraps :c:func:`TTF_FontFaceFamilyName`.

.. function:: font_face_style_name(font : TTF_Font) -> string

   Gets the current font face syle name.

   This wraps :c:func:`TTF_FontFaceStyleName`.

.. function:: glyph_is_provided(font : TTF_Font, ch : string) -> int

   Checks, if a glyph is provided for the passed character. Returns the index
   of the glyph in the font or 0, if not found.

   This wraps :c:func:`TTF_GlyphIsProvided`.

.. function:: glyph_metrics(font : TTF_Font, ch : string) \
              -> (int, int, int, int, int)

   TODO

   This wraps :c:func:`TTF_GlyphMetrics`.

.. function:: size(font : TTF_Font, s : string) -> (int, int)

   TODO

   This wraps :c:func:`TTF_SizeUTF8`.

.. function:: render_solid(font : TTF_Font, s : string, \
                           color : SDL_Color) -> SDL_Surface

   TODO

   This wraps :c:func:`TTF_RenderUTF8_Solid`.

.. function:: render_shaded(font : TTF_Font, s : string, fg : SDL_Color, \
                            bg : SDL_Color) -> SDL_Surface

   TODO

   This wraps :c:func:`TTF_RenderUTF8_Shaded`.

.. function:: render_blended(font : TTF_Font, s : string, \
                             color : SDL_Color) -> SDL_Surface



   This wraps :c:func:`TTF_RenderUTF8_Blended`.

.. function:: get_kerning_size(font : TTF_Font, prev_index : int, \
                               index : int) -> int

   TODO

   This wraps :c:func:`TTF_GetFontKerningSize`.

.. function:: close_font(font : TTF_Font) -> None

   TODO

   This wraps :c:func:`TTF_CloseFont`.

.. function:: close_font(font : TTF_Font) -> None

   Close an opened font file.

   This wraps :c:func:`TTF_CloseFont`.
