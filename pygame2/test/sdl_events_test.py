import sys
import unittest
import pygame2.sdl as sdl
import pygame2.sdl.events as events

if hasattr(sys, "pypy_version_info"):
    print("")
    print("    *** PyPy's ctypes can't encapsule str in py_object() ***")
    print("    *** Using a class as workaround                      ***")

    class pypycapsule(object):
        def __init__(self, data):
            self.data = data
        def __repr__(self):
            return repr(self.data)
else:
    pypycapsule = str


class SDLEventsTest(unittest.TestCase):
    __tags__ = ["sdl"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))
        sdl.init(sdl.SDL_INIT_EVERYTHING)

    def tearDown(self):
        sdl.quit_subsystem(sdl.SDL_INIT_EVERYTHING)
        sdl.quit()

    def test_SDL_WindowEvent(self):
        event = events.SDL_WindowEvent()
        self.assertIsInstance(event, events.SDL_WindowEvent)

    def test_SDL_KeyboardEvent(self):
        event = events.SDL_KeyboardEvent()
        self.assertIsInstance(event, events.SDL_KeyboardEvent)

    def test_SDL_TextEditingEvent(self):
        event = events.SDL_TextEditingEvent()
        self.assertIsInstance(event, events.SDL_TextEditingEvent)

    def test_SDL_TextInputEvent(self):
        event = events.SDL_TextInputEvent()
        self.assertIsInstance(event, events.SDL_TextInputEvent)

    def test_SDL_MouseMotionEvent(self):
        event = events.SDL_MouseMotionEvent()
        self.assertIsInstance(event, events.SDL_MouseMotionEvent)

    def test_SDL_MouseButtonEvent(self):
        event = events.SDL_MouseButtonEvent()
        self.assertIsInstance(event, events.SDL_MouseButtonEvent)

    def test_SDL_MouseWheelEvent(self):
        event = events.SDL_MouseWheelEvent()
        self.assertIsInstance(event, events.SDL_MouseWheelEvent)

    def test_SDL_JoyAxisEvent(self):
        event = events.SDL_JoyAxisEvent()
        self.assertIsInstance(event, events.SDL_JoyAxisEvent)

    def test_SDL_JoyBallEvent(self):
        event = events.SDL_JoyBallEvent()
        self.assertIsInstance(event, events.SDL_JoyBallEvent)

    def test_SDL_JoyHatEvent(self):
        event = events.SDL_JoyHatEvent()
        self.assertIsInstance(event, events.SDL_JoyHatEvent)

    def test_SDL_JoyButtonEvent(self):
        event = events.SDL_JoyButtonEvent()
        self.assertIsInstance(event, events.SDL_JoyButtonEvent)

    def test_SDL_TouchFingerEvent(self):
        event = events.SDL_TouchFingerEvent()
        self.assertIsInstance(event, events.SDL_TouchFingerEvent)

    def test_SDL_TouchButtonEvent(self):
        event = events.SDL_TouchButtonEvent()
        self.assertIsInstance(event, events.SDL_TouchButtonEvent)

    def test_SDL_MultiGestureEvent(self):
        event = events.SDL_MultiGestureEvent()
        self.assertIsInstance(event, events.SDL_MultiGestureEvent)

    def test_SDL_DollarGestureEvent(self):
        event = events.SDL_DollarGestureEvent()
        self.assertIsInstance(event, events.SDL_DollarGestureEvent)

    def test_SDL_DropEvent(self):
        event = events.SDL_DropEvent()
        self.assertIsInstance(event, events.SDL_DropEvent)

    def test_SDL_QuitEvent(self):
        event = events.SDL_QuitEvent()
        self.assertIsInstance(event, events.SDL_QuitEvent)

    def test_SDL_UserEvent(self):
        event = events.SDL_UserEvent()
        self.assertIsInstance(event, events.SDL_UserEvent)

    def test_SDL_SysWMEvent(self):
        event = events.SDL_SysWMEvent()
        self.assertIsInstance(event, events.SDL_SysWMEvent)

    def test_SDL_Event(self):
        event = events.SDL_Event()
        self.assertIsInstance(event, events.SDL_Event)

    @unittest.skipIf(sys.platform == "cli",
                     "IronPython's ctypes can't handle Union types correctly")
    def test_add_del_event_watch(self):
        eventwatch = []

        def watch(data, event):
            eventwatch.append((event.contents, data,))
            return 0
        efilter = events.SDL_EventFilter(watch)
        udata = pypycapsule("Something random")
        events.add_event_watch(efilter, udata)
        ev = events.SDL_Event()
        ev.type = events.SDL_USEREVENT
        ev.user = events.SDL_UserEvent()
        events.push_event(ev)
        self.assertEqual(len(eventwatch), 1)
        self.assertEqual(eventwatch[0][1], udata)

        events.del_event_watch(efilter, udata)
        ev = events.SDL_Event()
        events.push_event(ev)
        self.assertEqual(len(eventwatch), 1)
        self.assertEqual(eventwatch[0][1], udata)

    @unittest.skipIf(sys.platform == "cli",
                     "IronPython's ctypes can't handle Union types correctly")
    def test_event_state(self):
        pass
        #state = events.event_state(events.SDL_USEREVENT, events.SDL_QUERY)
        #self.assertEqual(state, events.SDL_ENABLE)
        #state = events.event_state(events.SDL_USEREVENT, events.SDL_IGNORE)
        #self.assertEqual(state, events.SDL_ENABLE)
        #state = events.event_state(events.SDL_USEREVENT, events.SDL_QUERY)
        #self.assertEqual(state, events.SDL_IGNORE)
        #state = events.event_state(events.SDL_USEREVENT, events.SDL_ENABLE)
        #self.assertEqual(state, events.SDL_IGNORE)
        #state = events.event_state(events.SDL_USEREVENT, events.SDL_QUERY)
        #self.assertEqual(state, events.SDL_ENABLE)
        
        #self.assertRaises(TypeError, events.event_state, None, None)
        
        #ev = events.SDL_Event()
        #ev.type = events.SDL_USEREVENT
        #ev.user = events.SDL_UserEvent()
        #events.push_event(ev)


    @unittest.skip("not implemented")
    def test_get_event_state(self):
        pass

    @unittest.skip("not implemented")
    def test_filter_events(self):
        pass

    @unittest.skip("not implemented")
    def test_flush_event(self):
        pass

    @unittest.skip("not implemented")
    def test_flush_events(self):
        pass

    @unittest.skip("not implemented")
    def test_get_event_filter(self):
        pass

    @unittest.skip("not implemented")
    def test_set_event_filter(self):
        pass

    @unittest.skip("not implemented")
    def test_has_event(self):
        pass

    @unittest.skip("not implemented")
    def test_has_events(self):
        pass

    @unittest.skip("not implemented")
    def test_peep_events(self):
        pass

    @unittest.skip("not implemented")
    def test_poll_event(self):
        pass

    @unittest.skip("not implemented")
    def test_pump_events(self):
        pass

    @unittest.skip("not implemented")
    def test_push_event(self):
        pass

    @unittest.skip("not implemented")
    def test_register_events(self):
        pass

    @unittest.skip("not implemented")
    def test_wait_event(self):
        pass

    @unittest.skip("not implemented")
    def test_wait_event_timeout(self):
        pass

    @unittest.skip("not implemented")
    def test_quit_requested(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
