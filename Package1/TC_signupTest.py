import unittest

class signupTest(unittest.TestCase):
    def test_signupbyEmail(self):
        print("This is signup bye email test")
        self.assertTrue(True)

    def test_signupbyFacebook(self):
        print("This is signup by facebook")
        self.assertTrue(True)

    def test_signupbyTwiter(self):
        print("This is signup by Twitter")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
