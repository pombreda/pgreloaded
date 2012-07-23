"""Audio playback example."""
import sys
import time

# Import the example resources, so that we can use one of the shipped
# WAV files.
from pygame2.resources import Resources
RESOURCES = Resources(__file__, "resources")

# Try to import the audio system and OpenAL bindings, so that we are
# able to play sounds through OpenAL. the al import is only necessary,
# since we will check, whether the sound is still playing in the code
# below.
try:
    import pygame2.audio as audio
    import pygame2.openal.al as al
except ImportError:
    import traceback
    traceback.print_exc()
    sys.exit(1)


def run():
    # We can use OpenAL directly to play some sound, there is no
    # necessity to use the audio module. This however is a bit more
    # complex (read: involves writing more code) and less
    # comfortable. For a direct OpenAL example, check the openal.py
    # example file.

    # Create a SoundSink. It is used do the output device handling,
    # source and audio buffer management and anything else necessary
    # to play sounds.
    #
    # You can create multiple sinks for different audio devices or for
    # the same device, so that you can e.g. manage different positions
    # for listening to sounds.
    sink = audio.SoundSink()

    # Create a SoundSource. The SoundSource defines an object within
    # your application world, that can emit sounds. It could be e.g. a
    # spaceship within your game, the general output object within your a
    # music player application, ...
    source = audio.SoundSource()

    # Load a SoundData object from the passed WAV file. A SoundData is
    # nothing more than a raw audio buffer (as PCM data), along with
    # some information about its channels, bit rate and frequency.
    data = audio.load_file(RESOURCES.get_path("hey.wav"))

    # Add the SoundData to the source, so that it will be played, when
    # the source is processed by the SoundSink.
    source.queue(data)

    # Tell the SoundSource that it shall be played on the next
    # processing by the SoundSink. This will cause the SoundSink to
    # buffer all attached SoundData objects of the SoundSource and play
    # them in order.
    source.request = audio.SOURCE_PLAY
    sink.process_source(source)

    # The main loop. In contrast to other exampes, we are checking the
    # status of our previously created source directly. Once it is done
    # playing, we exit from the loop to finish the program execution.
    #
    # The OpenAL sound system uses its own threads to play sounds and
    # music so that we do not not handle it explicitly, if we do not
    # need to perform more complex or synchronised operations. Hence,
    # once a SoundSource was requested to play something and got
    # processed, there is not much more left to do.
    while True:
        state = al.get_source_i(source.ssid, al.AL_SOURCE_STATE)
        if state == al.AL_PLAYING:
            print("playing...")
        else:
            print("done")
            break
        time.sleep(2)


if __name__ == "__main__":
    sys.exit(run())
