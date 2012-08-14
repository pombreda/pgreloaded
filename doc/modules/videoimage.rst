.. module:: pygame2.video.image
   :synopsis: Image loaders
.. currentmodule:: pygame2.video

:mod:`pygame2.video.image` - Image loaders
==========================================

.. function:: get_image_formats() -> (str, str, ...)

   Gets the formats supported by pygame2 in the default installation.

.. function:: load_image(fname : str[, assurface=False[, enforce=None]]) \
   -> SDL_Surface or Sprite

   Creates a :class:`Sprite` from an image file.

   If *assurface* is ``True``, a
   :class:`pygame2.sdl.surface.SDL_Surface` will be returned instead of
   a :class:`Sprite` object.

   This function makes use of the `Python Imaging Library
   <http://www.pythonware.com/products/pil/>`_, if it is available on
   the target execution environment. The function will try to load the
   file via :mod:`pygame2.sdlimage` first. If the file could not be
   loaded, it will try to load it via PIL.

   You can force the function to use only one of them, by passing the
   *enforce* as either ``"PIL"`` or ``"SDL"``.

   .. note::

      This will call :func:`pygame2.sdlimage.init()` implicitly with the
      default arguments, if the module is available.
