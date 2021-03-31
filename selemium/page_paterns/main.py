import os
from selenium import webdriver

from selemium.page_paterns.pages.card_page import CardsPage

driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
driver = webdriver.Chrome(driver_path)


def test_ice_spirit_is_displayed():
    driver.get('https://statsroyale.com/')
    cards_page = CardsPage(driver)
    cards_page.goto()  # got ot page with all cards
    assert cards_page.map.ice_spirit_card.is_displayed()

    driver.close()
