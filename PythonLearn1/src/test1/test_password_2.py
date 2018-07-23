import unittest
import json

class PasswordWithJsonTeseCase(unittest.TestCase):
    data_file_path = './user_data.json'

    def setUp(self):
        print('set up')
        self.test_data = json.loads(open(self.data_file_path).read())

    def test_week_password(self):
        for data in self.test_data:
            passwd = data['password']

            self.assertTrue(len(passwd) >= 6)

            msg = "user %s has a weak password" %(data['name'])
            self.assertTrue(passwd != 'password', msg)
            self.assertTrue(passwd != 'password123', msg)

    def test_dummy(self):
        pass

if __name__ == '__main__':
    unittest.main()