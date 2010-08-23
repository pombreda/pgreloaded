import unittest
import pygame2
import pygame2.sdlmixer as sdlmixer
import pygame2.sdlmixer.music as sdlmusic


class SDLMixerMusicTest (unittest.TestCase):
    __tags__ = [ "sdl", "sdlmixer" ]

    def todo_test_pygame2_sdlmixer_Music_fade_in(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Music.fade_in:

        # fade_in (ms[, loops, pos]) -> None
        # 
        # Fades in the Music.
        # 
        # This starts playing the Music at volume 0, which fades up to
        # the maximum value over *ms* milliseconds. The Music will be played
        # for *loops* + 1 number of times.
        # 
        # *pos* is the position to start the playback from.

        self.fail()

    def todo_test_pygame2_sdlmixer_Music_play(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Music.play:

        # play ([loops]) -> None
        # 
        # Starts the playback of the Music.
        # 
        # Starts the playback of the Music. The music will be played once, if
        # *loops* is omitted, otherwise it will be played *loops* + 1 times.
        # If *loops* is set to -1, the music will be played in an endless loop.

        self.fail()

    def todo_test_pygame2_sdlmixer_Music_type(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.Music.type:

        # Gets the music format.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_fade_out(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.fade_out:

        # fade_out (ms) -> None
        # 
        # Fades out the current music playback.
        # 
        # This gradually reduces the volume for the current music to 0 over *ms*
        # milliseconds. The music will be halted after the fadeout is complete.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_fading(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.fading:

        # fading () -> int
        # 
        # Gets the fading status of the music.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_get_decoders(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.get_decoders:

        # get_decoders () -> [str, str, ...]
        # 
        # Gets a list of music decoders that are provided by the underlying SDL_mixer library.
        # 
        # Gets a list of music decoders that are provided by the underlying
        # SDL_mixer library. For sound decoders, use the
        # pygame2.sdlmixer.get_decoders function.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_get_volume(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.get_volume:

        # get_volume () -> int
        # 
        # Gets the volume of the music.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_halt(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.halt:

        # halt () -> None
        # 
        # Halts the music playback and resets its state.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_pause(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.pause:

        # pause () -> None
        # 
        # Pauses the music playback.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_paused(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.paused:

        # paused () -> bool
        # 
        # Gets, whether the music playback is currently paused.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_playing(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.playing:

        # playing () -> bool
        # 
        # Gets, whether the music is currently playing.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_resume(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.resume:

        # resume () -> None
        # 
        # Resumes the previously paused music playback

        self.fail()

    def todo_test_pygame2_sdlmixer_music_rewind(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.rewind:

        # rewind () -> None
        # 
        # Rewinds the music to the start.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_set_position(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.set_position:

        # set_position (pos) -> None
        # 
        # Sets the current playback position.

        self.fail()

    def todo_test_pygame2_sdlmixer_music_set_volume(self):

        # __doc__ (as of 2010-08-22) for pygame2.sdlmixer.music.set_volume:

        # set_volume (volume) -> int
        # 
        # Sets the volume for the music.
        # 
        # Sets the volume for the music and returns the previous set volume.
        # The volume can be a numeric integer in the range [0, 128].

        self.fail()

if __name__ == "__main__":
    unittest.main ()
