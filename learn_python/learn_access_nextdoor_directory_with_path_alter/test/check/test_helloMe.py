import unittest

# get system path need package sys
import sys
import os


# change system path - to project root - then call Hello() from 2 directories
class helloMeTestCase(unittest.TestCase):

    def setUp(self):
        os.chdir("../..")
        cwd = os.getcwd()
        #sys.path.append("C:\\PycharmProjects\\coding_dojo_1\\learn_access_nextdoor_directory_with_path_alter")
        sys.path.append(cwd)


    def test_helloMe_from_nextdoor(self):
        from nextdoor.child1.child2.helloMe import hello

        hello_text=str(hello())

        self.assertRegex(hello_text,r'nextdoor\\child1',"Message: Hello")

    def test_helloMe_from_parent(self):
        from parent.child1.child2.helloMe import hello

        hello_text=str(hello())

        self.assertRegex(hello_text,r'parent\\child1',"Message: Hello")

