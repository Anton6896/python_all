"""
navigate in the page and click elements with selenium 

https://www.youtube.com/watch?v=U6gbGk5WPws&ab_channel=TechWithTim

"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def nav_an_see():
    _path = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(_path)
    driver.get('https://blog.twitter.com/')
    print(f"driver title :: {driver.title}\n")

    """
    return human click element (url)
    this i found self its i think is an better way contains() <-
    """
    # elem_ = driver.find_element_by_xpath(
    #     "//*[contains(text(),'What to expect on Twitter on US')]")
    # link_ = elem_.get_attribute('href')

    # return an selenium element (callable for selenium ) ---------------
    # link2 = driver.find_element_by_link_text("What to expect on Twitter on US Inauguration Day 2021")
    # if link2:
    #     link2.click()

    _wait = WebDriverWait(driver, 10)
    element = _wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, 'What to expect on Twitter on US Inauguration Day 2021')
    ))
    element.click()

    button_ = _wait.until(EC.element_to_be_clickable(
        (By.CLASS_NAME, 'bl07-author-card')
    ))
    button_.click()  # <- ok

    time.sleep(3)  
    driver.back()
    driver.back()


    driver.quit()


if __name__ == "__main__":
    nav_an_see()
