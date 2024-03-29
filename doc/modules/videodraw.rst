.. module:: pygame2.video.draw
   :synopsis: 2D drawing routines for software surfaces

:mod:`pygame2.video.draw` - 2D drawing routines for software surfaces
=====================================================================

.. function:: prepare_color(color : object, target : object) -> int

   Prepares the passed *color* for a specific *target*. *color* can be any
   object type that can be processed by
   :func:`pygame2.color.convert_to_color()`. *target* can be any
   :class:`pygame2.sdl.pixels.SDL_PixelFormat`,
   :class:`pygame2.sdl.surface.SDL_Surface` or
   :class:`pygame2.video.sprite.SoftwareSprite` instance.

   The returned integer will be a color value matching the target's pixel
   format.

.. function:: fill(target : object, color : object[, area=None]) -> None

   Fills a certain area on the passed *target* with a *color*. If no *area* is
   provided, the entire target will be filled with  the passed color. If an
   iterable item is provided as *area* (such as a list or tuple), it will be
   first checked, if the item denotes a single rectangular area
   (4 integer values) before assuming it to be a sequence of rectangular areas
   to fill with the color.

   *target* can be any :class:`pygame2.sdl.surface.SDL_Surface` or
   :class:`pygame2.video.sprite.SoftwareSprite` instance.

.. function:: line(target : object, color : object[, width=1]) -> None

   Draws one or multiple lines on the passed *target*. *line* can be a
   sequence of four integers for a single line in the form ``(x1, y1,
   x2, y2)`` or a sequence of a multiple of 4 for drawing multiple lines
   at once, e.g. ``(x1, y1, x2, y2, x3, y3, x4, y4, ...)``.

   *target* can be any :class:`pygame2.sdl.surface.SDL_Surface` or
   :class:`pygame2.video.sprite.SoftwareSprite` instance.
