# python_v2/my_library/tests/test_string_utils.py
import unittest
from python_v2.my_library.string_utils import reverse_string, capitalize_string, is_palindrome

class TestStringUtils(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")
        self.assertEqual(reverse_string(""), "")

    def test_capitalize_string(self):
        self.assertEqual(capitalize_string("hello"), "Hello")
        self.assertEqual(capitalize_string("world"), "World")
        self.assertEqual(capitalize_string(""), "")
        self.assertEqual(capitalize_string("HELLO"), "Hello")

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("Python"))