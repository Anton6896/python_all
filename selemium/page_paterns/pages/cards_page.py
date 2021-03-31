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

    def goto_all(self):
        self.map.all_cards()
        return self  # chaining option

    def get_card_by_name(self, name: str) -> WebElement:
        """
        Ice Spirit -> Ice+Spirit
        look for the specific card in page
        """
        if " " in name:
            name = name.replace(" ", "+")
        return self.map.card(name)


class CardPageMap(PageBase):
    """
    represent all carts that available
    """

    def __init__(self, driver):
        super().__init__(driver)
        self._driver = driver

    # find specific card by name
    def card(self, card_name) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, f"[href*='{card_name}']")

    def all_cards(self):
        self.header_nav.goto_cart_page()
