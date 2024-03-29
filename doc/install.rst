Installing Pygame2
==================
This section provides an overview and guidance for installing Pygame2 on
various target platforms.

Prerequisites
-------------
Pygame2 relies on some 3rd party packages to be fully usable and to
provide you full access to all of its features.

You must have at least one of the following Python versions installed:

* Python 2.7, 3.1+     (http://www.python.org)
* PyPy 1.8.0+          (http://www.pypy.org)

Other Python versions or Python implementations might work, but are
(currently) not officially tested or supported by the Pygame2
distribution.

.. note::
   PyPy's :mod:`ctypes` implementation does not support everything
   supported by Python's :mod:`ctypes` implementation. For PyPy there
   are some known regressions as listed in the :doc:`todos`.

Additionally, you will need the following packages and libraries to be
installed to use *all* features of Pygame2:

========= ========= ======================= =========================================
Package   Version   Required for            Package URL
========= ========= ======================= =========================================
SDL       >= 2.0.0  :mod:`pygame2.sdl`      http://www.libsdl.org
SDL_image >= 1.2.13 :mod:`pygame2.sdlimage` http://www.libsdl.org/projects/SDL_image/
SDL_ttf   >= 2.0.12 :mod:`pygame2.sdlttf`   http://www.libsdl.org/projects/SDL_ttf/
OpenAL    >= 1.1    :mod:`pygame2.openal`   http://www.openal.org
                                            http://kcat.strangesoft.net/openal.html
libvorbis >= 1.3.3  :mod:`pygame2.ogg`      http://www.xiph.org
========= ========= ======================= =========================================

.. note::
   The Pygame2 distribution ships with a set of pre-built DLLs for
   Microsoft Windows. The DLLs can be found in the lib\\dll\\ folder
   and will be installed under :mod:`pygame2.dll` by default. If you do
   not want the shipped DLLs to be used, you can replace them with your
   own DLLs.

   The shipped DLLs come as 64-bit and 32-bit builds and Pygame2 tries to
   auto-detect, which of those should be used.

Installation
------------
You can either use the python way of installing the package or the make
command using the Makefile on POSIX-compatible platforms, such as Linux
or BSD, or the make.bat batch file on Windows platforms.

Simply type ::

  python setup.py install

for the traditional python way or ::

  make install

for using the Makefile or make.bat. Both will try to perform a default
installation with as many features as possible.

Trying out
^^^^^^^^^^
You also can test out Pygame2 without actually installing it. You just need
to set up your ``PYTHONPATH`` to point to the location of the source
distribution package. On Windows-based platforms, you might use something
like ::

   set PYTHONPATH=C:\path\to\pgreloaded\:$PYTHONPATH

to define the ``PYTHONPATH`` on a command shell. On Linux/Unix, use ::

   export PYTHONPATH=/path/to/pgreloaded:$PYTHONPATH

For bourne shell compatibles or ::

   setenv PYTHONPATH /path/to/pgreloaded:$PYTHONPATH

for C shell compatibles. You can omit the `:$PYTHONPATH``, if you did not use
it so far and if your environment settings do not define it.

.. note::

   If you are using IronPython, use ``IRONPYTHONPATH`` instead of
   ``PYTHONPATH``.

Notes on Mercurial usage
^^^^^^^^^^^^^^^^^^^^^^^^
The Mercurial version of Pygame Reloaded is not intended to be used in a
production environment. Interfaces may change from one checkin to
another, methods, classes or modules can be broken and so on. If you
want more reliable code, please refer to the official releases.
