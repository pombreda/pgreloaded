Pygame Reloaded Readme

Content:
--------
0. Description
1. Quick Installation
    1.1 Dependencies
    1.2 Notes on Mercurial usage
2. Getting started
3. License

0. Description
--------------
Pygame Reloaded is a cross-platform multimedia framework for the
excellent Python programming language. Its purpose is to make writing
multimedia applications, such as games, with Python as easy as possible,
while providing the developer a reliable and extensible programming
interface.

1. Quick Installation
---------------------
You can either use the python way of installing the package or the make
command using the Makefile.

Simply type

    python setup.py install 

for the traditional python way or

    make install

for using the Makefile. This will try to perform a default installation with
as many features as possible.
    
1.1 Dependencies
----------------
Pygame Reloaded is designed to run in as many environments as
possible. As such, the only absolutely necessary dependency is a working
Python installation. Additionally other libraries are needed, if you
want to enable certain features of Pygame Reloaded.

* Python 2.7, 3.1, 3.2 supported    (http://www.python.org)
* PyPy 1.8.0+ supported             (http://www.pypy.org)

Please note, that some parts of PyPy's ctypes implementation currently
do not support everything, Python's ctypes implementation
supports. There are some regressions, which are described in the
TODOS.txt file.

Optional dependencies:

* SDL >= 2.0.0                      (http://www.libsdl.org)
* SDL_image >= 1.2.13               (http://www.libsdl.org/projects/SDL_image/)
* SDL_ttf >= 2.0.12                 (http://www.libsdl.org/projects/SDL_ttf/)
* OpenAL >= 1.1                     (http://www.openal.org
                                     http://kcat.strangesoft.net/openal.html)

1.2 Notes on Mercurial usage
----------------------------
The Mercurial version of Pygame Reloaded is not intended to be used in a
production environment. Interfaces may change from one checkin to
another, methods, classes or modules can be broken and so on. If you
want more reliable code, please refer to the official releases.

2. Getting started
------------------
To gain ground quickly, you can find the reference and tutorials within
the doc/ directory. A lot of examples demonstrating the abilities of
Pygame Reloaded are available in the examples/ directory.

3. License
----------
This library is distributed under the Public Domain. Parts of the library
might use a different license. In that case, the specific files contain the
license information. If there is no license information in the file, it is
distributed under the Public Domain.

This basically means you can use Pygame Reloaded in any project and in
any way you want. In cases where specific laws do not recognize the
Public Domain, this library uses the zlib license. Please see the
COPYING.txt file for further information.
