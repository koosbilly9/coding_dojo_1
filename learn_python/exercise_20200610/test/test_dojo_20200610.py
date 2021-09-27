import json
import unittest

import requests
from sqlalchemy.orm import Session

from coding_dojo_1.learn_python.exercise_20200610.main.web_server import get_db_session


class DB_Handeling_TestCase(unittest.TestCase):
    def test_get_session_for_sqlite_inMem(self):
        self.assertIsInstance(get_db_session(), Session,"get session back for in memory db engine")
        pass

# This is the class we want to test
class ApiEndPoints:
    def fetch_json(self, url):
        response = requests.get(url)
        return response.json()

# Our test case class
class ApiEndPointsClassTestCase(unittest.TestCase):

     def test_fetch_root(self):
        # Assert requests.get calls
        mgc = ApiEndPoints()
        url = f"http://127.0.0.1:50012/"
        json_data = mgc.fetch_json(url)
        self.assertEqual(json_data, {'response1': 'Hello World'})

     # @unittest.skip("wip")
     def test_get_first_user_in_mem(self):
         mgc = ApiEndPoints()
         name="Mike"
         url = f"http://127.0.0.1:50012/inMem/get_user/{name}"
         json_data = mgc.fetch_json(url)
         return_test_str = json.dumps({'user_name': name})
         self.assertEqual(json.dumps(json_data), json.dumps({"user_name": name}))


if __name__ == '__main__':
    unittest.main()