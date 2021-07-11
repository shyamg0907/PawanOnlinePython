from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver =webdriver.Chrome(executable_path="E:\pythonProject\pawanOnlineSeleniumPython\drivers\chromedriver.exe")
driver.implicitly_wait(3)
driver.maximize_window()
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html")
radioSelect =driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(radioSelect)
#drp.select_by_visible_text('Morning')
#drp.select_by_index(2)
drp.select_by_value("Radio-2")
print(len(drp.options))
all_option =drp.options
for opt in all_option:
    print(opt.text)

#driver.close()