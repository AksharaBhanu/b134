import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver=Chrome()
driver.get("https://pos.aksharatraining.in/pos/public/login")
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#input-username").send_keys("admin")
driver.find_element(By.CSS_SELECTOR,"#input-password").send_keys("pointofsale")
driver.find_element(By.CSS_SELECTOR,"[name='login-button']").click()
time.sleep(3)
driver.quit()