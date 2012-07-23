import sys
import os
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.power as power
from pygame2.test.util.testutils import interactive, doprint


class SDLPowerTest(unittest.TestCase):
    __tags__ = ["sdl"]

    @interactive("Do the shown numbers match your power supply status?")
    def test_get_power_info(self):
        retval = power.get_power_info()
        state = "Unknown"
        if retval[0] == power.SDL_POWERSTATE_ON_BATTERY:
            state = "On battery"
        elif retval[0] == power.SDL_POWERSTATE_NO_BATTERY:
            state = "No battery"
        elif retval[0] == power.SDL_POWERSTATE_CHARGING:
            state = "Battery charging"
        elif retval[0] == power.SDL_POWERSTATE_CHARGED:
            state = "Battery charged"
        output = "Power Status: %s" % state + os.linesep
        output += "Minutes left (-1 = undetermined): %d" % (retval[1] / 60) + \
            os.linesep
        output += "Percent left (-1 = undetermined): %d" % retval[2] + \
            os.linesep
        doprint(output)

if __name__ == '__main__':
    sys.exit(unittest.main())
