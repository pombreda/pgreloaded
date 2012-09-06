TODOs
=====

General
-------
* There seem to be random dead locks with X11/GL related unit tests on
  Linux running in a VM - might be related to the heavy X11 context
  switches within the setUp() and tearDown() calls. The dead locks are
  caused by a futex(... FUTEX_WAIT_PRIVATE ...) call never returning...

SDL2
----
* SDL_assert.h API - we do not really need that one
* SDL_mutex.h API - better be handled by multiprocessing and friends
* SDL_thread.h API - better be handled by multiprocessing and friends

* :func:`pygame2.sdl.rwops.rw_from_object()` seems to run into threading
  issues with 3rd party libraries that are loaded via SDL2
  (esp. SDL2_image) on 64-bit platforms. This might have to be reworked
  to make it thread-safe for ctypes OR the 3rd party libraries are
  somehow broken for such a usage.

PyPy
----
* PyPy 1.8+ can't encapsule str in py_object() pointers, which breaks
  a lot of unit tests (https://bugs.pypy.org/issue1233)

IronPython
----------
* does not handle function pointers correctly
* can not deal with nested union assignments correctly (e.g.
  pygame2.sdl.events)
* does not handle long/longlong conversions and ranges correctly
  (pygame2.video.pixelaccess and other pixel access routines)

Jython
------
* does not feature a solid (C)Python 2.7 compatibility at the moment
