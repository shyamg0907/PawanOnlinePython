import unittest
class apptest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Open Application")
    @classmethod
    def tearDownClass(cls):
        print("close Application")


    def setUp(self):
        print("Login method")

    def tearDown(self):
        print("logout method")

    @unittest.SkipTest
    def test_search(self):
        print("Simple search")

    @unittest.skip("I skipped test case test_advacnceSearch")
    def test_advanceSearch(self):
        print("From Advance search")


    def test_prePaidCharge(self):
        print("Prepaid Charge")


    def test_postPaidCharge(self):
        print("Post Paid Charge")


if __name__ == '__main__':
    unittest.main()
