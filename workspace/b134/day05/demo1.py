import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
time.sleep(1)
driver.get("https://aksharatraining.com/sample1.html")
time.sleep(1)
driver.find_element(By.XPATH,"/html/body/a").click()
time.sleep(2)