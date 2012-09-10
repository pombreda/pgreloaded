.. module:: pygame2.video.pixelaccess
   :synopsis: 2D and 3D direct pixel access

:mod:`pygame2.video.pixelaccess` - 2D and 3D direct pixel access
================================================================

.. class:: PixelView(source : object)

   2D :class:`pygame2.array.MemoryView` for :class:`Sprite` and surface
   pixel access.

   .. note::

      If necessary, the *source* surface will be locked for accessing its
      pixel data. The lock will be removed once the :class:`PixelView` is
      garbage-collected or deleted.


.. function:: pixels2d(source : object)

   Creates a 2D pixel array, based on ``numpy.ndarray``, from the passed
   *source*. *source* can be a :class:`pygame2.video.sprite.Sprite` or
   :class:`pygame2.sdl.surface.SDL_Surface`. The *source*'s
   ``SDL_Surface`` will be locked and unlocked automatically.

   The *source* pixels will be accessed and manipulated directly.

   .. note::

      :func:`pixels2d` is only usable, if the numpy package is available
      within the target environment. If numpy could not be imported, a
      :exc:`pygame2.compat.UnsupportedError` will be raised.

.. function:: pixels3d(source : object)

   Creates a 3D pixel array, based on ``numpy.ndarray``, from the passed
   *source*. *source* can be a :class:`pygame2.video.sprite.Sprite` or
   :class:`pygame2.sdl.surface.SDL_Surface`. The *source*'s
   ``SDL_Surface`` will be locked and unlocked automatically.

   The *source* pixels will be accessed and manipulated directly.

   .. note::

      :func:`pixels3d` is only usable, if the numpy package is available
      within the target environment. If numpy could not be imported, a
      :exc:`pygame2.compat.UnsupportedError` will be raised.
