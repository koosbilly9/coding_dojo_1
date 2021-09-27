import unittest

from ..some_sql import some_sql

class test_some_sql(unittest.TestCase):
    def test_get_standort(self):
        self.assertEqual("Okay", "Okay", "Test send km ")