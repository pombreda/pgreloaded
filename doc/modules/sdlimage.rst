.. module:: pygame2.sdlimage
   :synopsis: SDL2_image library wrapper

:mod:`pygame2.sdlimage` - SDL2_image library wrapper
====================================================

The :mod:`pygame2.sdlimage` module is a :mod:`ctypes`-based wrapper
around the SDL2_image library. It wraps nearly all publicly accessible
structures and functions of the SDL2_image library to be accessible from
Python code.

A detailled documentation about the behaviour of the different functions
can found within the `SDL2_image documentation <http://www.libsdl.org>`_.
The API documentation of :mod:`pygame2.sdlimage` will focus on a brief
description and outlines noteworthy specialities or - where necessary -
differences for Python.

SDL2_image API
--------------

.. function:: init(flags=IMG_INIT_JPG | IMG_INIT_PNG | IMG_INIT_TIF | \
                   IMG_INIT_WEBP) -> int

   Initializes the SDL2_image library using the passed bit-wise
   combination of image types defined by the ``IMG_INIT_`` constants.

   Legal values are:

   * IMG_INIT_JPG
   * IMG_INIT_PNG
   * IMG_INIT_TIF
   * IMG_INIT_WEBP

   This wraps :c:func:`IMG_Init`.

.. function:: quit() -> None

   Shuts down the SDL2_image library and releases all resources held by
   it. Calling SDL2_image related methods after :func:`quit()` will wake the
   dragons, so do not do it.

   This wraps :c:func:`IMG_Quit`.

.. function:: linked_version() -> SDL_version

   Gets the version of the loaded SDL2_image library.

   This wraps :c:func:`IMG_Linked_Version`.

.. function:: load(fname : string) -> SDL_Surface

   Load an image into a :class:`pygame2.sdl.surface.SDL_Surface` from
   the specified filename. Raises a :exc:`pygame2.sdl.SDLError`, if the
   file could not be loaded.

   This wraps :c:func:`IMG_Load`.

.. function:: load_rw(rwops : SDL_RWops, freesrc : bool) -> SDL_Surface

   Load a surface from a seekable data stream. If *freesrc* evaluates to
   ``True``, the passed stream will be closed after being read.

   This wraps :c:func:`IMG_Load_RW`.

.. function:: load_typed_rw(rwops : SDL_RWops, freesrc : bool, \
                            itype : string) -> SDL_Surface

   Load a surface from a seekable data stream. *itype* specifies the
   image format to use for loading and may be a value of **BMP**,
   **GIF**, **PNG**, etc. If *freesrc* evaluates to ``True``, the passed
   stream will be closed after being read.

   Raises a :exc:`pygame2.sdl.SDLError`, if the image could not be loaded.

   This wraps :c:func:`IMG_LoadTyped_RW`.

.. function:: load_texture(renderer : SDL_Renderer, fname : string) \
              -> SDL_Texture

   Create a :class:`pygame2.sdl.render.SDL_Texture` from the specified
   filename. Raises a :exc:`pygame2.sdl.SDLError`, if the file could not
   be loaded.

   This wraps :c:func:`IMG_LoadTexture`.

.. function:: load_texture_rw(renderer : SDL_Renderer, src : SDL_RWops, \
                              freesrc : bool) -> SDL_Texture

   Create a :class:`pygame2.sdl.render.SDL_Texture` from a seekable data
   stream. If *freesrc* evaluates to ``True``, the passed stream will be
   closed after being read. Raises a :exc:`pygame2.sdl.SDLError`, if the
   image could not be loaded.

   This wraps :c:func:`IMG_LoadTexture_RW`.

.. function:: load_texture_typed_rw(renderer : SDL_Renderer, \
                                    src : SDL_RWops, freesrc : bool, \
                                    itype : string) -> SDL_Texture

   Create a :class:`pygame2.sdl.render.SDL_Texture` from a seekable data
   stream. *itype* specifies the image format to use for loading and may
   be a value of **BMP**, **GIF**, **PNG**, etc. If *freesrc* evaluates
   to ``True``, the passed stream will be closed after being read.
   Raises a :exc:`pygame2.sdl.SDLError`, if the image could not be loaded.

   This wraps :c:func:`IMG_LoadTextureTyped_RW`.

.. function:: is_ico(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents ICO image data

   This wraps :c:func:`IMG_isICO`.

.. function:: is_cur(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents CUR image data

   This wraps :c:func:`IMG_isCUR`.

.. function:: is_bmp(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents BMP image data

   This wraps :c:func:`IMG_isBMP`.

.. function:: is_gif(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents GIF image data

   This wraps :c:func:`IMG_isGIF`.

.. function:: is_jpg(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents JPG image data

   This wraps :c:func:`IMG_isJPG`.

.. function:: is_lbm(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents LBM image data

   This wraps :c:func:`IMG_isLBM`.

.. function:: is_pcx(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents PCX image data

   This wraps :c:func:`IMG_isPCX`.

.. function:: is_png(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents PNG image data

   This wraps :c:func:`IMG_isPNG`.

.. function:: is_pnm(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents PNM image data

   This wraps :c:func:`IMG_isPNM`.

.. function:: is_tif(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents TIF image data

   This wraps :c:func:`IMG_isTIF`.

.. function:: is_xcf(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents XCF image data

   This wraps :c:func:`IMG_isXCF`.

.. function:: is_webp(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents WEBP image data

   This wraps :c:func:`IMG_isWEBP`.

.. function:: is_xpm(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents XPM image data

   This wraps :c:func:`IMG_isXPM`.

.. function:: is_xv(src : SDL_RWops) -> bool

   Checks, if the passed data stream represents XV image data

   This wraps :c:func:`IMG_isXV`.

.. function:: load_ico_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a ICO data stream.

   This wraps :c:func:`IMG_LoadICO_RW`.

.. function:: load_cur_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a CUR data stream.

   This wraps :c:func:`IMG_LoadCUR_RW`.

.. function:: load_bmp_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a BMP data stream.

   This wraps :c:func:`IMG_LoadBMP_RW`.

.. function:: load_gif_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a GIF data stream.

   This wraps :c:func:`IMG_LoadGIF_RW`.

.. function:: load_jpg_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a JPG data stream.

   This wraps :c:func:`IMG_LoadJPG_RW`.

.. function:: load_lbm_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a LBM data stream.

   This wraps :c:func:`IMG_LoadLBM_RW`.

.. function:: load_pcx_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a PCX data stream.

   This wraps :c:func:`IMG_LoadPCX_RW`.

.. function:: load_png_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a PNG data stream.

   This wraps :c:func:`IMG_LoadPNG_RW`.

.. function:: load_pnm_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a PNM data stream.

   This wraps :c:func:`IMG_LoadPNM_RW`.

.. function:: load_tga_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a TGA data stream.

   This wraps :c:func:`IMG_LoadTGA_RW`.

.. function:: load_tif_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a TIF data stream.

   This wraps :c:func:`IMG_LoadTIF_RW`.

.. function:: load_xcf_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a XCF data stream.

   This wraps :c:func:`IMG_LoadXCF_RW`.

.. function:: load_xpm_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a XPM data stream.

   This wraps :c:func:`IMG_LoadXPM_RW`.

.. function:: load_xv_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a XV data stream.

   This wraps :c:func:`IMG_LoadXV_RW`.

.. function:: load_webp_rw(src : SDL_RWops) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a WEBP data stream.

   This wraps :c:func:`IMG_LoadWEBP_RW`.

.. function:: read_xpm_from_array(xpm : bytes) -> SDL_Surface

   Loads a :class:`pygame2.sdl.surface.SDL_Surface` from a XPM character
   buffer.

   This wraps :c:func:`IMG_ReadXPMFromArray`.
