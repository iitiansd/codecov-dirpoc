import unittest
from services.dummy_service_ignore_me.app import IgnoreMe

class TestIgnoreMe(unittest.TestCase):
    def test_nothing(self):
        assert IgnoreMe().do_nothing() == "I should be excluded from coverage."