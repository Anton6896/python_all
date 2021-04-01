"""
represent navbar links
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class HeaderNavMap:
    """
    map of the links that exists at the web (that you gonna use)
    """

    def __init__(self, driver):
        self._driver = driver

    def cards_link(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[href='/cards']")

    def guides_link(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[href='/guides']")


class HeaderNav:
    """
    navigate thru the map
    """

    def __init__(self, driver):
        self.map = HeaderNavMap(driver)

    def goto_cards_page(self):
        self.map.cards_link().click()
        return self

    def goto_guides_page(self):
        self.map.guides_link().click()
        return self
