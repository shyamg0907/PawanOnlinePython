import unittest
class paymentTest(unittest.TestCase):

    def test_paymentindollar(self):
        print("This payment in dollar test")
        self.assertTrue(True)

    def test_paymentinruppes(self):
        print("THis is payemnt in Ruppes")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
