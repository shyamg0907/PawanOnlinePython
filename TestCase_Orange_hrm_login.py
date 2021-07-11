from selenium import webdriver
import unittest
import HtmlTestRunner

class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.assertEqual("OrangeHRM",self.driver.title,"OOPS, Title is not matched.")
        print(self.driver.title)

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element_by_name("txtUsername").send_keys("admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("Test Completed....!!!")


if __name__ == '__main__':
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="E:\\pythonProject\\pawanOnlineSeleniumPython\\Reports\\"))
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="..\\Reports"))
