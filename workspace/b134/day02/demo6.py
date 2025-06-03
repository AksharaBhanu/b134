
from selenium.webdriver import Chrome

driver=Chrome() #open browser
driver.get('http://www.fb.com') #enter url
print(driver.title) #get the title
print(driver.current_url)
print(driver.page_source)
driver.close() #close the browser