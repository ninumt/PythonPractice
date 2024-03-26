import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
'''driver=webdriver.Firefox()
driver=webdriver.Ie()
driver=webdriver.Safari()'''


driver.set_page_load_timeout(10)
driver.get("http://www.google.com")

searchbox=driver.find_element(By.ID,"APjFqb")

searchbox.send_keys("testing jobs in usa")
searchbox.send_keys(Keys.RETURN)
optionlist=searchbox.find_elements(By.CSS_SELECTOR, 'div[id="sBQTL"]')
print(len(optionlist))
for ele in optionlist:
    print(ele)
"""div[id='jZ2SBf'] div:nth-child(1)
//div[@id='sBQTL']//div[1]//span[1]"""
time.sleep(5)

driver.quit()
