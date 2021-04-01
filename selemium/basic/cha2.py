"""
Page map pattern
"""

import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# define a driver for chrome etc.
# driver_path = os.path.join(str(Path(__file__).parent.parent), 'driver_linux', 'chromedriver')
driver_path = os.path.join(str(Path(__file__).parent.parent), 'chromedriver_win32', 'chromedriver.exe')
driver = webdriver.Chrome(driver_path)


def test_check_data_in_card():
    driver.get('https://statsroyale.com/')
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()
    driver.find_element(By.CSS_SELECTOR, "[href*='Ice+Spirit']").click()

    card_name = driver.find_element(By.CSS_SELECTOR, "[class*='cardName']").text
    card_type, card_arena = str(driver.find_element(By.CSS_SELECTOR, "[class*='card__rarity']").text).split(", ")
    card_rarity = driver.find_element(By.CSS_SELECTOR, "[class*='rarityCaption']").text.split('\n')[1]

    assert card_name == "Ice Spirit"
    assert card_type == "Troop"
    assert card_arena == "Arena 8"
    assert card_rarity == "Common"

    driver.close()
