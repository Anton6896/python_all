from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selemium.page_paterns.pages.base.page_base import PageBase


class CardDetailMap:
    def __init__(self, driver):
        self._driver = driver

    @property
    def card_name(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='cardName']")

    @property
    def card_type(self) -> WebElement:
        # https://www.youtube.com/watch?v=UJ2B49YbW04&list=PLelD030IW7swU6n75wOIeCC9hqKipub_w&index=3&ab_channel=QAatthePoint
        # 25.50
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']")

    @property
    def cart_rarity(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']")


class CardDetail(PageBase):
    def __init__(self, driver):
        super(CardDetail, self).__init__(driver)
        self.map = CardDetailMap(driver)
