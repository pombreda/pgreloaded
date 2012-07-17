.. module:: pygame2.video.draw
   :synopsis: 2D drawing routines
.. currentmodule:: pygame2.video

:mod:`pygame2.video.draw` - 2D drawing routines
===============================================

.. function:: prepare_color(color : object, target : object) -> int

   Prepares the passed *color* for a specific *target*. *color* can be any
   object type that can be processed by
   :func:`pygame2.color.convert_to_color()`. *target* can be any
   :class:`pygame2.sdl.pixels.SDL_PixelFormat`,
   :class:`pygame2.sdl.surface.SDL_Surface` or
   :class:`Sprite` instance.

   The returned integer will be a color value matching the target's pixel
   format.

.. function:: fill(target : object, color : object[, area=None]) -> None

   Fills a certain area on the passed *target* with a *color*. If no *area* is
   provided, the entire target will be filled with  the passed color. If an
   iterable item is provided as *area* (such as a list or tuple), it will be
   first checked, if the item denotes a single rectangular area
   (4 integer values) before assuming it to be a sequence of rectangular areas
   to fill with the color.

.. class:: PixelView(source : object)

   2D :class:`pygame2.array.MemoryView` for
   :class:`Sprite` and surface pixel access.

   .. note::

      If necessary, the *source* surrface will be locked for accessing its
      pixel data. The lock will be removed once the :class:`PixelView` is
      garbage-collected or deleted.
