import unittest

from .. ..dir1.dir1_sub1.dir1_sub1_subsub1 import dir1_sub1_subsub1


class testdir1(unittest.TestCase):

    def test_hello(self):
        dir1_sub1_subsub1.call()

        return True