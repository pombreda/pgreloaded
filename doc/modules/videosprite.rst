.. module:: pygame2.video.sprite
   :synopsis: Sprite, texture and pixel surface routines

:mod:`pygame2.video.sprite` - Sprite, texture and pixel surface routines
========================================================================

.. inheritance-diagram:: pygame2.video.sprite
   :parts: 1


.. class:: SoftSprite(source=None, size=(0, 0), bpp=32, masks=None, \
   freesf=False)

   A simple, visible, pixel-based 2D object.

   If a *source* is provided, the constructor assumes it to be a
   readable buffer object or file path to load the pixel data from.
   The *size* and *bpp* will be ignored in those cases.

   If no *source* is provided, a *size* tuple containing the width and
   height of the sprite and a *bpp* value, indicating the bits per
   pixel to be used, need to be provided.

   *freesf* denotes, if the passed *source* shall be freed automatically on
   garbage-collecting the :class:`SoftSprite`.

   .. attribute:: surface

      The :class:`pygame2.sdl.surface.SDL_Surface` containing the pixel data.

   .. attribute:: depth

      The layer depth on which to draw the :class:`SoftSprite`.
      :class:`SoftSprite` objects with higher :attr:`depth` values will be
      drawn on top of other :class:`SoftSprite` values by the
      :class:`SoftSpriteRenderer`.

   .. attribute:: x

      The top-left horizontal offset at which the :class:`SoftSprite` resides.

   .. attribute:: y

      The top-left vertical offset at which the :class:`SoftSprite` resides.

   .. attribute:: position

      The top-left position (:attr:`x` and :attr:`y`) as tuple.

   .. attribute:: size

      The size of the :class:`SoftSprite` as tuple.

   .. attribute:: area

      The rectangular area occupied by the :class:`SoftSprite`.

.. class:: SoftSpriteRenderer(window : object)

   A rendering system for :class:`SoftSprite` components. The
   :class:`SoftSpriteRenderer` class uses a
   :class:`pygame2.sdl.video.SDL_Window` as drawing device to display
   :class:`SoftSprite` surfaces. It uses the internal SDL surface of the
   *window* as drawing context, so that GL operations, such as texture handling
   or the usage of SDL renderers is not possible.

   *window* can be either a :class:`pygame2.video.window.Window` or
   :class:`pygame2.sdl.video.SDL_Window` instance.

   .. attribute:: window

      The :class:`pygame2.sdl.video.SDL_Window` that is used as drawing device.

   .. attribute:: surface

      The :class:`pygame2.sdl.surface.SDL_Surface` that acts as drawing context
      for :attr:`window`.

   .. attribute:: sortfunc

      Sort function for the component processing order. The default sort order
      is based on the depth attribute of every sprite. Lower depth values will
      cause sprites to be drawn below sprites with higher depth values.
      if :attr:`sortfunc` shall be overriden, it must match thre callback
      requirements for :func:`sorted()`.

   .. method:: render(sprites : object[, x=None[, y=None]]) -> None

      Draws the passed *sprites* on the :class:`pygame2.video.window.Window`
      surface. *x* and *y* are optional arguments that can be used as relative
      drawing location for *sprites*. If set to ``None``, the location
      information of the *sprites* are used. If set and *sprites* is an
      iterable, such as a list of :class:`SoftSprite` objects, *x* and *y* are
      relative location values that will be added to each individual sprite's
      position. If *sprites* is a single :class:`SoftSprite`, *x* and *y* denote
      the absolute position of the :class:`SoftSprite`, if set.

   .. method:: process(world : World, components : iterable) -> None

      Draws the passed :class:`Sprite` objects on the
      :class:`pygame2.video.window.Window` surface.

.. class:: Sprite(renderer, source=None, size=(0, 0), \
                  format=SDL_PIXELFORMAT_RGBA8888, static=True)

   A simple, visible, pixel-based 2D object.

   If a source is provided, the constructor assumes it to be a
   readable buffer object or file path to load the pixel data from.
   The size will be ignored in those cases.

   If no source is provided, a size tuple containing the width and
   height of the sprite needs to be provided.

   TSprite objects are assumed to be static by default, making it
   impossible to access their pixel buffer in favour for faster copy
   operations. If you need to update the pixel data frequently, static
   can be set to False to allow a streaming access on the underlying
   texture pixel buffer.

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

.. class:: SpriteRenderer(obj : object)

   A rendering system for :class:`Sprite` components. The
   :class:`SpriteRenderer` class uses a :class:`pygame2.sdl.render.SDL_Renderer`
   as drawing device to display :class:`Sprite` surfaces.

   *obj* can be a :class:`pygame2.video.window.Window`,
   :class:`pygame2.sdl.video.SDL_Window` or a
   :class:`pygame2.sdl.render.SDL_Renderer`. If it is a
   :class:`pygame2.video.window.Window` or
   :class:`pygame2.sdl.video.SDL_Window` instance, it will try to
   create a :class:`pygame2.sdl.render.SDL_Renderer` with hardeware
   acceleration for it.

   .. attribute:: renderer

      The :class:`pygame2.sdl.render.SDL_Renderer` that is used as drawing
      context.

   .. attribute:: sortfunc

      Sort function for the component processing order. The default sort order
      is based on the depth attribute of every sprite. Lower depth values will
      cause sprites to be drawn below sprites with higher depth values.
      if :attr:`sortfunc` shall be overriden, it must match thre callback
      requirements for :func:`sorted()`.

   .. method:: render(sprites : object[, x=None[, y=None]]) -> None

      Renders the passed *sprites* via the :attr:`renderer`.
      *x* and *y* are optional arguments that can be used as relative
      drawing location for *sprites*. If set to ``None``, the location
      information of the *sprites* are used. If set and *sprites* is an
      iterable, such as a list of :class:`Sprite` objects, *x* and *y* are
      relative location values that will be added to each individual sprite's
      position. If *sprites* is a single :class:`Sprite`, *x* and *y* denote
      the absolute position of the :class:`Sprite`, if set.

   .. method:: process(world : World, components : iterable) -> None

      Draws the passed :class:`Sprite` via the :attr:`renderer`.
