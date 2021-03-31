from selenium.webdriver.common.by import By
from selemium.page_paterns.pages.base.page_base import PageBase


class CardPageMap:
    """
    represent all carts that available
    """

    def __init__(self, driver):
        self._driver = driver

    @property
    def ice_spirit_card(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")


class CardsPage(PageBase):
    """
    goto available carts from CardPageMap
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardPageMap(driver)

    def goto(self):
        self.header_nav.goto_cart_page()

    def goto_ice_spirit_card(self):
        self.header_nav.goto_cart_page()
        self.map.ice_spirit_card.click()
