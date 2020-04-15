import myflasksite 
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        myflasksite.app.testing = True
        self.app = myflasksite.app.test_client()

    def test_home(self):
        response = self.app.get('/')
        # Make your assertions
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()