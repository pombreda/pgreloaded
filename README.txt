Pygame2 Readme

Content:
--------
0. Description
1. Quick Installation
    1.1 Dependencies
    1.2 Notes on SVN usage
    1.3 Notes for Windows users
    1.4 Notes for Mac OS users
    1.5 Notes for Unix users
2. Getting started
3. License

0. Description
--------------
Pygame2 is a cross-platform multimedia framework for the excellent Python
programming language. Its purpose is to make writing multimedia applications,
such as games, with Python as easy as possible, while providing the developer a
reliable and extensible programming interface.

Pygame2 can be configured in numerous ways to tweak it to the specific needs
of the target application and environment. It can make use of different
3rd party libraries, such as SDL, to provide enhanced functionality.

1. Quick Installation
---------------------
You can either use the python way of installing the package or the make
command using the Makefile.

Simply type

  python setup.py install 

for the traditional python way or

  make install

for using the Makefile. This will try to perform a default installation with
as many features as possible. If it does not suit your needs or you do not have
all the dependencies available (see the section 1.1), you can tweak the
features to build and install by making the necessary adjustments within the
"cfg.py" file. 

You also can use certain environment settings to influence the build
instead of touching the "cfg.py" file. Currently the following
environment variables are controlling, which components of pgreloaded
should be build:

WITH_SDL=[yes|no|1|True]            Example: make -DWITH_SDL=yes

    Build and install the pygame2.sdl module. This wraps the SDL library
    and is required for any other SDL related module in pgreloaded.

WITH_SDL_MIXER=[yes|no|1|True]      Example: make -DWITH_SDL_MIXER=no

    Build and install the pygame2.sdlmixer module. This wraps the
    SDL_mixer library. 

WITH_SDL_IMAGE=[yes|no|1|True]      Example: make -DWITH_SDL_IMAGE=True

    Build and install the pygame2.sdlimage module. This wraps the
    SDL_image library.

WITH_SDL_TTF=[yes|no|1|True]        Example: make -DWITH_SDL_TTF=True

    Build and install the pygame2.sdlttf module. This wraps the
    SDL_ttf library.

WITH_SDL_GFX=[yes|no|1|True]        Example: make -DWITH_SDL_GFX=1

    Build and install the pygame2.sdlgfx module. This wraps the
    SDL_gfx library.

WITH_PNG=[yes|no|1|True]            Example: make -DWITH_PNG=True

    Build with PNG format saving support for pygame2.sdl.

WITH_JPEG=[yes|no|1|True]           Example: make -DWITH_JPEG=False

    Build with JPEG format saving support for pygame2.sdl.

WITH_FREETYPE=[yes|no|1|True]       Example: make -DWITH_FREETYPE=False
    
    Build and install the pygame2.freetype module. This wraps the
    FreeType2 library.

WITH_PORTMIDI=[yes|no|1|True]       Example: make -DWITH_PORTMIDI=False
    
    Build and install the pygame2.midi module. This wraps the
    portmidi library and gives access to the pygame2.midi module.

WITH_OPENAL=[yes|no|1|True]         Example: make -DWITH_OPENAL=False
    
    Build and install the pygame2.openal module. This wraps the
    OpenAL library and gives access to the pygame2.openal module.

WITH_OPENMP=[yes|no|1|True]         Example: make -DWITH_OPENAL=1
    
    Add support for the Open Multi-Processing library. This will utilize
    the OpenMP API to speed up certain routines, such as e.g blit and
    fill operations. This option is only available for certain compilers
    and will be disabled by default.

WITH_EXPERIMENTAL=[yes|no|1|True]   Example: make -DWITH_EXPERIMENTAL=True

    Build pygame2 modules, which are marked as experimental. Note that those
    modules are likely to change a lot between updates, may cause instabilities
    and can contain lots of bugs.
    
1.1 Dependencies
----------------
Pygame2 is designed to run in as many environments as possible. As such,
the only absolutely necessary dependency is a working Python
installation. Additionally other libraries are needed, if you want to
enable certain features of Pygame2.

* Python 2.4, 2.5, 2.6, 3.1 supported   (http://www.python.org)

[Optional dependencies]
* SDL >= 1.2.10                 (http://www.libsdl.org)
* SDL_mixer >= 1.2.11           (http://www.libsdl.org/projects/SDL_mixer/)
* SDL_ttf >= 2.0.9              (http://www.libsdl.org/projects/SDL_ttf/)
* SDL_image >= 1.2.10           (http://www.libsdl.org/projects/SDL_image/)
* SDL_gfx >= 2.0.18             (http://www.ferzkopp.net/Software/SDL_gfx-2.0/)
* libpng >= 1.2.24              (http://www.libpng.org)
* libjpeg >= 6b                 (http://www.ijg.org/)
* freetype >= 2.3.5             (http://www.freetype.org)
* portmidi >= 199               (http://portmedia.sourceforge.net/)
* OpenAL                        use one of:
    
  * OpenAL11CoreSDK (Aug 2009) http://www.openal.org 
  * openal-soft >= 1.11.753    http://kcat.strangesoft.net/openal.html

1.2 Notes on SVN usage
----------------------
The SVN version of Pygame2 is not intended to be used in a production
environment. Interfaces may change from one checkin to another, methods,
classes or modules can be broken and so on. If you want more reliable
code, please refer to the official releases.

1.3 Notes for Windows users
---------------------------
Bulding Pygame2 from its source code is supported in combination with the
MinGW compiler suite or Microsoft Visual C++.

Please take a look at the doc/BuildMingGW.txt and doc/BuildVC.txt documents for
more details about how to configure and install Pygame2 on your Windows
platform.

1.4 Notes for Mac OS users
--------------------------
Mac OS X is considered an Unix system so building is pretty
straighforward, although some exceptions apply. Details can be found on
the doc/BuildDarwin.txt file.

1.5 Notes for Unix users
------------------------
Building Pygame2 from its source code usually happens as described above
in 'Quick Installation'. You might want to take a look at the
doc/BuildUnix.txt document for more details about it, though.

2. Getting started
------------------
To gain ground quickly, you can find the reference and tutorials within
the doc/ directory. A lot of examples demonstrating the abilities of
Pygame2 are available in the examples/

3. License
----------
This library is distributed under GNU LGPL version 2.1, which can be found in
the file "doc/LGPL". Parts might be licensed with less restrictions (e.g.
BSD-style license or Public Domain code).

This basically means you can use Pygame2 in any project you want, but if
you make any changes or additions to pygame itself, those must be
released with a compatible license (preferably submitted back to the
pygame project). Closed source and commercial games are fine.

The programs in the "doc/examples" subdirectory are in the public domain.
The documentation generators in the doc/ directory are in the public domain.
Parts of the test framework in the "test/util" subdirectory are in
the public domain.

