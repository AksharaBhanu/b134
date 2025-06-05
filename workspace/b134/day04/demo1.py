import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
time.sleep(1)
driver.get("https://aksharatraining.com/sample1.html")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"a[id='a1']").click()
time.sleep(1)
driver.back()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'a[id="a1"]').click()
time.sleep(1)