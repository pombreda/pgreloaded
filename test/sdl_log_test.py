import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.log as log
from pygame2.compat import byteify

_ISPYPY = hasattr(sys, "pypy_version_info")
_ISIPY = sys.platform == "cli"


@unittest.skipIf(_ISPYPY, "PyPy's ctypes can't encapsule str in py_object()")
@unittest.skipIf(_ISIPY, "IronPython does not handle exceptions correctly")
class SDLLogTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        # On windows, SDL_Log* uses OutputDebugString, which does nothing,
        # if not executed in a development environment. Hence we will
        # redirect anything to stderr
        self.logdata = []

        def logfunc(userdata, category, priority, message):
            if userdata is not None:
                userdata = userdata.value
            self.logdata.append((userdata, category, priority, message,))

        # bind to the TestCase, so we do not loose the reference.
        self.funcptr = log.SDL_LogOutputFunction(logfunc)
        log.log_set_output_function(self.funcptr)
        log.log_set_all_priority(log.SDL_LOG_PRIORITY_VERBOSE)

    def tearDown(self):
        log.log_set_output_function(None)
        del self.funcptr

    def test_log_message(self):
        self.logdata = []  # reset the log
        log.log_message(log.SDL_LOG_CATEGORY_APPLICATION,
                        log.SDL_LOG_PRIORITY_VERBOSE, "test")
        self.assertEqual(self.logdata[0], (None,
                                           log.SDL_LOG_CATEGORY_APPLICATION,
                                           log.SDL_LOG_PRIORITY_VERBOSE,
                                           b"test"))
        log.log_message(log.SDL_LOG_CATEGORY_CUSTOM,
                        log.SDL_LOG_PRIORITY_CRITICAL, "test2")
        self.assertEqual(self.logdata[1], (None, log.SDL_LOG_CATEGORY_CUSTOM,
                                           log.SDL_LOG_PRIORITY_CRITICAL,
                                           b"test2"))
        log.log_message(log.SDL_LOG_CATEGORY_CUSTOM, log.SDL_LOG_PRIORITY_WARN,
                        None)
        self.assertEqual(self.logdata[2], (None, log.SDL_LOG_CATEGORY_CUSTOM,
                                           log.SDL_LOG_PRIORITY_WARN,
                                           b"None"))
        log.log_message(log.SDL_LOG_CATEGORY_CUSTOM, log.SDL_LOG_PRIORITY_WARN,
                        123)
        self.assertEqual(self.logdata[3], (None, log.SDL_LOG_CATEGORY_CUSTOM,
                                           log.SDL_LOG_PRIORITY_WARN, b"123"))

        self.assertRaises(TypeError, log.log_message, None, None, None)
        self.assertRaises(ValueError, log.log_message, 123, None, None)
        self.assertRaises(ValueError, log.log_message, 123, 456, None)
        self.assertRaises(ValueError, log.log_message, 123, 456, "Test")
        self.assertRaises(TypeError, log.log_message,
                          log.SDL_LOG_CATEGORY_CUSTOM, None, None)
        self.assertRaises(ValueError, log.log_message,
                          log.SDL_LOG_CATEGORY_CUSTOM, 123, None)
        self.assertRaises(ValueError, log.log_message,
                          log.SDL_LOG_CATEGORY_CUSTOM, 123, "Test")

    def test_log(self):
        self.logdata = []  # reset the log
        log.log("test")
        self.assertEqual(self.logdata[0],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_INFO, b"test"))
        log.log("abcdeghijk")
        self.assertEqual(self.logdata[1],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_INFO, b"abcdeghijk"))
        log.log(None)
        self.assertEqual(self.logdata[2],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_INFO, b"None"))
        log.log(123456)
        self.assertEqual(self.logdata[3],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_INFO, b"123456"))

    def test_log_critical(self):
        self.logdata = []  # reset the log
        log.log_critical(log.SDL_LOG_CATEGORY_APPLICATION, "test")
        self.assertEqual(self.logdata[0],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_CRITICAL, b"test"))
        log.log_critical(log.SDL_LOG_CATEGORY_SYSTEM, "test")
        self.assertEqual(self.logdata[1],
                         (None, log.SDL_LOG_CATEGORY_SYSTEM,
                          log.SDL_LOG_PRIORITY_CRITICAL, b"test"))
        log.log_critical(log.SDL_LOG_CATEGORY_CUSTOM, None)
        self.assertEqual(self.logdata[2], (None, log.SDL_LOG_CATEGORY_CUSTOM,
                                           log.SDL_LOG_PRIORITY_CRITICAL,
                                           b"None"))
        log.log_critical(log.SDL_LOG_CATEGORY_CUSTOM, 123)
        self.assertEqual(self.logdata[3], (None, log.SDL_LOG_CATEGORY_CUSTOM,
                                           log.SDL_LOG_PRIORITY_CRITICAL,
                                           b"123"))

        self.assertRaises(TypeError, log.log_critical, None, None)
        self.assertRaises(ValueError, log.log_critical, 123, None)
        self.assertRaises(ValueError, log.log_critical, 123, "Test")

    def test_log_debug(self):
        self.logdata = []  # reset the log
        log.log_debug(log.SDL_LOG_CATEGORY_APPLICATION, "test")
        self.assertEqual(self.logdata[0],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_DEBUG, b"test"))
        log.log_debug(log.SDL_LOG_CATEGORY_SYSTEM, "test")
        self.assertEqual(self.logdata[1], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_DEBUG,
                                           b"test"))
        log.log_debug(log.SDL_LOG_CATEGORY_SYSTEM, None)
        self.assertEqual(self.logdata[2], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_DEBUG,
                                           b"None"))
        log.log_debug(log.SDL_LOG_CATEGORY_SYSTEM, 123)
        self.assertEqual(self.logdata[3], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_DEBUG,
                                           b"123"))

        self.assertRaises(TypeError, log.log_debug, None, None)
        self.assertRaises(ValueError, log.log_debug, 123, None)
        self.assertRaises(ValueError, log.log_debug, 123, "Test")

    def test_log_error(self):
        self.logdata = []  # reset the log
        log.log_error(log.SDL_LOG_CATEGORY_APPLICATION, "test")
        self.assertEqual(self.logdata[0],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_ERROR, b"test"))
        log.log_error(log.SDL_LOG_CATEGORY_SYSTEM, "test")
        self.assertEqual(self.logdata[1], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_ERROR,
                                           b"test"))
        log.log_error(log.SDL_LOG_CATEGORY_SYSTEM, None)
        self.assertEqual(self.logdata[2], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_ERROR,
                                           b"None"))
        log.log_error(log.SDL_LOG_CATEGORY_SYSTEM, 123)
        self.assertEqual(self.logdata[3], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_ERROR,
                                           b"123"))

        self.assertRaises(TypeError, log.log_error, None, None)
        self.assertRaises(ValueError, log.log_error, 123, None)
        self.assertRaises(ValueError, log.log_error, 123, "Test")

    def test_log_info(self):
        self.logdata = []  # reset the log
        log.log_info(log.SDL_LOG_CATEGORY_APPLICATION, "test")
        self.assertEqual(self.logdata[0],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_INFO, b"test"))
        log.log_info(log.SDL_LOG_CATEGORY_SYSTEM, "test")
        self.assertEqual(self.logdata[1], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_INFO,
                                           b"test"))
        log.log_info(log.SDL_LOG_CATEGORY_SYSTEM, None)
        self.assertEqual(self.logdata[2], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_INFO,
                                           b"None"))
        log.log_info(log.SDL_LOG_CATEGORY_SYSTEM, 123)
        self.assertEqual(self.logdata[3], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_INFO,
                                           b"123"))

        self.assertRaises(TypeError, log.log_info, None, None)
        self.assertRaises(ValueError, log.log_info, 123, None)
        self.assertRaises(ValueError, log.log_info, 123, "Test")

    def test_log_verbose(self):
        self.logdata = []  # reset the log
        log.log_verbose(log.SDL_LOG_CATEGORY_APPLICATION, "test")
        self.assertEqual(self.logdata[0],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_VERBOSE, b"test"))
        log.log_verbose(log.SDL_LOG_CATEGORY_SYSTEM, "test")
        self.assertEqual(self.logdata[1], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_VERBOSE,
                                           b"test"))
        log.log_verbose(log.SDL_LOG_CATEGORY_SYSTEM, None)
        self.assertEqual(self.logdata[2], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_VERBOSE,
                                           b"None"))
        log.log_verbose(log.SDL_LOG_CATEGORY_SYSTEM, 123)
        self.assertEqual(self.logdata[3], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_VERBOSE,
                                           b"123"))

        self.assertRaises(TypeError, log.log_verbose, None, None)
        self.assertRaises(ValueError, log.log_verbose, 123, None)
        self.assertRaises(ValueError, log.log_verbose, 123, "Test")

    def test_log_warn(self):
        self.logdata = []  # reset the log
        log.log_warn(log.SDL_LOG_CATEGORY_APPLICATION, "test")
        self.assertEqual(self.logdata[0],
                         (None, log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_WARN, b"test"))
        log.log_warn(log.SDL_LOG_CATEGORY_SYSTEM, "test")
        self.assertEqual(self.logdata[1], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_WARN, b"test"))
        log.log_warn(log.SDL_LOG_CATEGORY_SYSTEM, None)
        self.assertEqual(self.logdata[2], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                           log.SDL_LOG_PRIORITY_WARN, b"None"))
        log.log_warn(log.SDL_LOG_CATEGORY_SYSTEM, 123)
        self.assertEqual(self.logdata[3], (None, log.SDL_LOG_CATEGORY_SYSTEM,
                                          log.SDL_LOG_PRIORITY_WARN, b"123"))

        self.assertRaises(TypeError, log.log_warn, None, None)
        self.assertRaises(ValueError, log.log_warn, 123, None)
        self.assertRaises(ValueError, log.log_warn, 123, "Test")

    def test_log_set_all_priority(self):
        self.assertEqual(log.log_get_priority
                         (log.SDL_LOG_CATEGORY_APPLICATION),
                         log.SDL_LOG_PRIORITY_VERBOSE)
        self.assertEqual(log.log_get_priority
                         (log.SDL_LOG_CATEGORY_SYSTEM),
                         log.SDL_LOG_PRIORITY_VERBOSE)
        log.log_set_all_priority(log.SDL_LOG_PRIORITY_WARN)
        self.assertEqual(log.log_get_priority
                         (log.SDL_LOG_CATEGORY_APPLICATION),
                         log.SDL_LOG_PRIORITY_WARN)
        self.assertEqual(log.log_get_priority
                         (log.SDL_LOG_CATEGORY_SYSTEM),
                         log.SDL_LOG_PRIORITY_WARN)
        self.assertRaises(ValueError, log.log_set_all_priority, 123)
        self.assertRaises(TypeError, log.log_set_all_priority, None)
        self.assertRaises(TypeError, log.log_set_all_priority, "test")

        # Reset to the setUp() value, so other tests do not fail
        log.log_set_all_priority(log.SDL_LOG_PRIORITY_VERBOSE)

    def test_log_set_get_priority(self):
        self.assertEqual(log.log_get_priority
                         (log.SDL_LOG_CATEGORY_APPLICATION),
                         log.SDL_LOG_PRIORITY_VERBOSE)
        self.assertEqual(log.log_get_priority(log.SDL_LOG_CATEGORY_SYSTEM),
                         log.SDL_LOG_PRIORITY_VERBOSE)
        self.assertEqual(log.log_get_priority(log.SDL_LOG_CATEGORY_CUSTOM),
                         log.SDL_LOG_PRIORITY_VERBOSE)
        log.log_set_priority(log.SDL_LOG_CATEGORY_CUSTOM,
                             log.SDL_LOG_PRIORITY_INFO)
        self.assertEqual(log.log_get_priority
                         (log.SDL_LOG_CATEGORY_APPLICATION),
                         log.SDL_LOG_PRIORITY_VERBOSE)
        self.assertEqual(log.log_get_priority(log.SDL_LOG_CATEGORY_SYSTEM),
                         log.SDL_LOG_PRIORITY_VERBOSE)
        self.assertEqual(log.log_get_priority(log.SDL_LOG_CATEGORY_CUSTOM),
                         log.SDL_LOG_PRIORITY_INFO)
        log.log_set_priority(log.SDL_LOG_CATEGORY_SYSTEM,
                             log.SDL_LOG_PRIORITY_ERROR)
        self.assertEqual(log.log_get_priority
                         (log.SDL_LOG_CATEGORY_APPLICATION),
                         log.SDL_LOG_PRIORITY_VERBOSE)
        self.assertEqual(log.log_get_priority(log.SDL_LOG_CATEGORY_SYSTEM),
                         log.SDL_LOG_PRIORITY_ERROR)
        self.assertEqual(log.log_get_priority(log.SDL_LOG_CATEGORY_CUSTOM),
                         log.SDL_LOG_PRIORITY_INFO)
        self.assertRaises(TypeError, log.log_set_priority, None, None)
        self.assertRaises(TypeError, log.log_set_priority, "Test", None)
        self.assertRaises(ValueError, log.log_set_priority, 123, None)
        self.assertRaises(ValueError, log.log_set_priority, 123, "Test")
        self.assertRaises(TypeError, log.log_set_priority,
                          log.SDL_LOG_CATEGORY_APPLICATION, None)
        self.assertRaises(TypeError, log.log_set_priority,
                          log.SDL_LOG_CATEGORY_APPLICATION, "Test")
        self.assertRaises(ValueError, log.log_set_priority,
                          log.SDL_LOG_CATEGORY_APPLICATION, 123)

        self.assertRaises(TypeError, log.log_get_priority, None)
        self.assertRaises(TypeError, log.log_get_priority, "Test")
        self.assertRaises(ValueError, log.log_get_priority, 123)

    def test_log_reset_priorities(self):
        # set in setUp()
        defpriority = log.SDL_LOG_PRIORITY_VERBOSE
        categories = (
            log.SDL_LOG_CATEGORY_APPLICATION,
            log.SDL_LOG_CATEGORY_ERROR,
            log.SDL_LOG_CATEGORY_SYSTEM,
            log.SDL_LOG_CATEGORY_AUDIO,
            log.SDL_LOG_CATEGORY_VIDEO,
            log.SDL_LOG_CATEGORY_RENDER,
            log.SDL_LOG_CATEGORY_INPUT,
            log.SDL_LOG_CATEGORY_CUSTOM
            )
        for cat in categories:
            priority = log.log_get_priority(cat)
            self.assertEqual(priority, defpriority)

        log.log_reset_priorities()
        for cat in categories:
            priority = log.log_get_priority(cat)
            self.assertNotEqual(priority, defpriority)

        log.log_set_all_priority(log.SDL_LOG_PRIORITY_VERBOSE)

    def test_log_get_set_output_function(self):
        logentries = []

        def __log(userdata, category, priority, message):
            logentries.append((userdata, category, priority, message,))

        # setUp should have set our output function already.
        origfunc, origdata = log.log_get_output_function()
        self.assertIsNone(origdata)
        logcount = len(self.logdata)
        origfunc(None, 0, 0, b"test_log_get_set_output_function")
        self.assertEqual(len(self.logdata), logcount + 1)
        self.assertEqual(self.logdata[logcount][3],
                         b"test_log_get_set_output_function")

        logptr = log.SDL_LogOutputFunction(__log)
        log.log_set_output_function(logptr, "Testobject")
        ptr, userdata = log.log_get_output_function()
        self.assertEqual(userdata, "Testobject")
        log.log("output test")
        self.assertEqual(logentries[0],
                         ("Testobject", log.SDL_LOG_CATEGORY_APPLICATION,
                          log.SDL_LOG_PRIORITY_INFO, b"output test"))

        log.log_set_output_function(origfunc, userdata)

if __name__ == '__main__':
    unittest.main()
