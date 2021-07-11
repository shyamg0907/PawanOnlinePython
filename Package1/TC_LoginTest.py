import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyEmail(self):
        print("This is login bye email test")
        self.assertTrue(True)

    def test_loginbyFacebook(self):
        print("This is login by facebook")
        self.assertTrue(True)

    def test_loginbyTwiter(self):
        print("This is login by Twitter")
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
