from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\geckodriver.exe")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://newtours.demoaut.com/")
print(driver.title)
driver.maximize_window()
driver.quit()