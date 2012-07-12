.. module:: pygame2.openal.alc
   :synopsis: SDL2 OpenAL ALC wrapper

:mod:`pygame2.openal.alc` - OpenAL ALC wrapper
==============================================

OpenAL ALC API
--------------

.. class:: ALCdevice

   TODO
   
.. class:: ALCcontext

   TODO

.. function:: get_error(device : ALCdevice) -> int

   Gets the most recent error generated within the AL system for the specific
   *device*.

   This wraps :c:func:`alcGetError`.

.. function:: create_context(device : ALCdevice[, attrs=None]) -> ALCcontext

   Creates a context from the specified device.

   This wraps :c:func:`alcCreateContext`.

.. function:: make_context_current(context : ALCcontext) -> bool

   Makes the specified context the current context.

   This wraps :c:func:`alcMakeContextCurrent`.

.. function:: process_context(context : ALCcontext) -> None

   Tells the passed *context* to begin processing.

   This wraps :c:func:`alcProcessContext`.

.. function:: suspend_context(context : ALCcontext) -> None

   Tells the passed *context* to suspend processing.

   This wraps :c:func:`alcSuspendContext`.

.. function:: destroy_context(context : ALCcontext) -> None

   Destroys the passed context.

   This wraps :c:func:`alcDestroyContext`.

.. function:: get_current_context() -> ALCcontext

   Retrieves the current context.

   This wraps :c:func:`ALCcontext`.

.. function:: get_context_device(context : ALCcontext) -> ALCdevice

   Retrieves the device used by the context.

   This wraps :c:func:`ALCdevice`.

.. function:: open_device(devicename=None) -> ALCdevice

   Opens an OpenAL device with the specified name. If no *devicename* is
   passed, the default output device is opened.

   This wraps :c:func:`alcOpenDevice`.

.. function:: close_device(device : ALCdevice) -> bool

   Closes the passed OpenAL device.

   This wraps :c:func:`alcCloseDevice`.

.. function:: is_extension_present(device : ALCdevice, extname : string) -> bool

   Checks, if a certain extension is available for the passed *device*.

   This wraps :c:func:`alcIsExtensionPresent`.

.. function:: get_proc_address(device : ALCdevice, funcname : string) -> c_void_p

   Retrieves the address of the specified device extension function.

   This wraps :c:func:`alcGetProcAddress`.

.. function:: get_enum_value(device : ALCdevice, enumname : string) -> int

   Retrieves the value for the specified enumeration name on the device.

   This wraps :c:func:`alcGetEnumValue`.

.. function:: get_string(device : ALCdevice, param : int) -> string

   Returns a set of strings related to the context device.

   This wraps :c:func:`alcGetString`.

.. function:: get_integer_v(device : ALCdevice, param : int, size : int) \
              -> (int, int, ...)

   Returns a set of integers related to the context device.

   This wraps :c:func:`alcGetIntegerv`.

.. function:: capture_open_device(devicename : string, \
                                  frequency : int, dformat : int, \
                                  buffersize : int) -> ALCdevice

   Opens an OpenAL capture device with the specified name.

   This wraps :c:func:`ALCdevice`.

.. function:: capture_close_device(device : ALCdevice)

   Closes the passed capture device.

   This wraps :c:func:`alcCaptureCloseDevice`.

.. function:: capture_start(device : ALCdevice) -> None

   Start a capturing operation.

   This wraps :c:func:`alcCaptureStart`.

.. function:: capture_stop(device : ALCdevice) -> None

   Stops a capturing operation.

   This wraps :c:func:`alcCaptureStop`.

.. function:: capture_samples(device : ALCdevice, amount : int, \
                              itemsize : int) -> bytes

   Retrieves the audio data samples of a capture device.

   This wraps :c:func:`alcCaptureSamples`.
