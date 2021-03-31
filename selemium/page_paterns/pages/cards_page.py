from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selemium.page_paterns.pages.base.page_base import PageBase


class CardsPage(PageBase):
    """
    goto available carts from CardPageMap
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardPageMap(driver)

    def goto(self):
        self.header_nav.goto_cart_page()
        return self

    def get_card_by_name(self, name: str) -> WebElement:  # if Ice Spirit -> Ice+Spirit
        if " " in name:
            name = name.replace(" ", "+")
        return self.map.card(name)


class CardPageMap:
    """
    represent all carts that available
    """

    def __init__(self, driver):
        self._driver = driver

    @property
    def ice_spirit_card(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")

    def card(self, card_name) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, f"[href*='{card_name}']")
