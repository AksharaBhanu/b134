import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

#using the locator: PARTIAL_LINK_TEXT
driver=Chrome()
driver.get('https://aksharatraining.com/sample1.html')

driver.find_element(By.PARTIAL_LINK_TEXT,"oo").click()

time.sleep(2)