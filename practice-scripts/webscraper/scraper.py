# this will be a basic web scraper project

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#URL you are looking to scrape
URL = "url-goes-here"
DRIVER_PATH = '/usr/local/bin'

# Scarapping logic

driver = webdriver.Chrome()
driver.get(URL)

# tempcurrentPrice = driver.find_element(By.CLASS_NAME, "last-change").text
#element = "location and finding logic here"


driver.quit()