import sys
import unittest
from ctypes import ArgumentError
import pygame2.openal.al as al


class ALTest(unittest.TestCase):
    __tags__ = ["openal"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_get_error(self):
        self.assertIsInstance(al.get_error(), int)
        self.assertEqual(al.get_error(), al.AL_INVALID_OPERATION)

    def test_OpenALError(self):
        err = al.OpenALError()
        self.assertEqual(err.msg, "Invalid operation")
        err = al.OpenALError("Something's wrong")
        self.assertEqual(err.msg, "Something's wrong")

    def test_enable(self):
        self.assertRaises(ArgumentError, al.enable, "Test")
        self.assertRaises(al.OpenALError, al.enable, 0)

    def test_disable(self):
        self.assertRaises(ArgumentError, al.disable, "Test")
        self.assertRaises(al.OpenALError, al.disable, 0)

    def test_is_enabled(self):
        self.assertRaises(ArgumentError, al.is_enabled, "Test")
        self.assertRaises(al.OpenALError, al.is_enabled, 0)

    def test_get_string(self):
        self.assertRaises(ArgumentError, al.get_string, "Test")
        self.assertRaises(al.OpenALError, al.get_string, 0)

    def test_get_boolean_v(self):
        self.assertRaises(ArgumentError, al.get_boolean_v, "Test")
        self.assertRaises(al.OpenALError, al.get_boolean_v, 0)

    def test_get_integer_v(self):
        self.assertRaises(ArgumentError, al.get_integer_v, "Test")
        self.assertRaises(al.OpenALError, al.get_integer_v, 0)

    def test_get_float_v(self):
        self.assertRaises(ArgumentError, al.get_float_v, "Test")
        self.assertRaises(al.OpenALError, al.get_float_v, 0)

    def test_get_double_v(self):
        self.assertRaises(ArgumentError, al.get_double_v, "Test")
        self.assertRaises(al.OpenALError, al.get_double_v, 0)

    def test_get_boolean(self):
        self.assertRaises(ArgumentError, al.get_boolean, "Test")
        self.assertRaises(al.OpenALError, al.get_boolean, 0)

    def test_get_integer(self):
        self.assertRaises(ArgumentError, al.get_integer, "Test")
        self.assertRaises(al.OpenALError, al.get_integer, 0)

    def test_get_float(self):
        self.assertRaises(ArgumentError, al.get_float, "Test")
        self.assertRaises(al.OpenALError, al.get_float, 0)

    def test_get_double(self):
        self.assertRaises(ArgumentError, al.get_double, "Test")
        self.assertRaises(al.OpenALError, al.get_double, 0)

    def test_is_extension_present(self):
        self.assertRaises(TypeError, al.is_extension_present, 1234)
        self.assertRaises(al.OpenALError, al.is_extension_present, "Test")

    def test_get_proc_address(self):
        self.assertRaises(TypeError, al.get_proc_address, 1234)
        self.assertEqual(al.get_proc_address("Test"), None)

    def test_get_enum_value(self):
        self.assertRaises(TypeError, al.get_enum_value, 1234)
        self.assertEqual(al.get_enum_value("Test"), 0)
        self.assertEqual(al.get_enum_value("AL_FORMAT_MONO8"),
                         al.AL_FORMAT_MONO8)

    def test_listener_f(self):
        self.assertRaises(ArgumentError, al.listener_f, None, None)
        self.assertRaises(ArgumentError, al.listener_f, "Test", None)
        self.assertRaises(ArgumentError, al.listener_f, "Test", "Test")
        self.assertRaises(ArgumentError, al.listener_f, 1234, None)
        self.assertRaises(ArgumentError, al.listener_f, 1234, "Test")
        self.assertRaises(al.OpenALError, al.listener_f, 1234, 10)
        self.assertRaises(al.OpenALError, al.listener_f, 1234, 10.3333)

    def test_listener_3f(self):
        self.assertRaises(ArgumentError, al.listener_3f, None, None, None, None)
        self.assertRaises(ArgumentError, al.listener_3f, "Test", None, None,
                          None)
        self.assertRaises(ArgumentError, al.listener_3f, "Test", "Test", None,
                          None)
        self.assertRaises(ArgumentError, al.listener_3f, "Test", "Test", "Test",
                          None)
        self.assertRaises(ArgumentError, al.listener_3f, "Test", "Test", "Test",
                          "Test")
        self.assertRaises(ArgumentError, al.listener_3f, 1234, None, None, None)
        self.assertRaises(ArgumentError, al.listener_3f, 1234, "Test", None,
                          None)
        self.assertRaises(ArgumentError, al.listener_3f, 1234, "Test", "Test",
                          None)
        self.assertRaises(ArgumentError, al.listener_3f, 1234, "Test", "Test",
                          "Test")
        self.assertRaises(ArgumentError, al.listener_3f, 1234, 1, None, None)
        self.assertRaises(ArgumentError, al.listener_3f, 1234, 1, "Test", None)
        self.assertRaises(ArgumentError, al.listener_3f, 1234, 1, "Test",
                          "Test")
        self.assertRaises(ArgumentError, al.listener_3f, 1234, 1, 1, None)
        self.assertRaises(ArgumentError, al.listener_3f, 1234, 1, 1, "Test")
        self.assertRaises(al.OpenALError, al.listener_3f, 1234, 1, 1, 1)
        self.assertRaises(al.OpenALError, al.listener_3f, 1234, 1.4, -5, 22.0)

    @unittest.skip("not implemented")
    def test_listener_fv(self):
        pass

    @unittest.skip("not implemented")
    def test_listener_i(self):
        pass

    @unittest.skip("not implemented")
    def test_listener_3i(self):
        pass

    @unittest.skip("not implemented")
    def test_listener_iv(self):
        pass

    @unittest.skip("not implemented")
    def test_get_listener_f(self):
        pass

    @unittest.skip("not implemented")
    def test_get_listener_3f(self):
        pass

    @unittest.skip("not implemented")
    def test_get_listener_fv(self):
        pass

    @unittest.skip("not implemented")
    def test_get_listener_i(self):
        pass

    @unittest.skip("not implemented")
    def test_get_listener_3i(self):
        pass

    @unittest.skip("not implemented")
    def test_get_listener_iv(self):
        pass

    @unittest.skip("not implemented")
    def test_gen_sources(self):
        pass

    @unittest.skip("not implemented")
    def test_delete_sources(self):
        pass

    @unittest.skip("not implemented")
    def test_is_source(self):
        pass

    @unittest.skip("not implemented")
    def test_source_f(self):
        pass

    @unittest.skip("not implemented")
    def test_source_3f(self):
        pass

    @unittest.skip("not implemented")
    def test_source_fv(self):
        pass

    @unittest.skip("not implemented")
    def test_source_i(self):
        pass

    @unittest.skip("not implemented")
    def test_source_3i(self):
        pass

    @unittest.skip("not implemented")
    def test_source_iv(self):
        pass

    @unittest.skip("not implemented")
    def test_get_source_f(self):
        pass

    @unittest.skip("not implemented")
    def test_get_source_3f(self):
        pass

    @unittest.skip("not implemented")
    def test_get_source_fv(self):
        pass

    @unittest.skip("not implemented")
    def test_get_source_i(self):
        pass

    @unittest.skip("not implemented")
    def test_get_source_3i(self):
        pass

    @unittest.skip("not implemented")
    def test_get_source_iv(self):
        pass

    @unittest.skip("not implemented")
    def test_source_play_v(self):
        pass

    @unittest.skip("not implemented")
    def test_source_stop_v(self):
        pass

    @unittest.skip("not implemented")
    def test_source_rewind_v(self):
        pass

    @unittest.skip("not implemented")
    def test_source_pause_v(self):
        pass

    @unittest.skip("not implemented")
    def test_source_play(self):
        pass

    @unittest.skip("not implemented")
    def test_source_stop(self):
        pass

    @unittest.skip("not implemented")
    def test_source_rewind(self):
        pass

    @unittest.skip("not implemented")
    def test_source_pause(self):
        pass

    @unittest.skip("not implemented")
    def test_gen_buffers(self):
        pass

    @unittest.skip("not implemented")
    def test_delete_buffers(self):
        pass

    @unittest.skip("not implemented")
    def test_is_buffer(self):
        pass

    @unittest.skip("not implemented")
    def test_buffer_data(self):
        pass

    @unittest.skip("not implemented")
    def test_buffer_f(self):
        pass

    @unittest.skip("not implemented")
    def test_buffer_3f(self):
        pass

    @unittest.skip("not implemented")
    def test_buffer_fv(self):
        pass

    @unittest.skip("not implemented")
    def test_buffer_i(self):
        pass

    @unittest.skip("not implemented")
    def test_buffer_3i(self):
        pass

    @unittest.skip("not implemented")
    def test_buffer_iv(self):
        pass

    @unittest.skip("not implemented")
    def test_get_buffer_f(self):
        pass

    @unittest.skip("not implemented")
    def test_get_buffer_3f(self):
        pass

    @unittest.skip("not implemented")
    def test_get_buffer_fv(self):
        pass

    @unittest.skip("not implemented")
    def test_get_buffer_i(self):
        pass

    @unittest.skip("not implemented")
    def test_get_buffer_3i(self):
        pass

    @unittest.skip("not implemented")
    def test_get_buffer_iv(self):
        pass

    @unittest.skip("not implemented")
    def test_doppler_factor(self):
        pass

    @unittest.skip("not implemented")
    def test_doppler_velocity(self):
        pass

    @unittest.skip("not implemented")
    def test_speed_of_source(self):
        pass

    @unittest.skip("not implemented")
    def test_distance_model(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
