#import syntax
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


#importing webdriver
driver = webdriver.Firefox()
#i used firefox driver and yahoo browser as they doesn't need to enter the captcha compared to google chrome
driver.get("https://www.duckduckgo.com/")

#yahoo browser
elem = driver.find_element(By.XPATH, '//*[@id="searchbox_input"]')
time.sleep(3)

#yahoo search bar
elem.send_keys("Flipkart")
time.sleep(3)
elem.send_keys(Keys.ENTER)
time.sleep(3)
elem = driver.find_element(By.XPATH, '/html/body/div[2]/div[6]/div[4]/div/div/div/div[2]/section[1]/ol/li[1]/article/div[2]/div/div/a/div/p/span').click()
time.sleep(3)

#flipkart search bar
elem = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
elem.send_keys("Mobiles")
time.sleep(3)
elem.send_keys(Keys.ENTER)
time.sleep(2)

#scrolling the web page
driver.execute_script("window.scrollTo(0,1500)")
time.sleep(3)

#clicking element
clickable_elements = driver.find_elements(By.CLASS_NAME, '//a | //button')
if clickable_elements:
    random_elements = random.choice(clickable_elements)
    random_elements.click()
    time.sleep(4)
else:
    print("NO CLICKABLE FOUND")
        
