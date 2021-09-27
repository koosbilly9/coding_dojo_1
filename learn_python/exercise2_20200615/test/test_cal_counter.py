import unittest

import requests
from sqlalchemy.orm import session

from coding_dojo_1.learn_python.exercise2_20200615.main.calorie_counter import db_handeling


class test_db_handeling(unittest.TestCase):

    def test_connection_sqlite_in_mem(self):
        self.assertIsInstance(db_handeling.get_sqlite_inMem_session(), session.Session)

    def test_insert_food_egg(self):
        self.assertEqual('egg', db_handeling.insert_food('egg'))


class test_end_points(unittest.TestCase):
    url = f"http://127.0.0.1:50012/"

    def test_end_point_root(self):
        response = requests.get(self.url)
        self.assertEqual(str(response), '<Response [200]>')
        self.assertEqual(response.json(), {'response1': 'Hello World 2'})

    def test_end_point_help(self):
        response = requests.get(self.url + 'help')
        self.assertEqual(str(response), '<Response [200]>')
