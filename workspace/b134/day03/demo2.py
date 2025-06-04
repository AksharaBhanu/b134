import time

from selenium.webdriver import Chrome
driver=Chrome()
time.sleep(1)
driver.get('http://www.google.com')
time.sleep(1)
driver.maximize_window()
time.sleep(1)
driver.fullscreen_window()
time.sleep(1)
driver.maximize_window()
time.sleep(1)
driver.minimize_window()
time.sleep(1)
driver.quit()