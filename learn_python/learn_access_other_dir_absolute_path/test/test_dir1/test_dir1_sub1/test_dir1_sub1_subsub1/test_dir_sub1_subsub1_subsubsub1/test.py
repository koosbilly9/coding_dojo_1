import unittest
import os
import sys


from .. .. ..dir1.dir1_sub1.dir1_sub1_subsub1 import dir1_sub1_subsub1


class testdir1(unittest.TestCase):

    def setUp(self):
        print(f"{ os.path.dirname(sys.modules['__main__'].__file__ )}")

    def test_hello(self):
        dir1_sub1_subsub1.call()

        return True