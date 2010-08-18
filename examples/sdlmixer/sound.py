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
    import pygame2.sdlmixer.channel as sdlmixerchannel
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

    sound = sdlmixer.Chunk (pygame2.examples.RESOURCES.get ("house_lo.wav"))
    channel_sound = sdlmixer.Channel (1)

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
                    if channel_sound.paused:
			print ("Resuming")
                        channel_sound.resume ()
                    elif channel_sound.playing:
			print ("Pausing")
                        channel_sound.pause ()
                    else:
			print ("Starting")
                        channel_sound.play (sound, -1)
                if ev.key == sdlconst.K_ESCAPE:
                    # exit the application
                    okay = False
                elif ev.key in (sdlconst.K_PLUS, sdlconst.K_KP_PLUS):
                    # increase volume
                    channel_sound.volume = min (channel_sound.volume + 1,
                                                sdlmixerconst.MAX_VOLUME)
                    print ("Volume is now: %d" % channel_sound.volume)
                elif ev.key in (sdlconst.K_MINUS, sdlconst.K_KP_MINUS):
                    # decrease volume
                    channel_sound.volume = max (channel_sound.volume - 1, 0)
                    print ("Volume is now: %d" % channel_sound.volume)

        screen.fill (black)
        screen.flip ()
    
    video.quit ()
    sdlmixer.close_audio ()
    sdlmixer.quit ()

if __name__ == "__main__":
    run ()
