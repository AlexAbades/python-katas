from unittest import TestCase

from katas.digital_root.digital_root import (
    digital_root_module,
    digital_root_recursive,
    digital_root_while,
)


class TestDigitalRoot(TestCase):

    def test_test(self):
        self.assertTrue(True)

    def test_digital_root_recursive(self):
        self.assertEqual(digital_root_recursive(16), 7)
        self.assertEqual(digital_root_recursive(942), 6)
        self.assertEqual(digital_root_recursive(132189), 6)
        self.assertEqual(digital_root_recursive(493193), 2)

    def test_digital_root_while(self):
        self.assertEqual(digital_root_while(16), 7)
        self.assertEqual(digital_root_while(942), 6)
        self.assertEqual(digital_root_while(132189), 6)
        self.assertEqual(digital_root_while(493193), 2)

    def test_digital_root_module(self):
        self.assertEqual(digital_root_module(16), 7)
        self.assertEqual(digital_root_module(942), 6)
        self.assertEqual(digital_root_module(132189), 6)
        self.assertEqual(digital_root_module(493193), 2)

    def test_digital_root_module_negative(self):
        with self.assertRaises(ValueError) as context:
            digital_root_module(-1)
        self.assertEqual(str(context.exception), "Number should be positive")
