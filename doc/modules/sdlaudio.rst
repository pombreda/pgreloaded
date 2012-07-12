.. module:: pygame2.sdl.audio
   :synopsis: SDL2 Audio wrapper

:mod:`pygame2.sdl.audio` - SDL2 Audio  wrapper
==============================================

SDL2 Audio API
--------------

.. function:: SDL_AUDIO_BITSIZE(x : int) -> bool

   Gets the bitsize of an audio format.

   This wraps :c:func:`SDL_AUDIO_BITSIZE()`.

.. function:: SDL_AUDIO_ISFLOAT(x : int) -> bool

   Checks, if the audio format is a float format.

   This wraps :c:func:`SDL_AUDIO_ISFLOAT()`.

.. function:: SDL_AUDIO_ISBIGENDIAN(x : int) -> bool

   Checks, if the audio format is in big-endian byte order.

   This wraps :c:func:`SDL_AUDIO_ISBIGENDIAN`.

.. function:: SDL_AUDIO_ISSIGNED(x : int) -> bool

   Checks, if the audio format uses signed values.

   This wraps :c:func:`SDL_AUDIO_ISSIGNED`.

.. function:: SDL_AUDIO_ISINT(x : int) -> bool

   Checks, if the audio format is an int format.

   This wraps :c:func:`SDL_AUDIO_ISINT`.

.. function:: SDL_AUDIO_ISLITTLEENDIAN(x : int) -> bool

   Checks, if the audio format is in little-endian byte order.

   This wraps :c:func:`SDL_AUDIO_ISLITTLEENDIAN`.

.. function:: SDL_AUDIO_ISUNSIGNED(x : int) -> bool

   Checks, if the audio format usses unsigned values.

   This wraps :c:func:`SDL_AUDIO_ISUNSIGNED`.

.. function:: get_num_audio_drivers() -> int

   Gets the number of built in audio drivers.

   This wraps :c:func:`SDL_GetNumAudioDrivers`.

.. function:: get_audio_driver(index : int) -> string

   Gets the name of a specific audio driver.

   This wraps :c:func:`SDL_GetAudioDriver`.

.. function:: audio_init(drivername : string) -> None

   Initializes the SDL audio subsystem with the passed driver.

   .. note::

      Do not use :func:`audio_init()` - this might lead to SIGSEGV
      crashes - use the ``SDL_AUDIODRIVER`` environment variable before
      calling :func:`pygame2.sdl.init_subsystem()` instead.

   This wraps :c:func:`SDL_AudioInit`.

.. function:: audio_quit() -> None

   Quits the SDL audio subsystem.

   .. note::

      Do not use :func:`audio_quit()` - this might lead to inconsistent
      internal SDL2 states - use :func:`pygame2.sdl.quit_subsystem()`
      instead.

   This wraps :c:func:`SDL_AudioQuit`.

.. function:: get_current_audio_driver() -> string

   Gets the currently used audio driver.

   This wraps :c:func:`SDL_GetCurrentAudioDriver`.

.. function:: open_audio(desired : SDL_AudioSpec) -> SDL_AudioSpec

   Opens the audio device with the desired :class:`SDL_AudioSpec`
   parameters. If the return value is ``None``, the audio data passed
   to the set callback function in desired will be guaranteed to be in
   the requested format, and will be automatically converted to the
   hardware audio format if necessary.

   This wraps :c:func:`SDL_OpenAudio`.

.. function:: get_num_audio_devices(iscapture=False) -> int

   Gets the number of available audio devices.

   If *iscapture* is ``True``, only input (capture) devices are queried,
   otherwise only output devices are queried. In some cases, this might
   return -1, indicating that the number of available devices could not
   be determined (e.g. for network sound servers). You should check for
   an error by calling :func:`pygame2.sdl.get_error()` in those cases.

   This wraps :c:func:`SDL_GetNumAudioDevices`.

.. function:: get_audio_device_name(index : int, iscapture=False) -> string

   Gets the name of an audio device. If *iscapture* is ``True`` , only input
   (capture) devices are queried, otherwise only output devices are queried.

   This wraps :c:func:`SDL_GetAudioDeviceName`.

.. function:: open_audio_device(device : int, iscapture : bool, \
                                desired : SDL_AudioSpec, \
                                allowed_changes : int) -> int

   TODO

   This wraps :c:func:`SDL_OpenAudioDevice`.

.. function:: get_audio_status() -> int

   TODO

   This wraps :c:func:`SDL_GetAudioStatus`.

.. function:: get_audio_device_status(device : int) -> int

   TODO

   This wraps :c:func:`SDL_GetAudioDeviceStatus`.

.. function:: pause_audio(pause_on : bool) -> None

   TODO

   This wraps :c:func:`SDL_PauseAudio`.

.. function:: pause_audio_device(device : int, pause_on : bool) -> None

   TODO

   This wraps :c:func:`SDL_PauseAudioDevice`.

.. function:: load_wav_rw(rwops : SDL_RWops, freesrc : bool) \
              -> (SDL_AudioSpec, bytes, int)

   TODO

   This wraps :c:func:`SDL_LoadWAV_RW`.

.. function:: load_wav(filename : string) -> (SDL_AudioSpec, bytes, int)

   TODO

   This wraps :c:func:`SDL_LoadWAV`.

.. function:: free_wav(buf : bytes) -> None

   TODO

   This wraps :c:func:`SDL_FreeWAV`.

.. function:: build_audio_cvt(src_format : int, src_channels : int, \
                          src_rate : int, dst_format : int, \
                          dst_channels : int, dst_rate : int) -> SDL_AudioCVT

   TODO

   This wraps :c:func:`SDL_BuildAudioCVT`.

.. function:: convert_audio(cvt : SDL_AudioCVT) -> None

   TODO

   This wraps :c:func:`SDL_`.

.. function:: mix_audio(dst : bytes, src : bytes, length, volume) -> None

   TODO

   This wraps :c:func:`SDL_MixAudio`.

.. function:: mix_audio_format(dst : bytes, src : bytes, aformat : int, \
                               length : int, volume : int) -> None

   TODO

   This wraps :c:func:`SDL_MixAudioFormat`.

.. function:: lock_audio() -> None

   TODO

   This wraps :c:func:`SDL_LockAudio`.

.. function:: unlock_audio() -> None

   TODO

   This wraps :c:func:`SDL_UnlockAudio`.

.. function:: lock_audio_device(device : int) -> None

   TODO

   This wraps :c:func:`SDL_LockAudioDevice`.

.. function:: unlock_audio_device(device : int) -> None

   TODO

   This wraps :c:func:`SDL_UnlockAudioDevice`.

.. function:: close_audio() -> None

   TODO

   This wraps :c:func:`SDL_CloseAudio`.

.. function:: close_audio_device(device : int) -> None

   TODO

   This wraps :c:func:`SDL_CloseAudioDevice`.

.. class:: SDL_AudioSpec(frequency, aformat, channels, samples, \
                         callback[, userdata=None])

   Audio specification.

   This wraps :c:func:`SDL_AudioSpec`.

.. class:: SDL_AudioCVT()

   TODO

   This wraps :c:func:`SDL_AudioCVT`.

.. class:: SDL_AudioCallback(callback)

   TODO

   This wraps :c:func:`SDL_AudioCallback`.

.. class:: SDL_AudioFilter(callback)

   TODO

   This wraps :c:func:`SDL_AudioFilter`.
