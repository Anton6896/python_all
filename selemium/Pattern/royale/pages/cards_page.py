from selenium.webdriver.common.by import By
from selemium.Pattern.royale.pages.base import PageBase

class CardPage(PageBase):
    """
    goto available carts from CardPageMap
    """

    def __init__(self, driver):
        self.map = CardPageMap(driver)

    def goto_ice_spirit_card(self):
        self.map.ice_spirit_card.click()


class CardPageMap:
    """
    represent all carts that available
    """

    def __init__(self, driver):
        self._driver = driver

    @property
    def ice_spirit_card(self):
        return self._driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']")
