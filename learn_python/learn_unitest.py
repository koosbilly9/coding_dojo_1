import unittest

class helloMeTestCase(unittest.TestCase):
    def test_helloMe_from_parent(self):
        self.assertRegex('koos',r'koos',"Compare string")

        self.assertRegex('koos was n dapper muis', r'koos', "Compare string in longer string ")

        self.assertRegex('http://www.google.com?koos was n dapper muis',
                         r'koos|http://', "Compare string in longer string ")