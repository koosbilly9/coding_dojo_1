import unittest
from mock import Mock

import sys

from myEgg.some_km_send import send_to_km_partner

send_to_km_partner = Mock(return_value="Okay")


class test_some_km_send(unittest.TestCase):
    # def setUp(self):
    #     sys.path.append("C:\\PycharmProjects\\coding_dojo_1\\learn_mock_km")

    def test_send_to_km_partner(self):
        self.assertEqual(send_to_km_partner(), "Okay", "Test send km ")