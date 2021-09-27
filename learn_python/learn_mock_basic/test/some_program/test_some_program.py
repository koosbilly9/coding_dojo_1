import unittest
from mock import Mock

from some_program.some_program import get_time


class test_some_program(unittest.TestCase):
    def test_get_time(self):
        self.assertEqual(get_time(),"00:00:00","Test Time " )

    def test_mock_get_time(self):
        get_time = Mock(return_value="XX:01:00")
        self.assertEqual(get_time(),"XX:01:00","Test Time " )

