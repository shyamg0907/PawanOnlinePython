from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver =webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element(By.TAG_NAME)