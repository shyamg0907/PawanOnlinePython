from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")

driver.get("http://www.amazon.in")
driver.maximize_window()
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

cookie={'name':'shyam','value':'12344567'}
driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_cookie('shyam')
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)

driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)
driver.close()