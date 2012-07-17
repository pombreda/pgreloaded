.. module:: pygame2.video.sprite
   :synopsis: Sprite, texture and pixel surface routines
.. currentmodule:: pygame2.video

:mod:`pygame2.video.sprite` - Sprite, texture and pixel surface routines
========================================================================

.. class:: Sprite(source=None, size=(0, 0), bpp=32, freesf=False)

   A simple, visible, pixel-based 2D object.

   If a *source* is provided, the constructor assumes it to be a
   readable buffer object or file path to load the pixel data from.
   The *size* and *bpp* will be ignored in those cases.

   If no *source* is provided, a *size* tuple containing the width and
   height of the sprite and a *bpp* value, indicating the bits per
   pixel to be used, need to be provided.

   *freesf* denotes, if the passed *source* shall be freed automatically on
   garbage-collecting the :class:`Sprite`.

   .. attribute:: surface

      The :class:`pygame2.sdl.surface.SDL_Surface` containing the pixel data.

   .. attribute:: depth

      The layer depth on which to draw the :class:`Sprite`. :class:`Sprite`
      objects with higher :attr:`depth` values will be drawn on top of other
      :class:`Sprite` values by the :class:`SpriteRenderer`.

   .. attribute:: x

      The top-left horizontal offset at which the :class:`Sprite` resides.

   .. attribute:: y

      The top-left vertical offset at which the :class:`Sprite` resides.

   .. attribute:: position

      The top-left position (:attr:`x` and :attr:`y` as tuple.

   .. attribute:: size

      The size of the :class:`Sprite` as tuple.

   .. attribute:: area

      The rectangular area occupied by the :class:`Sprite`.

.. class:: SpriteRenderer(window : Window)

   A rendering system for :class:`Sprite` components. The
   :class:`SpriteRenderer` class uses a :class:`Window` as drawing
   device to display :class:`Sprite` surfaces. It uses the internal SDL
   surface of the *window* as drawing context, so that GL operations,
   such as texture handling or the usage of SDL renderers is not
   possible.

   .. attribute:: window

      The :class:`Window` that is used as drawing device.

   .. attribute:: surface

      The :class:`pygame2.sdl.surface.SDL_Surface` that acts as drawing context
      for the :class:`Window`.

   .. attribute:: sortfunc

      Sort function for the component processing order. The default sort order
      is based on the depth attribute of every sprite. Lower depth values will
      cause sprites to be drawn below sprites with higher depth values.
      if :attr:`sortfunc` shall be overriden, it must match thre callback
      requirements for :func:`sorted()`.

   .. method:: render(sprite : Sprite[, x=None[, y=None]]) -> None

      Draws the passed *sprite* on the :class:`pygame2.video.Window`
      surface. *x* and *y* are optional arguments that can be used as drawing
      location for *sprite*. If set to ``None``, the location information
      of the *sprite* are used.

   .. method:: process(world : World, components : iterable) -> None

      Draws the passed :class:`Sprite` objects on the
      :class:`pygame2.video.Window` surface.
