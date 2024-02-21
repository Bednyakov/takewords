import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
        self.base_url = '/'

    def test_index(self):
        response = self.app.get(f'{self.base_url}')
        self.assertEqual(response.status_code, 200)

    def test_translate(self):
        response = self.app.get(f'{self.base_url}translate/')
        self.assertEqual(response.status_code, 200)