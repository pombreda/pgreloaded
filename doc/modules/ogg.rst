.. module:: pygame2.ogg
   :synopsis: Ogg Vorbis library wrapper

:mod:`pygame2.ogg` - Ogg Vorbis library wrapper
===============================================

The :mod:`pygame2.ogg` module is a :mod:`ctypes`-based wrapper around
the Ogg Vorbis libraries. It wraps nearly all publicly accessible
structures and functions of the Ogg Virobis library sets to be accessible
from Python code.

A detailled documentation about the behaviour of the different functions
can found within the relvant Ogg Vorbis documentation. The API documentation
of :mod:`pygame2.ogg` will focus on a brief description and outlines
noteworthy specialities or - where necessary - differences for Python.


Submodules
----------

.. toctree::
   :maxdepth: 1

   oggvorbisfile.rst
   
Ogg API
-------

.. exception:: OggError(msg=None)

   An Ogg Vorbis specific exception class.
