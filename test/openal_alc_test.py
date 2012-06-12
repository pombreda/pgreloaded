import sys
import unittest
import pygame2.openal as openal
import pygame2.openal.alc as alc


class ALCTest(unittest.TestCase):
    __tags__ = ["openal"]

    def setUp(self):
        if sys.version.startswith("3.1"):
            self.assertIsInstance = \
                lambda x, t: self.assertTrue(isinstance(x, t))

    def tearDown(self):
        pass

    def test_ALCdevice(self):
        device = alc.open_device()
        self.assertIsInstance(device, alc.ALCdevice)
        alc.close_device(device)

    def test_ALCcontext(self):
        context = alc.ALCcontext()
        self.assertIsInstance(context, alc.ALCcontext)

    def test_get_error(self):
        device = alc.open_device()
        errval = alc.get_error(device)
        self.assertEqual(errval, alc.ALC_NO_ERROR)
        alc.close_device(device)

    @unittest.skip("not implemented")
    def test_capture_open_close_device(self):
        pass

    @unittest.skip("not implemented")
    def test_capture_samples(self):
        pass

    @unittest.skip("not implemented")
    def test_capture_start(self):
        pass

    @unittest.skip("not implemented")
    def test_capture_stop(self):
        pass

    def test_open_close_device(self):
        dev = alc.open_device("invalid device name :-)")
        self.assertIsNone(dev)
        self.assertRaises(TypeError, alc.close_device, dev)
        self.assertRaises(TypeError, alc.close_device, "Test")
        self.assertRaises(TypeError, alc.close_device, 12345)

        dev = alc.open_device(None)
        errval = alc.get_error(dev)
        self.assertEqual(errval, alc.ALC_NO_ERROR)

        # Closing a device with an attached context should not work according
        # to the OpenAL specification.
        ctx = alc.create_context(dev)

        # The test below ideally should work, however the SI
        # implementation as well as openal-soft close the device without
        # caring about any context attached to it.
        # All contexts are implicitly destroyed.
        #
        # self.assertFalse(alc.close_device(self._device))

        alc.destroy_context(ctx)
        self.assertTrue(alc.close_device(dev))

    def test_create_destroy_context(self):
        device = alc.open_device()
        
        self.assertRaises(TypeError, alc.create_context, None, None)
        self.assertRaises(TypeError, alc.create_context, 1234, None)
        self.assertRaises(TypeError, alc.create_context, "Test", None)
        self.assertRaises(TypeError, alc.create_context, device, 1234)
        self.assertRaises(TypeError, alc.create_context, device, "Test")

        ctx = alc.create_context(device)
        self.assertEqual(alc.get_error(device), alc.ALC_NO_ERROR)
        self.assertIsInstance(ctx, alc.ALCcontext)
        alc.destroy_context(ctx)
        self.assertEqual(alc.get_error(device), alc.ALC_NO_ERROR)

        ctx = alc.create_context(device, None)
        self.assertEqual(alc.get_error(device), alc.ALC_NO_ERROR)
        self.assertIsInstance(ctx, alc.ALCcontext)
        alc.destroy_context(ctx)
        self.assertEqual(alc.get_error(device), alc.ALC_NO_ERROR)

        ctx = alc.create_context(device, [alc.ALC_FREQUENCY, 11025])
        self.assertEqual(alc.get_error(device), alc.ALC_NO_ERROR)
        self.assertIsInstance(ctx, alc.ALCcontext)
        alc.destroy_context(ctx)
        self.assertEqual(alc.get_error(device), alc.ALC_NO_ERROR)
        
        self.assertTrue(alc.close_device(device))

    def test_get_context_device(self):
        self.assertRaises(TypeError, alc.get_context_device, None)
        self.assertRaises(TypeError, alc.get_context_device, "Test")
        self.assertRaises(TypeError, alc.get_context_device, None)

        device = alc.open_device()
        ctx = alc.create_context(device)
        dev = alc.get_context_device(ctx)
        self.assertIsInstance(dev, alc.ALCdevice)
        self.assertEqual(alc.get_error(device), alc.ALC_NO_ERROR)
        self.assertEqual(alc.get_error(dev), alc.ALC_NO_ERROR)
        alc.destroy_context(ctx)
        self.assertTrue(alc.close_device(device))

    def test_make_context_current_get_current_context(self):
        self.assertRaises(TypeError, alc.make_context_current, None)
        self.assertRaises(TypeError, alc.make_context_current, "Test")
        self.assertRaises(TypeError, alc.make_context_current, 1234)

        device = alc.open_device()
        self.assertIsNone(alc.get_current_context())

        ctx = alc.create_context(device)
        self.assertTrue(alc.make_context_current(ctx))
        cur = alc.get_current_context()
        self.assertIsInstance(cur, alc.ALCcontext)
        alc.destroy_context(ctx)
        self.assertFalse(alc.make_context_current(ctx))
        self.assertIsNone(alc.get_current_context())
        
        self.assertTrue(alc.close_device(device))

    def test_get_enum_value(self):
        device = alc.open_device()
        self.assertRaises(TypeError, alc.get_enum_value, None, None)
        self.assertRaises(TypeError, alc.get_enum_value, 12345, None)
        self.assertRaises(TypeError, alc.get_enum_value, "Test", None)
        self.assertRaises(TypeError, alc.get_enum_value, device, None)

        retval = alc.get_enum_value(device, "Test1234")
        self.assertEqual(retval, 0)
        # TODO: find some positive cases that are valid for 99% of the
        # default device.
        self.assertTrue(alc.close_device(device))

    @unittest.skip("not implemented")
    def test_get_integer_v(self):
        pass

    def test_get_string(self):
        extnames = (("ALC_ENUMERATION_EXT", alc.ALC_DEVICE_SPECIFIER),
                    ("ALC_ENUMERATE_ALL_EXT", alc.ALC_ALL_DEVICES_SPECIFIER)
                    )
        for ext, tval in extnames:
            if alc.is_extension_present(None, ext):
                stringvals = alc.get_string(None, tval)
                self.assertIsInstance(stringvals, str)

    @unittest.skip("not implemented")
    def test_get_proc_address(self):
        pass

    def test_is_extension_present(self):
        extnames = ("ALC_ENUMERATION_EXT",
                    "ALC_ENUMERATE_ALL_EXT"
                    )
        for ext in extnames:
            retval = alc.is_extension_present(None, ext)
            self.assertIsInstance(retval, bool)

        self.assertRaises(TypeError, alc.is_extension_present, 1234, "Test")
        self.assertRaises(TypeError, alc.is_extension_present, "Test", "Test")

    @unittest.skip("not implemented")
    def test_process_context(self):
        pass

    @unittest.skip("not implemented")
    def test_suspend_context(self):
        pass

if __name__ == '__main__':
    sys.exit(unittest.main())
