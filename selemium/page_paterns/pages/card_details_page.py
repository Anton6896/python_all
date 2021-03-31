from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class CardDetailMap:
    def __init__(self, driver):
        self._driver = driver

    def card_name(self) -> WebElement:
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='cardName']")

    def card_type(self) -> WebElement:
        # https://www.youtube.com/watch?v=UJ2B49YbW04&list=PLelD030IW7swU6n75wOIeCC9hqKipub_w&index=3&ab_channel=QAatthePoint
        # 25.50
        return self._driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']")
