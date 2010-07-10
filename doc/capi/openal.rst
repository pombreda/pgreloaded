==============
pygame2.openal
==============
The :mod:`pygame2.openal` C API contains various objects and functions for
math and vector operations.

Import
------
Include headers::

  pygame2/pgopenal.h

.. cfunction:: int import_pygame2_openal (void)

  Imports the :mod:`pygame2.openal` module. This returns 0 on success and
  -1 on failure.

Macros
------

.. cmacro:: CONTEXT_IS_CURRENT (ctxt)

  Gets, whether the passed context is the current one. This returns 0,
  if the context is not the current one

.. cmacro:: ASSERT_CONTEXT_IS_CURRENT (ctxt, ret)

  Checks, whether the passed context is the current one. If not, this
  will set a :exc:`PyExc_PyGameError` and return *retval*.

PyDevice
--------
.. ctype:: PyDevice
.. ctype:: PyDevice_Type

The PyDevice object is an OpenAL device implementation, which
interoperates with the underlying audio hardware or software driver and
is used for audio playback.

Members
^^^^^^^
.. cmember:: ALCdevice* PyDevice.device

  Pointer to the underlying OpenAL device.

Functions
^^^^^^^^^
.. cfunction:: int PyDevice_Check (PyObject *obj)

  Returns true, if the argument is a :ctype:`PyDevice` or a subclass of
  :ctype:`PyDevice`.

.. cfunction:: ALCdevice* PyDevice_AsDevice (PyObject *obj)

  Macro for accessing the *device* member of the :ctype:`PyDevice`. This
  does not perform any type or argument checks.

.. cfunction:: PyObject* PyDevice_New (const char *name)

  Creates a new :ctype:`PyDevice` object for the passed OpenAL device
  identifier. *name* can bu NULL to use the default device. On failure,
  this returns NULL.

PyCaptureDevice
---------------
.. ctype:: PyCaptureDevice
.. ctype:: PyCaptureDevice_Type

The PyCaptureDevice object is an OpenAL device implementation, which
interoperates with the underlying audio hardware or software driver and
is used for audio recording.

Members
^^^^^^^
.. cmember:: PyDevice PyCaptureDevice.device

  The parent :ctype:`PyDevice` class the PyCaptureDevice inherits from.

.. cmember:: ALCsizei PyCaptureDevice.size

  The default buffer size to use for capturing sound.

.. cmember:: ALCenum PyCaptureDevice.format

  The format of the sound to capture.

.. cmember:: ALCuint PyCaptureDevice.frequency

  The frequency in Hz of the sound to capture.

Functions
^^^^^^^^^
.. cfunction:: int PyCaptureDevice_Check (PyObject *obj)

  Returns true, if the argument is a :ctype:`PyCaptureDevice` or a
  subclass of :ctype:`PyCaptureDevice`.

.. cfunction:: ALCdevice* PyCaptureDevice_AsDevice (PyObject *obj)

  Macro for accessing the (inherited) *device* member of the
  :ctype:`PyCaptureDevice`. This does not perform any type or argument
  checks.

.. cfunction:: PyObject* PyCaptureDevice_New (const char *name, ALCuint frequency, ALCenum format, ALCsizei size)

  Creates a new :ctype:`PyCaptureDevice` object for the passed OpenAL
  device identifier. *name* can bu NULL to use the default capture
  device. On failure, this returns NULL.

PyContext
---------
.. ctype:: PyContext
.. ctype:: PyContext_Type

  PyContext objects represent logical state groups, where sources and a
  listener are managed and audio data is correctly streamed to the
  underlying output device.

Members
^^^^^^^
.. cmember:: ALCcontext* context

  Pointer to the underlying OpenAL context.

.. cmember:: PyObject* device

  The :ctype:`PyDevice` bound to the context.

.. cmember:: PyObject* listener

  The :ctype:`PyListener` bound to the context. This will be NULL until
  the first call to the :attr:`pygame2.openal.Context.listener`
  property.

Functions
^^^^^^^^^
.. cfunction:: int PyContext_Check (PyObject *obj)

  Returns true, if the argument is a :ctype:`PyContext` or a subclass of
  :ctype:`PyContext`.

.. cfunction:: ALCcontext* PyContext_AsContext (PyObject *obj)

  Macro for accessing the *context* member of the :ctype:`PyContext`. This
  does not perform any type or argument checks.

PyBuffers
---------
.. ctype:: PyBuffers
.. ctype:: PyBuffers_Type

  PyBuffer objects are used by OpenAL to buffer and provide PCM data for
  playback, recording and manipulation.

Members
^^^^^^^
.. cmember:: PyObject* context

  The :ctype:`PyContext` the PyBuffers was created from.

.. cmember:: ALCsizei count

  The amount of buffers reserved.

.. cmember:: ALuint* buffers

  OpenAL identifiers for the single buffers.

Functions
^^^^^^^^^
.. cfunction:: int PyBuffers_Check (PyObject *obj)

  Returns true, if the argument is a :ctype:`PyBuffers` or a subclass of
  :ctype:`PyBuffers`.

.. cfunction:: ALuint* PyBuffers_AsBuffers (PyObject *obj)

  Macro for accessing the *buffers* member of the :ctype:`PyBuffers`. This
  does not perform any type or argument checks.

PySources
---------
.. ctype:: PySources
.. ctype:: PySources_Type

   Sources store locations, directions, and other attributes of an
   object in 3D space and have a buffer associated with them for
   playback. When the program wants to play a sound, it controls
   execution through a source object. Sources are processed
   independently from each other.

Members
^^^^^^^
.. cmember:: PyObject* context

  The :ctype:`PyContext` the PySources was created from.

.. cmember:: ALCsizei count

  The amount of sources reserved.

.. cmember:: ALuint* sources

  OpenAL identifiers for the single sources.

Functions
^^^^^^^^^
.. cfunction:: int PySources_Check (PyObject *obj)

  Returns true, if the argument is a :ctype:`PySources` or a subclass of
  :ctype:`PySources`.

.. cfunction:: ALuint* PySources_AsSources (PyObject *obj)

  Macro for accessing the *sources* member of the :ctype:`PySources`. This
  does not perform any type or argument checks.

PyListner
---------
.. ctype:: PyListener
.. ctype:: PyListener_Type

  The PyListener represents the user hearing the sounds played by OpenAL
  in a specific :ctype:`PyContext`. Source playback is done relative to
  the position of the PyListener in the 3D space.

Members
^^^^^^^
.. cmember:: PyObject* context

  The :ctype:`PyContext` the PyListener belongs to.

Functions
^^^^^^^^^
.. cfunction:: int PyListener_Check (PyObject *obj)

  Returns true, if the argument is a :ctype:`PyListener` or a subclass of
  :ctype:`PyListener`.
