import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#using the locator: name
driver=Chrome()
driver.get('https://aksharatraining.com/sample1.html')

driver.find_element(By.NAME,"n1").click()

time.sleep(2)