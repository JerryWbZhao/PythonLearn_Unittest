import unittest

class PasswordTeseCase(unittest.TestCase):

    def setUp(self):
        print('set up')
        self.test_data = [
            dict(name='jack', password='Iloverose'),
            dict(name='rose', password='Ilovejack'),
            dict(name='tom', password='password123'),
            dict(name='jenny', password='password'),
        ]

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