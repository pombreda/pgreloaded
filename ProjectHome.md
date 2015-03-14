.<br />
.<br />
.<br />
**ATTENTION:** The project has been moved to https://bitbucket.org/marcusva/py-sdl2
.<br />
.<br />
.<br />

pgreloaded is a cross-platform multimedia framework for the excellent Python programming language. Its purpose is to make writing multimedia applications, such as games, with Python as easy as possible, while providing the developer a reliable and extensible programming interface.

## About ##

Pygame Reloaded (aka pygame2, pgreloaded) started as a rewrite of the Pygame multimedia and game framework. As of 2012, the development focuses on providing a ctypes-based wrapper around SDL 2.0, along with a rich feature set for creating multimedia applications, games and graphics-based application prototypes.

Pygame Reloaded can be installed side-by-side with Pygame as it uses a different package namespace and thus will not cause any conflicts with another Pygame installation.

_Pygame Reloaded is not backwards compatible with Pygame - and work on Pygame is still continuing._

## Documentation ##

You can find the documentation online at http://wiki.pgreloaded.googlecode.com/hg/documentation/index.html.


## Downloads ##

There are no downloadable packages (yet). The -alpha5 release available features the legacy code base for SDL 1.2 (see below).

## Legacy Code for SDL 1.2 ##

As the original purpose was to rewrite everything based on SDL 1.2, you can find tons of legacy code in the sdl12 repository at http://code.google.com/p/pgreloaded/source/checkout?repo=sdl12.

The key differences between Pygame and and this code can be found in the module layout and integration purpose. Where Pygame is a fully integrated package with nearly anything ready to use after doing a simple import and init, the legacy code uses a more modular approach, where each module needs a seperate import and a few more lines of code to get anything ready to use.

Especially the SDL-related modules try to wrap all portions of the original C API in a 1:1 manner, using Python's full power.