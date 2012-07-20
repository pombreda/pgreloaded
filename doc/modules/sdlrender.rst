.. module:: pygame2.sdl.render
   :synopsis: SDL2 rendering wrapper

:mod:`pygame2.sdl.render` - SDL2 rendering wrapper
==================================================

.. class:: SDL_RendererInfo()

   TODO

   This wraps `SDL_RendererInfo`.

   .. attribute:: name

      The name of the rendering context driver.

   .. attribute:: flags

      TODO

   .. attribute:: num_texture_formats

      TODO

   .. attribute:: texture_formats

      TODO

   .. attribute:: max_texture_width

      TODO

   .. attribute:: max_texture_height

      TODO

.. class:: SDL_Renderer()

   TODO

   This wraps `SDL_Renderer`.

.. class:: SDL_Texture()

   TODO

   This wraps `SDL_Texture`.

.. function:: get_num_render_drivers() -> int

   Gets the number of 2D renderering drivers available for the current display.

   This wraps `SDL_GetNumRenderDrivers`.

.. function:: get_render_driver_info(index : int) -> SDL_RendererInfo

   Retrieves information about a 2D rendering driver for the current display.
   Returns a :class:`SDL_RendererInfo` on success and raises a
   :exc:`pygame2.sdl.SDLError` on failure.

   This wraps `SDL_GetRenderDriverInfo`.

.. function:: create_window_and_renderer(width : int, height : int, \
                                         windowflags : int) -> (SDL_Window, SDL_Renderer)

   Creates a :class:`pygame2.sdl.video.SDL_Window` and a default renderer for
   the window and returns them as tuple. Raises a :exc:`pygame2.sdl.SDLError`
   on failure.

   This wraps `SDL_CreateWindowAndRenderer`.

.. function:: create_renderer(window : SDL_Window, index : int, flags : int) -> SDL_Renderer

   Creates a 2D rendering context for a :class:`pygame2.sdl.video.SDL_Window`.
   *index* denotes the index if the rendering driver to initialize, or -1 to
   initialize the first one supporting the requested flags.

   Raises a :exc:`pygame2.sdl.SDLError` on failure.

   This wraps `SDL_CreateRenderer`.

.. function:: create_software_renderer(surface : SDL_Surface) -> SDL_Renderer

   Creates a 2D software rendering context for a *surface*. Raises a
   :exc:`pygame2.sdl.SDLError` on failure.

   This wraps `SDL_CreateSoftwareRenderer`.

.. function:: get_renderer(window : SDL_Window) -> SDL_Renderer

   Retrieves the rendering context for the passed *window*. If no renderer
   exists, ``None`` will be returned.

   This wraps `SDL_GetRenderer`.

.. function:: get_renderer_info(renderer : SDL_Renderer) -> SDL_RendererInfo

   Retrieves the information about a rendering context. Raises a
   :exc:`pygame2.sdl.SDLError` on failure.

   This wraps `SDL_GetRendererInfo`.

.. function:: create_texture(renderer : SDL_Renderer, format_ : int, \
                             access : int, w : int, h : int) -> SDL_Texture

   Creates a texture for the specified rendering context.

   Raises an error, if the format is unsupported or the width and height are
   out of range.

   This wraps `SDL_CreateTexture`.

.. function:: create_texture_from_surface(renderer : SDL_Renderer, \
                                          surface : SDL_Surface) -> SDL_Texture

   Creates a texture from an existing *surface*. The *surface* is not modified
   or freed by this function.

   This wraps `SDL_CreateTextureFromSurface`.

.. function:: query_texture(texture : SDL_Texture) -> (int, int, int, int)

   Queries the attributes of the *texture* and returns them as tuple. This
   returns the texture flags, access mode and width and height.

   This wraps `SDL_QueryTexture`.

.. function:: set_texture_color_mod(texture : SDL_Texture, r : int, g : int, \
                                    b : int) -> None

   Sets the additional color value to be used in render copy operations. The
   color value will be multiplied into copy operations.

   This wraps `SDL_SetTextureColorMod`.

.. function:: get_texture_color_mod(texture : SDL_Texture) -> (int, int, int)

   Gets the additional color value used in render copy operations as RGB tuple.

   This wraps `SDL_GetTextureColorMod`.

.. function:: set_texture_alpha_mod(texture : SDL_Texture, alpha : int) -> None

   Sets the additional alpha value used in render copy operations.

   The alpha value will be multiplied into copy operations.

   This wraps `SDL_SetTextureAlphaMod`.

.. function:: get_texture_alpha_mod(texture : SDL_Texture) -> int

   Gets the additional alpha value used in render copy operations.

   This wraps `SDL_GetTextureAlphaMod`.

.. function:: set_texture_blend_mode(texture : SDL_Texture, mode : int) -> None

   Sets the blend mode to be used for textures copy operations.

   This wraps `SDL_SetTextureBlendMode`.

.. function:: get_texture_blend_mode(texture : SDL_Texture) -> int

   Gets the blend mode used for texture copy operations.

   This wraps `SDL_GetTextureBlendMode`.

.. function:: update_texture(texture : SDL_Texture, rect : SDL_Rect, \
                             pixels : bytes, pitch : int) -> None

   Update the given *texture* with new *pixel* data. The passed *rect* can be
   ``None``, if the entire texture's pixel data should be updated (see
   :func:`lock_texture()`).

   This wraps `SDL_UpdateTexture`.

.. function:: lock_texture(texture : SDL_texture[, rect=None]) -> (bytes, int)

   Locks a *texture* for pixel access and returns the raw pixel data and pitch.
   If the *rect* argument is ``None``, the entire texture will be locked.
   The texture must have been created with ``SDL_TEXTUREACCESS_STREAMING``.

   This wraps `SDL_LockTexture`.

.. function:: unlock_texture(texture : SDL_texture) -> None

   Unlocks a texture and uploads the changed pixel data to the video memory,
   if necessary.

   This wraps `SDL_UnlockTexture`.

.. function:: render_target_supported(renderer : SDL_Renderer) -> bool

   Determines whether the window of the *renderer* supports the use of render
   targets.

   This wraps `SDL_RenderTargetSupported`.

.. function:: set_render_target(renderer : SDL_Renderer[, texture=None]) -> None

   Sets a *texture* as the current rendering target. If the passed texture is
   ``None``, the default render target will be used. If a :class:`SDL_Texture`
   is passed, it must have been created with the ``SDL_TEXTUREACCESS_TARGET``
   flag.

   This wraps `SDL_SetRenderTarget`.

.. function:: render_set_viewport(renderer : SDL_Renderer[, rect=None]) -> None

   Sets the drawing area for rendering on the current target. If the passed
   :class:`pygame2.sdl.rect.SDL_Rect` is ``None``, the entire target will be
   used as drawing area.

   This wraps `SDL_RenderSetViewport`.

.. function:: render_get_viewport(renderer : SDL_Renderer) -> SDL_Rect

   Gets the drawing area for the current target.

   This wraps `SDL_RenderGetViewport`.

.. function:: set_render_draw_color(renderer : SDL_Renderer, r : int, \
                                    g : int, b : int, a : int) -> None

   Sets the color used for drawing operations (rect, line and clear).

   This wraps `SDL_SetRenderDrawColor`.

.. function:: get_render_draw_color(renderer : SDL_Renderer) -> (int, int, int, int)

   Gets the color used for drawing operations (rect, line and clear) as RGBA
   tuple.

   This wraps `SDL_GetRenderDrawColor`.

.. function:: set_render_draw_blend_mode(renderer : SDL_Renderer, mode : int) -> None

   Sets the blend mode for drawing operations (fill and line).

   This wraps `SDL_SetRenderDrawBlendMode`.

.. function:: get_render_draw_blend_mode(renderer : SDL_Renderer) -> int

   Gets the blend mode for drawing operations (fill and line).

   This wraps `SDL_GetRenderDrawBlendMode`.

.. function:: render_clear(renderer : SDL_Renderer) -> None

   Clears the current rendering target with the set drawing color. This clears
   the entire rendering target, ignoring any set viewport.

   This wraps `SDL_RenderClear`.

.. function:: render_draw_point(renderer : SDL_Renderer, x : int, y : int) -> None

   Draws a point on the current rendering target.

   This wraps `SDL_RenderDrawPoint`.

.. function:: render_draw_points(renderer : SDL_Renderer, points : interable) -> None

   Draws multiple points on the current rendering target.

   This wraps `SDL_RenderDrawPoints`.

.. function:: render_draw_line(renderer : SDL_Renderer, x1 : int, y1 : int, \
                               x2 : int, y2 : int) -> None

   Draws a line on the current rendering target.

   This wraps `SDL_RenderDrawLine`.

.. function:: render_draw_lines(renderer : SDL_Renderer, points : iterable) -> None

   Draws a series of connected lines on the current rendering target.

   This wraps `SDL_RenderDrawLines`.

.. function:: render_draw_rect(renderer : SDL_Renderer[, rect=None]) -> None

   Draws a rectangle on the current rendering target. If the passed *rect* is
   ``None``, the entire rendering target will be outlined.

   This wraps `SDL_RenderDrawRect`.

.. function:: render_draw_rects(renderer : SDL_Renderer, rects : iterable) -> None

   Draw multiple rectangles on the current rendering target.

   This wraps `SDL_RenderDrawRects`.

.. function:: render_fill_rect(renderer : SDL_Renderer[, rect=None]) -> None

   Fill a rectangle on the current rendering target with the set drawing color.
   If the passed *rect* is ``None``, the entire rendering target will be filled.

   This wraps `SDL_RenderFillRect`.

.. function:: render_fill_rects(renderer : SDL_Renderer, rects : iterable) -> None

   Fills multiple rectangles on the current rendering target with  the set
   drawing color.

   This wraps `SDL_RenderFillRects`.

.. function:: render_copy(renderer : SDL_Renderer, texture : SDL_Texture[, \
                          srcrect=None[, dstrect=None]]) -> None

   Copy a portion of the passed *texture* to the current rendering target.
   If *srcrect* is ``None``, the entire texture will be copied. If *dstrect*
   is ``None``, the entire rendering target will be used as area to copy
   the texture to.

   This wraps `SDL_RenderCopy`.

.. function:: render_read_pixels(renderer : SDL_Renderer, rect :SDL_Rect, \
                                 format_ : int, bufsize : int, pitch : int)

   TODO

   This wraps `SDL_RenderReadPixels`.

.. function:: render_present(renderer : SDL_Renderer) -> None

   TODO

   This wraps `SDL_RenderPresent`.

.. function:: destroy_texture(texture : SDL_Texture) -> None

   TODO

   This wraps `SDL_DestroyTexture`.

.. function:: destroy_renderer(renderer : SDL_Renderer) -> None

   TODO

   This wraps `SDL_DestroyRenderer`.
