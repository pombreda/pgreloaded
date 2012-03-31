Pygame2 Readme

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
Pygame2 is a cross-platform multimedia framework for the excellent Python
programming language. Its purpose is to make writing multimedia applications,
such as games, with Python as easy as possible, while providing the developer a
reliable and extensible programming interface.

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
Pygame2 is designed to run in as many environments as possible. As such,
the only absolutely necessary dependency is a working Python
installation. Additionally other libraries are needed, if you want to
enable certain features of Pygame2.

* Python 2.7, 3.1, 3.2 supported    (http://www.python.org)

[Optional dependencies]
* SDL >= 2.0.0                      (http://www.libsdl.org)

1.2 Notes on Mercurial usage
----------------------------
The Mercurial version of Pygame2 is not intended to be used in a production
environment. Interfaces may change from one checkin to another, methods,
classes or modules can be broken and so on. If you want more reliable
code, please refer to the official releases.

2. Getting started
------------------
To gain ground quickly, you can find the reference and tutorials within
the doc/ directory. A lot of examples demonstrating the abilities of
Pygame2 are available in the examples/ directory.

3. License
----------
This library is distributed under the Public Domain, except for the code
below sdl/ (package pygame2.sdl), which is licensed under the zlib
license stated in the COPYING file.

This basically means you can use Pygame2 in any project and in any way
you want.  In cases, where specific laws do not recognize the Public
Domain, this library uses the zlib license. Please see the COPYING.txt
file for further information.
