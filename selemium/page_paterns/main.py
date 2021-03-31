import os
from selenium import webdriver

from selemium.page_paterns.pages.cards_page import CardsPage

driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
driver = webdriver.Chrome(driver_path)
driver.get('https://statsroyale.com/')


def test_ice_spirit_is_displayed():
    cards_page = CardsPage(driver).goto_all()  # on page with all cards
    ice_spirit = cards_page.get_card_by_name("Ice Spirit")  # look for card
    assert ice_spirit.is_displayed()

    driver.close()


def test_ice_spirit_details():
    CardsPage(driver).goto_all().get_card_by_name("Ice Spirit").click()
