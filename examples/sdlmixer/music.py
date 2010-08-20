import os, sys, time
import pygame2
import pygame2.examples
try:
    import pygame2.sdl.constants as sdlconst
    import pygame2.sdl.event as event
    import pygame2.sdl.video as video
    import pygame2.sdl.wm as wm
except ImportError:
    print ("No pygame2.sdl support")
    sys.exit ()

try:
    import pygame2.sdlmixer as sdlmixer
    import pygame2.sdlmixer.music as sdlmixermusic
    import pygame2.sdlmixer.constants as sdlmixerconst
except ImportError:
    print ("No pygame2.sdlmixer support")
    sys.exit ()

black = pygame2.Color (0, 0, 0)
white = pygame2.Color (255, 255, 255)

def run ():
    video.init ()
    sdlmixer.init ()
    sdlmixer.open_audio (sdlmixerconst.DEFAULT_FREQUENCY,
                         sdlmixerconst.DEFAULT_FORMAT,
                         sdlmixerconst.DEFAULT_CHANNELS,
                         1024)
    print ("Detected decoders: %s" % sdlmixermusic.get_decoders ())

    music = sdlmixer.Music (pygame2.examples.RESOURCES.get ("house_lo.wav"))

    if music.type == sdlmixerconst.MUS_NONE:
        print ("Music format could not be detected")
    elif music.type == sdlmixerconst.MUS_CMD:
        print ("Music is an external command")
    elif music.type == sdlmixerconst.MUS_WAV:
        print ("Music has WAV format")
    elif music.type == sdlmixerconst.MUS_OGG:
        print ("Music has OGG format")
    elif music.type == sdlmixerconst.MUS_MOD:
        print ("Music has MOD format")
    elif music.type == sdlmixerconst.MUS_MID:
        print ("Music has MIDI format")
    elif music.type == sdlmixerconst.MUS_MP3:
        print ("Music has MP3/smpeg format")
    elif music.type == sdlmixerconst.MUS_MP3_MAD:
        print ("Music has MP3/MAD format")
    elif music.type == sdlmixerconst.MUS_FLAC:
        print ("Music has FLAC format")
    
    screen = video.set_mode (640, 480)
    wm.set_caption ("SDL_mixer sound example")

    screenrect = pygame2.Rect (640, 480)
    screen.fill (black)
    screen.flip ()

    okay = True
    while okay:
        for ev in event.get ():
            if ev.type == sdlconst.QUIT:
                okay = False
            if ev.type == sdlconst.KEYDOWN:
                # play, pause, resume
                if ev.key == sdlconst.K_SPACE:
                    if sdlmixermusic.paused ():
                        print ("Resuming")
                        sdlmixermusic.resume ()
                    elif sdlmixermusic.playing ():
                        print ("Pausing")
                        sdlmixermusic.pause ()
                    else:
                        print ("Playing")
                        music.play ()
                if ev.key == sdlconst.K_ESCAPE:
                    # exit the application
                    okay = False
                elif ev.key in (sdlconst.K_PLUS, sdlconst.K_KP_PLUS):
                    # increase volume
                    sdlmixermusic.set_volume (min (channel_sound.volume + 1,
                                                   sdlmixerconst.MAX_VOLUME))
                    print ("Volume is now: %d" % sdlmixermusic.get_volume ())
                elif ev.key in (sdlconst.K_MINUS, sdlconst.K_KP_MINUS):
                    # decrease volume
                    sdlmixermusic.set_volume (max (channel_sound.volume - 1, 0))
                    print ("Volume is now: %d" % sdlmixermusic.get_volume ())

        screen.fill (black)
        screen.flip ()
    
    video.quit ()
    sdlmixer.close_audio ()
    sdlmixer.quit ()

if __name__ == "__main__":
    run ()