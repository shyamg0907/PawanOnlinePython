import XLUtils
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
# txtUserName
# txtPassword
# BtnSubmitLogin

driver.get("https://pms.mrccsolutions.com/login.php")
driver.maximize_window()
# driver.implicitly_wait(2)


path = "E:\\pythonProject\\pawanOnlineSeleniumPython\\xlData.xlsx"
rows = XLUtils.getRowCount(path,"Sheet1")
print(rows)
for r in range(2,rows+1):
    username = XLUtils.readData(path,"Sheet1",rows, 1)
    password = XLUtils.readData(path,"Sheet1",rows, 2)
    print(path)
    print(username)
    print(password)

    driver.find_element_by_name("txtUserName").clear()
    driver.find_element_by_name("txtUserName").send_keys('sagupta')
    driver.find_element_by_name("txtPassword").clear()
    driver.find_element_by_name("txtPassword").send_keys('pass@word1')
    driver.find_element_by_name("BtnSubmitLogin").click()

    if driver.title == "MRCC PMS":
        print("Test is passed")
        XLUtils.writeData(path,"Sheet1",r, 3,"Test Passed")
    else:
        print("Test Failed")
        XLUtils.writeData(path,"Sheet1",r,3,"Test Failed")

    driver.find_element_by_link_text("Logout").click()
