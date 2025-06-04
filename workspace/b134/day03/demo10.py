import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#using the locator: class name
driver=Chrome()
driver.get('https://aksharatraining.com/sample1.html')

driver.find_element(By.CLASS_NAME,"c1").click()

time.sleep(2)