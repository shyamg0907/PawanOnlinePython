from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

driver =webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
#links = driver.find_elements_by_tag_name("a")
links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links are: ",len(links))
for link in links:
    print("Links Titles are : ",link.text)
    if link.text == "Powered by":
        break
#print(atagname.)

driver.quit()