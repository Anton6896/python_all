'''
https://crossbrowsertesting.com/?utm_source=seleniumeasy&utm_medium=da&utm_campaign=sedemo

greate web fore teting the selenium driver :
https://www.seleniumeasy.com/test/bootstrap-modal-demo.html

'''

import os
from pathlib import Path
from selenium import webdriver
import time

driver_path = os.path.join(str(Path(__file__).parent.parent), 'chromedriver_win32', 'chromedriver.exe')
driver = webdriver.Chrome(driver_path)


def open_page():
    driver.get('https://www.seleniumeasy.com/test/bootstrap-modal-demo.html')
    print(driver.title)
    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    open_page()
