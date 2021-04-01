import os
from selenium import webdriver

# trying to work in windows
from my_selemium.royale.page.cards_page import CardPage

driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver.exe')
driver = webdriver.Chrome(driver_path)
driver.get('https://statsroyale.com/')  # main page


def test_image_check():
    """
    ice spirit image check
    """
    carts_page = CardPage(driver).goto_all()
    ice_spirit = carts_page.goto_cart_name('Ice Spirit')
    assert ice_spirit.is_displayed()
