.. module:: pygame2.video
   :synopsis: Video and graphics routines

:mod:`pygame2.video` - Video and graphics routines
==================================================

The :mod:`pygame2.video` module contains various classes and methods
for creating, processing and manipulating on-screen graphics.


Submodules
----------

All classes and methods of the modules below are directly included in
the :mod:`pygame2.video` module.

.. toctree::
   :maxdepth: 1

   videodraw.rst
   videofont.rst
   videogui.rst
   videoimage.rst
   videopixelaccess.rst
   videosprite.rst
   videowindow.rst

Video API
---------

.. function:: init() -> None

   Initializes the underlying SDL2 video subsystem. Raises a
   :exc:`pygame2.sdl.SDLError`, if the SDL2 video subsystem could not be
   initialised.

.. function:: quit() -> None

   Quits the underlying SDL2 video subysystem. If no other SDL2 subsystems are
   active, this will also call :func:`pygame2.sdl.quit()`.

.. class:: TestEventProcessor()

   A simple event processor for testing purposes.

   .. method:: run(window : Window) -> None

      Starts an event loop without actually processing any event. The method
      will run endlessly until a ``SDL_QUIT`` event occurs.
