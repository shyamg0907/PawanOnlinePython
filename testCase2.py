import unittest
from selenium import webdriver
class searchEnineTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
        self.driver.get("https://pms.mrccsolutions.com/login.php")
        print("Title of test_Goole is", self.driver.title)
        self.driver.close()

    def test_Bing(self):
        self.driver=webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
        self.driver.get("https://bing.com")
       
        print("Title of Bing Test",self.driver.title)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

