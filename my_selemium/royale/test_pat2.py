import os
from selenium import webdriver

# trying to work in windows
driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver.exe')
driver = webdriver.Chrome(driver_path)
driver.get('https://statsroyale.com/')  # main page


