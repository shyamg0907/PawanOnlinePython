from selenium import webdriver
driver=webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")

driver.get("https://pms.mrccsolutions.com/login.php")
#driver.save_screenshot("E:\\pythonProject\\pawanOnlineSeleniumPython\\screenshots\\ss1.png")

driver.get_screenshot_as_file("E:\\pythonProject\\pawanOnlineSeleniumPython\\screenshots\\ss2.jpeg")

driver.close()
