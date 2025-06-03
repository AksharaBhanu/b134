import time

from selenium.webdriver import Edge
#to open browser -- we should create object of browser class--> Edge Browser

driver=Edge() #open edge browser
driver.get('http://www.google.com') #send url and get page
driver.close()