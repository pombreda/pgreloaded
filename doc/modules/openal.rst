.. module:: pygame2.openal
   :synopsis: OpenAL sound wrapper

:mod:`pygame2.openal` - OpenAL sound wrapper
============================================

The :mod:`pygame2.openal` module is a :mod:`ctypes`-based wrapper around
the OpenAL library. It wraps nearly all publicly accessible structures and
functions of the OpenAL library to be accessible from Python code.

A detailled documentation about the behaviour of the different functions
can found within the `OpenAL documentation <http://connect.creativelabs.com/openal/Documentation/Forms/AllItems.aspx>`_.
The API documentation of :mod:`pygame2.openal` will focus on a brief
description and outlines noteworthy specialities or - where necessary -
differences for Python.

Submodules
----------

.. toctree::
   :maxdepth: 1

   openalal.rst
   openalalc.rst

OpenAL API
----------

.. function:: get_dll_file() -> string

   Gets the file name of the loaded OpenAL library.
