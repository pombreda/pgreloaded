Installing Pygame2
==================
This section provides an overview and guidance for installing Pygame2 on various
target platforms.

Prerequisites
-------------
Pygame2 relies on some 3rd party packages to be fully usable and to provide you
full access to all of its features.

You must have at least one of the following Python versions installed:

* Python 2.7, 3.1, 3.2 (http://www.python.org)

Other Python versions might work, but are (currently) not officially tested or
supported by the Pygame2 distribution.

Additionally, you will need the following packages and libraries to be
installed:

======= ======== ================== =====================
Package Version  Required for       Package URL
======= ======== ================== =====================
SDL     >= 2.0.0 :mod:`pygame2.sdl` http://www.libsdl.org
======= ======== ================== =====================

.. note::
    The Pygame2 distribution ships with a set of pre-built DLLs for Microsoft
    Windows. The DLLs can be found in the lib\\dll\\ folder and will be installed
    under :mod:`pygame2.dll` by default. If you do not want the shipped DLLs to
    be used, you can replace them with your own DLLs.
    
    The shipped DLLs are 64-bit builds, thus your Python installation needs to
    be a 64-bit build, too, if you want to use them. If you want or need a
    32-bit Python installation, you have to exchange the DLLs with matching
    32-bit versions.

Installation
------------
You can either use the python way of installing the package or the make
command using the Makefile on *nix platforms, such as Linux or BSD, or the
make.bat batch file on Windows platforms.

Simply type ::

  python setup.py install
  
for the traditional python way or ::

  make install
  
for using the Makefile or make.bat. Both will try to perform a default
installation with as many features as possible.
