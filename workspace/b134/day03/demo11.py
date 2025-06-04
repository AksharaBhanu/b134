import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#using the locator:LINK_TEXT
driver=Chrome()
driver.get('https://aksharatraining.com/sample1.html')

driver.find_element(By.LINK_TEXT,"Google").click()

time.sleep(2)