import unittest
import time
import pygame2
import pygame2.sdlmixer as sdlmixer
import pygame2.sdlmixer.constants as mixconst
import pygame2.sdlmixer.channel as sdlchannel

class SDLMixerChannelTest (unittest.TestCase):
    __tags__ = [ "sdl", "sdlmixer" ]

    def setUp (self):
        sdlmixer.init ()
	sdlmixer.open_audio (mixconst.DEFAULT_FREQUENCY,
                             mixconst.DEFAULT_FORMAT,
                             mixconst.DEFAULT_CHANNELS, 1024)
    def tearDown (self):
        sdlmixer.close_audio ()
        sdlmixer.quit ()

    def todo_test_pygame2_sdlmixer_Channel_chunk(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.chunk:

        # The current Chunk of audio data to be played.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_expire(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.expire:

        # expire (ms) -> None
        # 
        # Halts the playback of the Channel after *ms* milliseconds.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_fade_in(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.fade_in:

        # fade_in (sound, ms[, loops, ticks]) -> None
        # 
        # Fades in the passed sound.
        # 
        # This starts playing the passed *sound* at volume 0, which fades up to
        # the maximum value over *ms* milliseconds. The *sound* will be played
        # for *loops* + 1 number of times.
        # 
        # *ticks* is the optional maximum time in milliseconds to stop playing
        # after.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_fade_out(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.fade_out:

        # fade_out (ms) -> None
        # 
        # Fades out the current audio playback.
        # 
        # This gradually reduces the volume to 0 over *ms* milliseconds. The channel
        # will be halted after the fadeout is complete.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_fading(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.fading:

        # The fading status of the Channel.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_halt(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.halt:

        # halt () -> None
        # 
        # Stops the audio playback immediately and resets the playback state

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_pause(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.pause:

        # pause () -> None
        # 
        # Pauses the current audio playback.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_paused(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.paused:

        # Gets, whether the Channel playback is currently paused.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_play(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.play:

        # play (sound[, loops, ticks]) -> None
        # 
        # Starts the playback of an audio Chunk.
        # 
        # The audio chunk will be played for *loops* + 1 times (or one
        # time only, if *loops* is omitted). If *loops* is set to -1, the
        # sound will be played in an endless loop.
        # 
        # *ticks* is the optional maximum time in milliseconds to stop playing
        # after.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_playing(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.playing:

        # Gets, whether the Channel is currently playing audio.
        # 
        # NOTE:
        # 
        # This will be also be True, if the Channel is paused.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_resume(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.resume:

        # resume () -> None
        # 
        # Resumes the playback of a paused sound chunk.

        self.fail()

    def todo_test_pygame2_sdlmixer_Channel_volume(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Channel.volume:

        # Gets or sets the channel volume. The volume can be a numeric
        # integer in the range [0, 128].

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_allocate(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.allocate:

        # allocate (amount) -> (Channel, Channel, ...)
        # 
        # (Pre-)Allocates a set of Channel objects.

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_expire(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.expire:

        # expire (ms) -> None
        # 
        # Halts the playback of all channels after *ms* milliseconds.

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_fade_out(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.fade_out:

        # fade_out (ms) -> int
        # 
        # Fades out the current audio playback for all channels.
        # 
        # This gradually reduces the volume for all channels to 0 over *ms*
        # milliseconds. The channels will be halted after the fadeout is complete.
        # 
        # The number of channels set to fade out will be returned.

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_get_volume(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.get_volume:

        # get_volume () -> int
        # 
        # Gets the currently set overall volume for all Channel objects.

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_halt(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.halt:

        # halt () -> None
        # 
        # Stops the sound playback for all Channel objects.

        self.fail()

    def test_pygame2_sdlmixer_channel_opened(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.opened:

        # opened () -> int
        # 
        # Gets the number of currently open (allocated) channels.

        channels = sdlchannel.allocate (8)
        self.assertEquals (sdlchannel.opened (), len (channels))
        channels = sdlchannel.allocate (3)
        self.assertEquals (sdlchannel.opened (), len (channels))

    def todo_test_pygame2_sdlmixer_channel_pause(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.pause:

        # pause () -> None
        # 
        # Pauses the sound playback for all Channel objects.

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_paused(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.paused:

        # paused () -> int
        # 
        # Gets the number of channels being currently paused.

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_playing(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.playing:

        # playing () -> int
        # 
        # Gets the number of channels currently playing.

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_resume(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.resume:

        # resume () -> None
        # 
        # Resumes the playback for all paused Channel objects.

        self.fail()

    def todo_test_pygame2_sdlmixer_channel_set_volume(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.channel.set_volume:

        # set_volume (volume) -> int
        # 
        # Sets the overall volume for all available Channel objects.
        # 
        # Sets the volume for all available Channel objects and returns the previous
        # set volume.

        self.fail()

if __name__ == "__main__":
    unittest.main ()
