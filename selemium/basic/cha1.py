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


def test_image_in_place():
    driver.get('https://statsroyale.com/')
    #  go to card pages (this is a link on navbar)
    driver.find_element(By.CSS_SELECTOR, "[href='/cards']").click()

    try:
        delay = 5
        elem = WebDriverWait(driver, delay).until(
            EC.presence_of_element_located(
                # *= is an re contains
                (By.CSS_SELECTOR, "[href*='Ice+Spirit']")
            )
        )
        assert elem.is_displayed

    except TimeoutException:
        print('Loading took too much time!')
    finally:
        driver.close()


def test_selenium_1():
    """
    go to this site in navbar navigate to field , fill with word "puppies" , push button, check result
    """
    driver.get('https://www.seleniumeasy.com/test')
    driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul[1]/li[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="navbar-brand-centered"]/ul[1]/li[1]/ul/li[1]/a').click()
    driver.find_element(By.ID, 'user-message').send_keys('puppies')
    driver.find_element(By.XPATH, '//*[@id="get-input"]/button').click()
    mess = driver.find_element(By.ID, 'display').text
    assert mess == 'puppies'
    driver.close()


# def test_selenium_2():
#     driver.get('https://www.seleniumeasy.com/test')
#     driver.find_element(By.CSS_SELECTOR, "[href*='']").click()


def test_google_search():
    """
    open an browser , go to google pages , in search field look for puppies,
     push submit, close the window, return title
    :return: title of google search
    """
    try:
        driver.get('https://www.google.com/')
        delay = 3  # wait till google site is ready for search
        WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.NAME, 'q'))).send_keys('puppies')
        driver.find_element(By.NAME, 'btnK').submit()
        assert "puppies" in driver.title

    except TimeoutException:
        print('Loading took too much time!')

    finally:
        driver.close()


# if __name__ == '__main__':
#     """
#     https://www.tutorialspoint.com/pytest/pytest_run_tests_in_parallel.htm
#     pip install pytest-xdist
#     pytest -n 3  (-n -> workers)
#     running pytest in parallel  ( but it better run thru the terminal ) !!!
#     """
#
#     test_google_search()
#     test_image_in_place()
#     test_selenium_1()

