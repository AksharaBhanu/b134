import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get('https://aksharatraining.com/sample3.html')
time.sleep(1)
element=driver.find_element(By.TAG_NAME,"input")
element.send_keys("****")
time.sleep(2)