from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from my_selemium.royale.page.base.in_common import PageBase


class CardsPageMap:
    def __init__(self, driver):
        self._driver = driver

    def ice_spirit_cart(self) -> WebElement:
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[href*='Ice+Spirit']")
            )
        )
        return element

    def cart(self, cart_name) -> WebElement:
        element = WebDriverWait(self._driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, f"[href*='{cart_name}']")
            )
        )
        return element


class CardPage(PageBase):
    """
    for more clear code i can put >>> self.header_nav.goto_cards_page()
    in the map as init function but debug will be more complicated
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.map = CardsPageMap(driver)

    def goto_ice_spirit_cart(self):
        self.header_nav.goto_cards_page()
        self.map.ice_spirit_cart().click()

    def goto_cart_name(self, name: str):
        if ' ' in name:
            name = name.replace(' ', '+')

        self.header_nav.goto_cards_page()
        self.map.cart(name)

    def goto_all(self):
        self.header_nav.goto_cards_page()
