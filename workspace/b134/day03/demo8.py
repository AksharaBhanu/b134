import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#using the locator: id
driver=Chrome()
driver.get('https://aksharatraining.com/sample1.html')

driver.find_element(By.ID,"a1").click()

time.sleep(2)