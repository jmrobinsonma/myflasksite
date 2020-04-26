import app
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_myscrapbook(self):
        response = self.app.get('/myscrapbook')
        self.assertEqual(response.status_code, 200)

    def test_freestuff_app_book(self):
        response = self.app.get('/freestuff_app_book')
        self.assertEqual(response.status_code, 200)

    def test_dicebook(self):
        response = self.app.get('/dicebook')
        self.assertEqual(response.status_code, 200)

    def test_apibook(self):
        response = self.app.get('/apibook')
        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()
