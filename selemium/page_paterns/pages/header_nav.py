"""
navigation thru the navBar on page
"""
from selenium.webdriver.common.by import By


class HeaderNavMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def cards_link(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[href='/cards']")

    @property
    def guides_link(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[href*='/guides']")


class HeaderNav:
    def __init__(self, driver):
        self.map = HeaderNavMap(driver)

    def goto_cart_page(self):
        self.map.cards_link.click()

    def goto_guide_page(self):
        self.map.guides_link.click()
