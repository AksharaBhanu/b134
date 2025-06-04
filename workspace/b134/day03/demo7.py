import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#using the locator: tag name
driver=Chrome()
driver.get('https://aksharatraining.com/sample1.html')

driver.find_element(By.TAG_NAME,"a").click()

time.sleep(2)