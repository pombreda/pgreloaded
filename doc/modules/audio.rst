.. module:: pygame2.audio
   :synopsis: Audio in- and output routines.

:mod:`pygame2.audio` - Audio in- and output routines
====================================================

The :mod:`pygame2.audio` module provides easy to use audio in- and output
capabilities based on the OpenAL standard. It is designed to be non-invasive
within a component-based application.

At least three classes need to be used for playing back audio data. The
:class:`SoundSink` handles the audio device connection and controls the overall
playback mechanisms. The :class:`SoundSource` represents an in-application
object that emits sounds and a :class:`SoundData` contains the PCM audio data
to be played.

The OpenAL standard supports 3D positional audio, so that a source of sound
can be placed anywhere relative to the listener (the user of the application
or some in-application avatar).

TODO: insert graphics

Device handling
---------------

To actually play back sound or to stream sound to a third-party system (e.g.
a sound server or file), an audio output device needs to be opened. It usually
allows the software to access the audio hardware via the operating system, so
that audio data can be recorded or played back.

   >>> sink = SoundSink()        # Open the default audio output device
   >>> sink = SoundSink("oss")   # Open the OSS audio output device
   >>> sink = SoundSink("winmm") # Open the Windows MM audio output device
   ...

.. note::

   Depending on what to accomplish and what kind of quality for audio output to
   have, one might use a specific audio output device to be passed as argument
   to the :class:`SoundSink` constructor.

Placing the listener
--------------------

TODO


Creating sound sources
----------------------

As said earlier, a :class:`SoundSource` represents an object that can emit
sounds. TODO


Creating sounds
---------------


Audio API
---------

.. data:: SOURCE_NONE

   Indicates that no specific action should be performed on processing the
   :class:`SoundSource`

.. data:: SOURCE_PLAY

   Indicates that the :class:`SoundSource` shall play its :class:`SoundData`.

.. data:: SOURCE_PAUSE

   Indicates that the :class:`SoundSource` shall pause playing.

.. data:: SOURCE_STOP

   Indicates that the :class:`SoundSource` shall stop playing.

.. data:: SOURCE_REWIND

    Indicates that the :class:`SoundSource` shall rewind to the start of the
    currently processed :class:`SoundData` buffer.


.. class:: SoundData()

   Buffered audio data.

   .. attribute:: bufid

      The OpenAL buffer id, if any. This will be set automatically by the
      :class:`SoundSink`, if the :class:`SoundData` is processed.

   .. attribute:: format

      The format of the audio data.

   .. attribute:: data

      A buffer containing the raw PCM data to play.

   .. attribute:: size

      The size of the audio buffer.

   .. attribute:: frequency

      The frequency of the audio data.


.. class:: SoundListener()

   Listener position information for the 3D audio environment.

   .. attribute:: position

      The (initial) position of the listener as 3-value tuple within a x-y-z
      coordinate system.

   .. attribute:: velocity

      The velocity of the listener as 3-value tuple within a x-y-z coordinate
      system.

   .. attribute:: orientation

      The forward (in which direction does the listener look) orientation of
      the listener as 4-value tuple within a x-y-z coordinate system.


.. class:: SoundSource()

   xxx

   .. attribute:: ssid

      The OpenAL source id, if any. This will be set automatically by the
      :class:`SoundSink`, if the :class:`SoundSource` is processed.

   .. attribute:: gain

      The volume gain of the source.

   .. attribute:: pitch

      The pitch of the source.

   .. attribute:: position

      The (initial) position of the source as 3-value tuple in a x-y-z
      coordinate system.

   .. attribute:: velocity

      The velocity of the source as 3-value tuple in a x-y-z coordinate system.

   .. attribute:: request

      The action to be performed by the :class:`SoundSink`, when it processes
      the :class:`SoundSource`

   .. method:: queue(sounddata : SoundData) -> None

      Adds a :class:`SoundData` audio buffer to the source's processing and
      playback queue.


.. class:: SoundSink(device=None)

   Audio playback system.

   The SoundSink handles audio output for sound sources. It connects to an
   audio output device and manages the source settings, their buffer queues
   and the playback of them.

   .. attribute:: device

      The used OpenAL :class:`pygame2.alc.ALCdevice`.

   .. attribute:: context

      The used :class:`pygame2.alc.ALCcontext`.

   .. method:: activate() -> None

      Activates the :class:`SoundSink`, marking its :attr:`context` as the
      currently active one.

      Subsequent OpenAL operations are done in the context of the
      SoundSink's bindings.

   .. method:: set_listener(listener : SoundListener) -> None

      Sets the listener position for the :class:`SoundSink`.

      .. note::

         This implicitly activates the :class:`SoundSink`.

   .. method:: process_source(source : SoundSource) -> None

      Processes a single :class:`SoundSource`.

      .. note::

        This does *not* activate the :class:`SoundSink`. If another
        :class:`SoundSink` is active, chances are good that the
        source is processed in that :class:`SoundSink`.

   .. method:: process(world, components) -> None

      Processes :class:`SoundSource` components, according to their
      :attr:`SoundSource.request`

      .. note::

         This implicitly activates the :class:`SoundSink`.


.. function:: load_file(fname : string) -> SoundData

   Loads an audio file into a :class:`SoundData` object.

.. function:: load_stream(source : object) -> SoundData

   Not implemented yet.

.. function:: load_wav_file(fname : string) -> SoundData

   Loads a WAV audio file into a :class:`SoundData` object.

.. function:: load_ogg_file(fname : string) -> SoundData

   Loads an Ogg Vorbis audio file into a :class:`SoundData` object.

   .. note::

      This requires the :mod:`pygame2.ogg.voribsfile` module.
