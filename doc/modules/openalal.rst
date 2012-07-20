.. module:: pygame2.openal.al
   :synopsis: SDL2 OpenAL AL wrapper

:mod:`pygame2.openal.al` - OpenAL AL wrapper
============================================

.. function:: get_error() -> int

   Gets the most recent error generated within the AL system.

   This wraps :c:func:`alGetError`.

.. exception:: OpenALError(msg=None)

   An OpenAL specific exception class. If no *msg* is provided, the message
   will be set a mapped value of :func:`get_error()`.

.. function:: enable(capability : int) -> None

   Enables a feature of the OpenAL driver.

   This wraps :c:func:`alEnable`.

.. function:: disable(capability : int) -> None

   Disables a feature of the OpenAL driver.

   This wraps :c:func:`alDisable`.

.. function:: is_enabled(capability : int) -> bool

   Checks, if a feature of the OpenAL driver is currently enabled.

   This wraps :c:func:`alIsEnabled`.

.. function:: get_string(param : int) -> string

   Retrieves an OpenAL string property.

   This wraps :c:func:`alGetString`.

.. function:: get_boolean_v(param : int) -> (int, int, ...)

   Retrieves an OpenAL boolean state.

   This wraps :c:func:`alGetBooleanv`.

.. function:: get_integer_v(param : int) -> (int, int, ...)

   Retrieves an OpenAL integer state.

   This wraps :c:func:`alGetIntegerv`.

.. function:: get_float_v(param : int) -> (float, float, ...)

   Retrieves an OpenAL float state.

   This wraps :c:func:`alGetFloatv`.

.. function:: get_double_v(param : int) -> (float, float, ...)

   Retrieves an OpenAL double state.

   This wraps :c:func:`alGetDoublev`.

.. function:: get_boolean(param : int) -> bool

   Returns an OpenAL boolean state.

   This wraps :c:func:`alGetBoolean`.

.. function:: get_integer(param : int) -> int

   Returns an OpenAL integer state.

   This wraps :c:func:`alGetInteger`.

.. function:: get_float(param : int) -> float

   Returns an OpenAL float state.

   This wraps :c:func:`alGetFloat`.

.. function:: get_double(param : int) -> float

   Returns an OpenAL double state.

   This wraps :c:func:`alGetDouble`.

.. function:: is_extension_present(extname : string) -> bool

   Tests if the specified extension is available for the OpenAL driver.

   This wraps :c:func:`alIsExtensionPresent`.

.. function:: get_proc_address(fname : string) -> c_void_p

   Returns the address of an OpenAL extension function.

   This wraps :c:func:`alGetProcAddress`.

.. function:: get_enum_value(ename : string) -> int

   Returns the enumeration value of an OpenAL enum.

   This wraps :c:func:`alGetEnumValue`.

.. function:: listener_f(param : int, value : float) -> None

   Sets a floating point property for the listener.

   This wraps :c:func:`alListenerf`.

.. function:: listener_3f(param : int, value1 : float, value2 : float, \
                          value3 : float) -> None

   Sets a floating point property for the listener.

   This wraps :c:func:`alListener3f`.

.. function:: listener_fv(param : int, values : iterable) -> None

   Sets a floating point-vector property for the listener

   This wraps :c:func:`alListenerfv`.

.. function:: listener_i(param : int, value : int) -> None

   Sets an integer property for the listener.

   This wraps :c:func:`alListeneri`.

.. function:: listener_3i(param : int, value1 : int, value2 : int, \
                          value3 : int) -> None

   Sets an integer property for the listener.

   This wraps :c:func:`alListener3i`.

.. function:: listener_iv(param : int, values : iterable) -> None

   Sets an integer-vector property for the listener.

   This wraps :c:func:`alListenerfv`.

.. function:: get_listener_f(param : int) -> float

   Gets a floating point property for the listener.

   This wraps :c:func:`alGetListenerf`.

.. function:: get_listener_3f(param : int) -> (float, float, float)

   Gets a floating point property for the listener and returns it as tuple.

   This wraps :c:func:`alGetListener3f`.

.. function:: get_listener_fv(param : int, size : int) -> (float, float, ...)

   Gets a floating point-vector property for the listener and returns it
   as tuple.

   This wraps :c:func:`alGetListenerfv`.

.. function:: get_listener_i(param : int) -> int

   Gets an integer property for the listener.

   This wraps :c:func:`alGetListeneri`.

.. function:: get_listener_3i(param : int) -> (int, int, int)

   Gets an integer property for the listener and returns it as tuple.

   This wraps :c:func:``alGetListener3i``.

.. function:: get_listener_iv(param : int, size : int) -> (int, int, ...)

   Gets an integer-vector property for the listener and returns it
   as tuple.

   This wraps :c:func:`alGetListeneriv`.

.. function:: gen_sources(size : int) -> (int, int, ...)

   Generates one or more sources and returns their ids as tuple.

   This wraps :c:func:`alGenSources`.

.. function:: delete_sources(sources : iterable) -> None

   Deletes one or more sources.

   This wraps :c:func:`alDeleteSources`.

.. function:: is_source(sid : int) -> bool

   Tests if the passed *sid* is a valid source identifier.

   This wraps :c:func:`alIsSource`.

.. function:: source_f(sid : int, param : int, value : float) -> None

   Sets a floating point property of a source.

   This wraps :c:func:`alSourcef`.

.. function:: source_3f(sid : int, param : int, value1 : float, \
                        value2 : float, value3 : float) -> None

   Sets a floating point property of a source.

   This wraps :c:func:`alSource3f`.

.. function:: source_fv(sid : int, param : int, values : iterable) -> None

   Sets a floating point-vector property of a source.

   This wraps :c:func:`alSourcefv`.

.. function:: source_i(sid : int, param : int, value : int) -> None

   Sets an integer property of a source.

   This wraps :c:func:`alSourcei`.

.. function:: source_3i(sid : int, param : int, value1 : int, value2 : int, \
                        value3 : int) -> None

   Sets an integer property of a source.

   This wraps :c:func:`alSource3i`.

.. function:: source_iv(sid : int, param : int, values : iterable) -> None

   Sets an integer-vector property of a source.

   This wraps :c:func:`alSourceiv`.

.. function:: get_source_f(sid : int, param : int) -> float

   Gets a floating point property of a source.

   This wraps :c:func:`alGetSourcef`.

.. function:: get_source_3f(sid : int, param : int) -> (float, float, float)

   Gets a floating point property of a source and returns it as tuple.

   This wraps :c:func:`alGetSource3f`.

.. function:: get_source_fv(sid : int, param : int, size : int) -> (int, int, ...)

   Gets a floating point-vector property of a source.

   This wraps :c:func:`alGetSourcefv`.

.. function:: get_source_i(sid : int, param : int) -> int

   Gets an integer property of a source.

   This wraps :c:func:`alGetSourcei`.

.. function:: get_source_3i(sid : int, param : int) -> (int, int, int)

   Gets an integer property of a source.

   This wraps :c:func:`alGetSource3i`.

.. function:: get_source_iv(sid : int, param : int, size : int) -> (int, int, ...)

   Gets an integer-vector property of a source.

   This wraps :c:func:`alGetSourceiv`.

.. function:: source_play_v(sids : iterable) -> None

   Plays a set of sources.

   This wraps :c:func:`alSourcePlayv`.

.. function:: source_stop_v(sids : iterable) -> None

   Stops a set of sources.

   This wraps :c:func:`alSourceStopv`.

.. function:: source_rewind_v(sids : iterable) -> None

   Rewinds a set of sources.

   This wraps :c:func:`alSourceRewindv`.

.. function:: source_pause_v(sids : iterable) -> None

   Pauses a set of sources.

   This wraps :c:func:`alSourcePausev`.

.. function:: source_play(sid : int) -> None

   Plays a source.

   This wraps :c:func:`alSourcePlay`.

.. function:: source_stop(sid : int) -> None

   Stops a source.

   This wraps :c:func:`alSourceStop`.

.. function:: source_rewind(sid : int) -> None

   Rewinds a source.

   This wraps :c:func:`alSourceRewind`.

.. function:: source_pause(sid : int) -> None

   Pauses a source.

   This wraps :c:func:`alSourcePause`.

.. function:: source_queue_buffers(sid : int, bids : iterable) -> None

   Queues a set of buffers on a source. All buffers attached to a source will
   be played in sequence and the number of buffers played can be retrieved
   using a :func:`source_i()` call to retrieve ``AL_BUFFERS_PROCESSED``.

   This wraps :c:func:`alSourceQueueBuffers`.

.. function:: source_unqueue_buffers(sid : int, bids : iterable) -> None

   Unqueues a set of buffers attached to a source.

   This wraps :c:func:`alSourceUnqueueBuffers`.

.. function:: gen_buffers(count : int) -> (int, int, ...)

   Generates one or more buffers, which contain audio data.

   This wraps :c:func:`alGenBuffers`.

.. function:: delete_buffers(buffers : iterable) -> None

   Deletes one or more buffers, freeing the resources used by them.

   This wraps :c:func:`alDeleteBuffers`.

.. function:: is_buffer(bid : int) -> bool

   Tests if the passed bid is a valid buffer identifier.

   This wraps :c:func:`alIsBuffer`.

.. function:: buffer_data(bid : int, bformat : int, data : bytes, \
                          freq : int) -> None

   Fill a buffer with audio data. The predefined formats expect the data
   to be valid PCM data, extension functions might load other data types
   as well."""

   This wraps :c:func:`alBufferData`.

.. function:: buffer_f(bid : int, param : int, value : float) -> None

   Sets a floating point property of the buffer.

   This wraps :c:func:`alBufferf`.

.. function:: buffer_3f(bid : int, param : int, value1 : float, \
                        value2 : float, value3 : float) -> None

   Sets a floating point property of the buffer.

   This wraps :c:func:`alBuffer3f`.

.. function:: buffer_fv(bid : int, param : int, values : iterable) -> None

   Sets a floating point-vector property of the buffer.

   This wraps :c:func:`alBufferfv`.

.. function:: buffer_i(bid : int, param : int, value : int) -> None

   Sets an integer property of the buffer.

   This wraps :c:func:`alBufferi`.

.. function:: buffer_3i(bid : int, param : int, value1 : int, value2 : int, \
                        value3 : int) -> None

   Sets an integer property of the buffer.

   This wraps :c:func:`alBuffer3i`.

.. function:: buffer_iv(bid : int, param : int, values : iterable) -> None

   Sets an integer-vector property of the buffer.

   This wraps :c:func:`alBufferiv`.

.. function:: get_buffer_f(bid : int, param : int) -> float

   Gets a floating point property of the buffer.

   This wraps :c:func:`alGetBufferf`.

.. function:: get_buffer_3f(bid : int, param : int) -> (float, float, float)

   Gets a floating point property of the buffer.

   This wraps :c:func:`alGetBuffer3f`.

.. function:: get_buffer_fv(bid : int, param : int, size : int) -> (float, float, ...)

   Gets a floating point-vector property of the buffer.

   This wraps :c:func:`alGetBufferfv`.

.. function:: get_buffer_i(bid : int, param : int) -> int

   Gets an integer property of the buffer.

   This wraps :c:func:`alGetBufferi`.

.. function:: get_buffer_3i(sid : int, param : int) -> (int, int, int)

   Gets an integer property of the buffer.

   This wraps :c:func:`alGetBuffer3i`.

.. function:: get_buffer_iv(sid : int, param : int, size : int) -> (int, int, ...)

   Gets an integer-vector property of the buffer.

   This wraps :c:func:`alGetBufferiv`.

.. function:: doppler_factor(value : float) -> None

   Sets the OpenAL doppler factor value.

   This wraps :c:func:`alDopplerFactor`.

.. function:: doppler_velocity(value : float) -> None

   Sets the speed of sound to be used in Doppler calculations.

   .. note::

      This is a legacy function from OpenAL 1.0 and should not be used
      anymore. Use :func:`speed_of_source()` instead.

   This wraps :c:func:`alDopplerVelocity`.

.. function:: speed_of_sound(value : float) -> None

   Sets the speed of sound to be used in Doppler calculuations.

   This wraps :c:func:`alSpeedOfSound`.

.. function:: distance_model(value : int) -> None

   Sets the OpenAL distance model.

   This wraps :c:func:`alDistanceModel`.
