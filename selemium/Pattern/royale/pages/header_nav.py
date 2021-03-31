"""
the nav bar as HeaderNavMap
pattern : Page map Pattern
"""
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


class HeaderNav:
    def __init__(self, driver):
        self.map = HeaderNavMap(driver)

    def goto_cart_page(self):
        self.map.card_link.click()

    def goto_guide_page(self):
        self.map.guides_link.click()


class HeaderNavMap:
    def __init__(self, driver):
        # self.driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
        # self.driver = webdriver.Chrome(self.driver_path)
        self._driver = driver

    @property
    def card_link(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[href='/cards']")

    @property
    def guides_link(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[href*='/guides']")


if __name__ == '__main__':
    pass
