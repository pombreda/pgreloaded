.. module:: pygame2.sdl.surface
   :synopsis: SDL2 surface wrapper

:mod:`pygame2.sdl.surface` - SDL2 surface wrapper
=================================================

.. class:: SDL_Surface()

   TODO

   .. attribute:: size

      TODO

   .. attribute:: locked

      TODO

   .. attribute:: locked_data

      TODO

   .. attribute:: clip_rect

      TODO

   .. attribute:: format

      TODO

   .. attribute:: pixels

      TODO

   .. attribute:: pitch

      TODO


.. function:: convert_pixels(width : int, height : int, srcformat : int, \
                             src : bytes, srcpitch : int, dstformat : int, \
                             dstpitch : int) -> bytes

   Converts the passed pixel pixel buffer and returns a new buffer. The pixels
   of the passed *src* buffer will be converted from *srcformat* to values of
   *dstformat*. The size of the result buffer will be *height* * *dstpitch*.

   This wraps `SDL_ConvertPixels`.

.. function:: convert_surface(src : SDL_Surface, pformat : SDL_PixelFormat, \
                              flags : int) -> SDL_Surface

   Creates a new surface with the specified format and copies and maps the
   passed *surface* to it.

   This wraps `SDL_ConvertSurface`.

.. function:: convert_surface_format(src : SDL_Surface, \
                                     pformat : SDL_PixelFormat, \
                                     flags : int) -> SDL_Surface

   Creates a new surface with the specified format and copies and maps the
   passed *surface* to it.

   This wraps `SDL_ConvertSurfaceFormat`.

.. function:: create_rgb_surface(width : int, height : int, depth : int[, \
                                 rmask=0[, gmask=0[, bmask=0[, amask=0]]]]) -> SDL_Surface

   Creates a RGB surface. If the *depth* is 4 or 8 bits, an empty palette is
   allocated for the surface. If the *depth* is greater than 8 bits, the pixel
   format is set using the passed RGBA mask.

   This wraps `SDL_CreateRGBSurface`.

.. function:: create_rgb_surface_from(pixels : bytes, width : int, \
                                      height : int, depth : int, pitch : int, \
                                      rmask : int, gmask : int, bmask : int, \
                                      amask : int) -> SDL_Surface

   Creates a RGB surface from a pixel buffer.

   This wraps `SDL_CreateRGBSurfaceFrom`.

.. function:: fill_rect(dst : SDL_Surface, rect : SDL_rect, color : int) -> None

   Fills an area with a certain color on the surface. If *rect* is ``None``,
   the entire surface will be filled.

   This wraps `SDL_FillRect`.

.. function:: fill_rects(dst : SDL_Surface, rects : iterable, color : int) -> None

   Fills multiple areas with a certain color on the surface.

   This wraps `SDL_FillRects`.

.. function:: free_surface(surface : SDL_Surface) -> None

   Frees the resources hold by a surface. Once freed, the surface should not
   be accessed anymore.

   This wraps `SDL_FreeSurface`.

.. function:: get_clip_rect(surface : SDL_Surface) -> SDL_Rect

   Gets the clipping area for blitting operations.

   This wraps `SDL_GetClipRect`.

.. function:: set_clip_rect(surface : SDL_Surface, rect : SDL_Rect) -> bool

   Sets the clipping area for blitting operations.

   This wraps `SDL_SetClipRect`.

.. function:: get_color_key(surface : SDL_Surface) -> int

   Gets the set colorkey for transparent pixels on the surface. If no colorkey
   is set, ``None`` will be returned.

   This wraps `SDL_GetColorKey`.

.. function:: set_color_key(surface : SDL_Surface, flag : int, key : int) -> None

   Sets the colorkey for transparent pixels on the surface. You can pass
   ``SDL_RLEACCEL`` to enable RLE accelerated blits.

   This wraps `SDL_SetColorKey`.

.. function:: get_surface_alpha_mod(surface : SDL_Surface) -> int

   Gets the additional alpha value to be used in blit operations.

   This wraps `SDL_GetSurfaceAlphaMod`.

.. function:: set_surface_alpha_mod(surface : SDL_Surface, alpha : int) -> None

   Sets the additional alpha value used in blit operations.

   This wraps `SDL_SetSurfaceAlphaMod`.

.. function:: set_surface_blend_mode(surface : SDL_Surface, blend : int) -> None

   Sets the blend mode to be used in blit operations.

   This wraps `SDL_SetSurfaceBlendMode`.

.. function:: get_surface_blend_mode(surface : SDL_Surface) -> int

   Gets the blend mode used in blit operations.

   This wraps `SDL_GetSurfaceBlendMode`.

.. function:: get_surface_color_mod(surface : SDL_Surface) -> (int, int, int)

   Gets the additional color value used for blit operations.

   This wraps `SDL_GetSurfaceColorMod`.

.. function:: set_surface_color_mod(surface : SDL_Surface, r : int, g : int, \
                                    b : int) -> None

   Sets the additional color value to be used for blit operations.

   This wraps `SDL_SetSurfaceColorMod`.

.. function:: load_bmp_rw(src : SDL_RWops, freesrc : bool) -> SDL_Surface

   Load a surface from a seekable data stream. If *freesrc* evaluates to
   ``True``, the passed stream will be closed after being read.

   This wraps `SDL_LoadBMP_RW`.

.. function:: load_bmp(filename : string) -> SDL_Surface

   Loads a surface from a BMP file.

   This wraps `SDL_LoadBMP`.

.. function:: save_bmp_rw(surface : SDL_Surface, dst : SDL_RWops, \
                          freedst : bool) -> None

   Saves a surface to a seekable data stream. If *freedst* evaluates to
   ``True``, the passed stream will be closed after being written.

   This wraps `SDL_SaveBMP_RW`.

.. function:: save_bmp(surface : SDL_Surface, filename : string) -> None

   Saves a surface to a file.

   This wraps `SDL_SaveBMP`.

.. function:: lock_surface(surface : SDL_Surface) -> None

   Locks the surface to allow a direct acces to its pixels.

   This wraps `SDL_LockSurface`.

.. function:: SDL_MUSTLOCK(surface : SDL_Surface) -> bool

   Checks, if the surface must be locked prior to access its pixels.

   This wraps `SDL_MUSTLOCK`.

.. function:: unlock_surface(surface : SDL_Surface) -> None

   Unlocks the surface.

   This wraps `SDL_UnlockSurface`.

.. function:: lower_blit(src : SDL_Surface, srcrect : SDL_Rect, \
                         dst : SDL_Surface, dstrect : SDL_Rect) -> None

   TODO

   This wraps `SDL_LowerBlit`.

.. function:: lower_blit_scaled(src : SDL_Surface, srcrect : SDL_Rect, \
                                dst : SDL_Surface, dstrect : SDL_Rect) -> None

   TODO

   This wraps `SDL_LowerBlitScaled`.

.. function:: upper_blit(src : SDL_Surface, srcrect : SDL_Rect, \
                         dst : SDL_Surface, dstrect : SDL_Rect) -> None
              blit_surface(src : SDL_Surface, srcrect : SDL_Rect, \
                           dst : SDL_Surface, dstrect : SDL_Rect) -> None

   TODO

   This wraps `SDL_UpperBlit` and `SDL_BlitSurface`.

.. function:: upper_blit_scaled(src : SDL_Surface, srcrect : SDL_Rect, \
                                dst : SDL_Surface, dstrect : SDL_Rect) -> None

   TODO

   This wraps `SDL_UpperBlitScaled`.

.. function:: soft_stretch(src : SDL_Surface, srcrect : SDL_Rect, \
                           dst : SDL_Surface, dstrect : SDL_Rect) -> None

   TODO

   This wraps `SDL_SoftStretch`.

.. function:: set_surface_palette(surface : SDL_Surface, palette : SDL_Palette) -> None

   Sets the palette used by the surface.

   This wraps `SDL_SetSurfacePalette`.

.. function:: set_surface_rle(surface : SDL_Surface, flag : bool) -> None

   Sets the RLE acceleration hint for the surface. If RLE is enabled,
   colorkey and alpha blending blits are much faster, but the surface
   must be locked before directly accessing the pixels.

   This wraps `SDL_SetSurfaceRLE`.
