from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver =webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
#driver.switch_to_alert().accept()
driver.switch_to_alert().dismiss()
