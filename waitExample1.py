from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://www.mrccgroup.com/")

if driver.title == "MRCC":
    print("Title is corerct !!! ",driver.title)
driver.close()
#driver.find_elements(By.