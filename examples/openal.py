"""Pure OpenAL playback example."""
import os
import sys
import time
import wave
from pygame2.resources import Resources
import pygame2.openal.al as al
import pygame2.openal.alc as alc

RESOURCES = Resources(__file__, "resources")

def run():
    if len (sys.argv) < 2:
        print ("Usage: %s wavefile" % os.path.basename(sys.argv[0]))
        print ("    Using an example wav file...")
        wavefp = wave.open(RESOURCES.get("hey.wav"))
    else:
        wavefp = wave.open(sys.argv[1], "rb")

    channels = wavefp.getnchannels()
    bitrate = wavefp.getsampwidth() * 8
    samplerate = wavefp.getframerate()
    wavbuf = wavefp.readframes(wavefp.getnframes())
    formatmap = {
        (1, 8) : al.AL_FORMAT_MONO8,
        (2, 8) : al.AL_FORMAT_STEREO8,
        (1, 16): al.AL_FORMAT_MONO16,
        (2, 16) : al.AL_FORMAT_STEREO16,
    }
    alformat = formatmap[(channels, bitrate)]

    device = alc.open_device()
    context = alc.create_context(device)
    alc.make_context_current(context)

    sources = al.gen_sources(1)

    al.source_f(sources[0], al.AL_PITCH, 1)
    al.source_f(sources[0], al.AL_GAIN, 1)
    al.source_3f(sources[0], al.AL_POSITION, 0, 0, 0)
    al.source_3f(sources[0], al.AL_VELOCITY, 0, 0, 0)

    buffers = al.gen_buffers(1)

    al.buffer_data(buffers[0], alformat, wavbuf, samplerate)
    al.source_queue_buffers(sources[0], buffers)
    al.source_play(sources[0])

    state = al.get_source_i(sources[0], al.AL_SOURCE_STATE)
    while state == al.AL_PLAYING:
        print("playing the file...")
        time.sleep(1)
        state = al.get_source_i(sources[0], al.AL_SOURCE_STATE)
    print("done")

    al.delete_sources(sources)
    al.delete_buffers(buffers)
    alc.destroy_context(context)
    alc.close_device(device)

if __name__ == "__main__":
    sys.exit(run())
