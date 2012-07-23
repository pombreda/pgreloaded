import sys
import time
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.timer as timer

if sys.version_info[0] >= 3:
    long = int


class SDLTimerTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        sdl.init(sdl.SDL_INIT_TIMER)
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        sdl.quit_subsystem(sdl.SDL_INIT_TIMER)
        sdl.quit()

    def test_get_ticks(self):
        ticks = timer.get_ticks()
        time.sleep(1)
        ticks2 = timer.get_ticks()
        time.sleep(1)
        ticks3 = timer.get_ticks()
        # Add some latency, since the final numbers can heavily depend
        # on the system's context switching behaviour, load, etc., etc.,
        # etc.
        self.assertTrue(abs(ticks2 - 1000 - ticks) <= 3,
            "%f is not <= 3 for %f and %f" % (abs(ticks2 - 1000 - ticks),
                                              ticks2, ticks))
        self.assertTrue(abs(ticks3 - 1000 - ticks2) <= 3,
            "%f is not <= 3 for %f and %f" % (abs(ticks3 - 1000 - ticks2),
                                              ticks3, ticks2))
        self.assertTrue(abs(ticks3 - 2000 - ticks) <= 3,
            "%f is not <= 3 for %f and %f" % (abs(ticks3 - 2000 - ticks2),
                                              ticks3, ticks))

    def test_get_performance_counter(self):
        perf = timer.get_performance_counter()
        self.assertTrue(type(perf) in (int, long))

    def test_get_performance_frequency(self):
        freq = timer.get_performance_frequency()
        self.assertTrue(type(freq) in (int, long))

    def test_delay(self):
        for wait in range(5, 200, 5):
            start = time.time() * 1000
            timer.delay(wait)
            end = time.time() * 1000
            sum = (end - start)
            self.assertTrue(abs(wait - sum) <= 3,
                "%f is not <= 3 for %f and %f" % (abs(wait - sum), wait, sum))

    @unittest.skipIf(hasattr(sys, "pypy_version_info"),
                     "PyPy's ctypes can't encapsule str in py_object()")
    def test_add_remove_timer(self):
        calls = []

        def timerfunc(interval, param):
            calls.append(param)
            return interval

        callback = timer.SDL_TimerCallback(timerfunc)
        timerid = timer.add_timer(100, callback, "Test")
        start = timer.get_ticks()
        end = start
        while(end - start) < 1100:
            # One second wait
            end = timer.get_ticks()
        # check for <=11, since it can happen that a last call is still
        # executing
        self.assertLessEqual(len(calls), 11)
        timer.remove_timer(timerid)
        self.assertLessEqual(len(calls), 11)
        timer.remove_timer(timerid)
        # Wait a bit, so the last executing handlers can finish
        timer.delay(10)


if __name__ == '__main__':
    sys.exit(unittest.main())
