.. module:: pygame2.sdl.pixels
   :synopsis: SDL2 pixel access wrapper

:mod:`pygame2.sdl.pixels` - SDL2 pixel access wrapper
=====================================================

.. function:: SDL_FOURCC(a : string, b : string, c : string, d : string) -> int
              SDL_DEFINE_PIXELFOURCC(a : string, b : string, c : string, d : string) -> int

   Calculates the four character code ordinal value of the passed characters.

   This wraps `SDL_FOURCC`.

.. function:: SDL_DEFINE_PIXELFORMAT(ptype : int, order : int, layout : int, \
                                     bits : int, pbytes : int) -> int

   Calculates a unique pixel format identifier based on the passed values.

   This wraps `SDL_DEFINE_PIXELFORMAT`.

.. function:: SDL_PIXELTYPE(x : int) -> int

   Determines the ``SDL_PIXELTYPE_*`` value for the passed format value.

   This wraps `SDL_PIXELTYPE`.

.. function:: SDL_PIXELORDER(x : int) -> int

   Determines the pixel order value for the passed format value. The return
   value will be one of

   * ``SDL_ARRAYORDER_*``
   * ``SDL_PACKEDORDER_*``
   * ``SDL_BITMAPORDER_*``

   This wraps `SDL_PIXELORDER`.

.. function:: SDL_PIXELLAYOUT(x : int) -> int

   Determines the ``SDL_PACKEDLAYOUT_*`` value for the passed format value.

   This wraps `SDL_PIXELLAYOUT`.

.. function:: SDL_BITSPERPIXEL(x : int) -> int

   Determines the bits per pixel for the passed format value.

   This wraps `SDL_BITSPERPIXEL`.

.. function:: SDL_BYTESPERPIXEL(x : int) -> int

   Determines the bytes per pixel for the passed format value.

   This wraps `SDL_BYTESPERPIXEL`.

.. function:: SDL_ISPIXELFORMAT_INDEXED(pformat : int) -> bool

   Checks, if the passed format value is an indexed format.

   This wraps `SDL_ISPIXELFORMAT_INDEXED`.

.. function:: SDL_ISPIXELFORMAT_ALPHA(pformat : int) -> bool

   Checks, if the passed format value is an alpha channel supporting format.

   This wraps `SDL_ISPIXELFORMAT_ALPHA`.

.. function:: SDL_ISPIXELFORMAT_FOURCC(pformat : int) -> bool

   Checks, if the passed format value is a FourCC based format.

   This wraps `SDL_ISPIXELFORMAT_FOURCC`.

.. class:: SDL_Color(r=255, g=255, b=255)
           SDL_Colour(r=255, g=255, b=255)

   A simple RGB color class.

   This wraps `SDL_Color`.

   .. attribute:: r

      The red value of the color.

   .. attribute:: g

      The green value of the color.

   .. attribute:: b

      The blue value of the color.

.. class:: SDL_Palette()

   A color palette class.

   This wraps `SDL_Palette`.

   .. attribute:: ncolors

      The number of colors in the palette

   .. attribute:: colors

      The colors contained in the palette as array of :class:`SDL_Color` items.

.. class:: SDL_PixelFormat

   A SDL pixel format class.

   This wraps `SDL_PixelFormat`.

   .. attribute:: format

      TODO

   .. attribute:: palette

      TODO

   .. attribute:: next

      TODO

   .. attribute:: BitsPerPixel

      TODO

   .. attribute:: BytesPerPixel

      TODO

   .. attribute:: Rmask

      TODO

   .. attribute:: Gmask

      TODO

   .. attribute:: Bmask

      TODO

   .. attribute:: Amask

      TODO

   .. attribute:: Rloss

      TODO

   .. attribute:: Gloss

      TODO

   .. attribute:: Bloss

      TODO

   .. attribute:: Aloss

      TODO

   .. attribute:: Rshift

      TODO

   .. attribute:: Gshift

      TODO

   .. attribute:: Bshift

      TODO

   .. attribute:: Ashift

      TODO

.. function:: get_pixelformat_name(pformat : int) -> string

   Gets the name of a specific pixel format value.

   This wraps `SDL_GetPixelFormatName`.

.. function:: pixelformat_enum_to_masks(pformat : int) -> (int, int, int, int, int)

   Gets the pixel masks for a specific pixel format value. The returned tuple
   consists of ``(bpp, red mask, green mask, blue mask, alpha mask)``.

   This wraps `SDL_PixelFormatEnumToMasks`.

.. function:: masks_to_pixelformat_enum(bpp : int, rmask : int, gmask : int, \
                                        bmask : int, amask : int) -> int

   Gets the format for a set of pixel mask information.

   This wraps `SDL_MasksToPixelFormatEnum`.

.. function:: alloc_format(pformat : int) -> SDL_PixelFormat

   Creates a SDL_PixelFormat from the passed format value. In case the passed
   format value is not valid or an error occurs on creation, a
   :exc:`pygame2.sdl.SDLError` is raised.

   Once not used anymore, the :class:`SDL_PixelFormat` must be freed using
   :func:`free_format()`.

   This wraps `SDL_AllocFormat`.

.. function:: free_format(pformat : SDL_PixelFormat) -> None

   Frees a previously allocated :class:`SDL_PixelFormat`.

   This wraps `SDL_FreeFormat`.

.. function:: alloc_palette(ncolors : int) -> SDL_Palette

   Creates a :class:`SDL_Palette` with *ncolors* number of colors. Once not
   used anymore, the :class:`SDL_Palette` must be freed using
   :func:`free_palette()`.

   This wraps `SDL_AllocPalette`.

.. function:: free_palette(palette : SDL_Palette) -> None

   Frees a previously allocated :class:`SDL_Palette`.

   This wraps `SDL_FreePalette`.

.. function:: calculate_gamma_ramp(gamma : float) -> (int, int, int, ...)

   Calculates a set of 256 gamma values for a value in the range [0.0; 1.0].

   This wraps `SDL_CalculateGammaRamp`.

.. function:: get_rgb(pixel : int, pformat : SDL_PixelFormat) -> (int, int, int)

   Gets the mapped RGB values for a specific pixel value and format.

   This wraps `SDL_GetRGB`.

.. function:: get_rgba(pixel : int, pformat : SDL_PixelFormat) -> (int, int, int, int)

   Gets the mapped RGBA values for a specific pixel value and format.

   This wraps `SDL_GetRGBA`.

.. function:: map_rgb(pformat : SDL_PixelFormat, r : int, g : int, b : int) -> int

   Maps the passed RGB values to a specific pixel value using the passed format.

   This wraps `SDL_MapRGB`.

.. function:: map_rgba(pformat : SDL_PixelFormat, r : int, g : int, b : int, a : int) -> int

   Maps the passed RGBA values to a specific pixel value using the passed
   format.

   This wraps `SDL_MapRGBA`.

.. function:: set_palette_colors(palette : SDL_Palette, colors : iterable[, \
                                 first=0[, ncolors=0]]) -> int

   Sets the colors of a :class:`SDL_Palette` to the passed values, starting
   at *first* in the *colors* array and setting *ncolors*.

   This wraps `SDL_SetPaletteColors`.

.. function:: set_pixelformat_palette(pformat : SDL_PixelFormat, palette : SDL_Palette) -> int

   Binds a palette to the passed SDL_PixelFormat.

   This wraps `SDL_SetPixelFormatPalette`.
