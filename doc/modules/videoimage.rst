.. module:: pygame2.video.image
   :synopsis: Image loaders

:mod:`pygame2.video.image` - Image loaders
==========================================

.. function:: get_image_formats() -> (str, str, ...)

   Gets the formats supported by pygame2 in the default installation.

.. function:: load_image(fname : str[, renderer=None[,assurface=False[, \
   enforce=None]]]) -> SDL_Surface, Sprite or SoftSprite

   Creates a :class:`Sprite` from an image file.

   If *assurface* is ``True``, a
   :class:`pygame2.sdl.surface.SDL_Surface` will be returned instead of
   a :class:`pygame2.video.sprite.Sprite` or
   :class:`pygame2.video.sprite.SoftSprite` object. If *renderer* is set
   to a SDL_Renderer, a :class:`pygame2.video.sprite.Sprite` will be
   returned.

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
