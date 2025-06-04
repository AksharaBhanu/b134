import time

from selenium.webdriver import Chrome
driver=Chrome()
time.sleep(1)
driver.get('http://www.google.com')
time.sleep(1)
defaul_size=driver.get_window_size()
print(defaul_size)
driver.set_window_size(400,500)
time.sleep(2)
defualt_location=driver.get_window_position()
print(defualt_location)
driver.set_window_position(400,100)
time.sleep(2)