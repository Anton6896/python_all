import os
from selenium import webdriver

from selemium.page_paterns.pages.card_details_page import CardDetail
from selemium.page_paterns.pages.cards_page import CardsPage

driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
driver = webdriver.Chrome(driver_path)
driver.get('https://statsroyale.com/')


def test_ice_spirit_is_displayed():
    cards_page = CardsPage(driver).goto_all()  # on page with all cards
    ice_spirit = cards_page.get_card_by_name("Ice Spirit")  # look for card
    assert ice_spirit.is_displayed()

    driver.close()


# def test_ice_spirit_details():
#     cards_page = CardsPage(driver).goto_all()  # on page with all cards
#     cards_page.get_card_by_name("Ice Spirit").click()
#
#     details_page = CardDetail(driver)
#     card_name = details_page.map.card_name.text
#     card_type, card_arena = details_page.map.card_type.text.split(", ")
#     card_rarity = details_page.map.cart_rarity.text.split('\n')[1]
#
#     assert card_name == "Ice Spirit"
#     assert card_type == "Troop"
#     assert card_arena == "Arena 8"
#     assert card_rarity == "Common"
#
#     driver.close()


# if __name__ == '__main__':
#     test_ice_spirit_is_displayed()
#     test_ice_spirit_details()
