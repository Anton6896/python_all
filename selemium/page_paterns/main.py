import os
from selenium import webdriver

from selemium.page_paterns.pages.cards_page import CardsPage

driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
driver = webdriver.Chrome(driver_path)


def test_ice_spirit_is_displayed():
    driver.get('https://statsroyale.com/')
    cards_page = CardsPage(driver).goto()
    ice_spirit = cards_page.get_card_by_name("Ice Spirit")
    assert ice_spirit.is_displayed()

    driver.close()
