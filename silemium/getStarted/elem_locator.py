import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver_path = os.path.join(str(Path(__file__).parent.parent), 'chromedriver_win32', 'chromedriver.exe')
driver = webdriver.Chrome(driver_path)

'''
locate an element on the page
https://www.seleniumeasy.com/test/bootstrap-modal-demo.html
'''


def locator():
    """
    start page : https://www.seleniumeasy.com/test/basic-checkbox-demo.html
    go to : https://www.seleniumeasy.com/test/basic-first-form-demo.html  (thru the nav bar menu)
    select : elem_id = 'user-message'
    past text: 'testing is cool !!'
    press button: form with button for javaScript (have no id)
    see data in : id="display"
    :return: result as text in terminal
    """

    # driver.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
    driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')
    print(f"driver at page : {driver.title}")

    # get to page from vie the navBar
    driver.find_element_by_link_text('Input Forms').click()
    driver.find_element_by_link_text('Simple Form Demo').click()

    search_field = driver.find_element_by_id('user-message')
    search_field.send_keys('testing is cool !!')
    # search_field.send_keys(Keys.RETURN)  # not working on this site
    driver.find_element_by_xpath('//*[@id="get-input"]/button').click()
    output_field = driver.find_element_by_id('display')
    print(output_field.text)
    # time.sleep(3)
    driver.quit()


def locator2():
    # navigate to target page
    driver.get('https://www.techwithtim.net/')
    search_field = driver.find_element_by_name('s')
    search_field.send_keys('tet')
    search_field.send_keys(Keys.RETURN)

    """
    create an list with all posts ... 
    struct -> DOM :: main->article->(data i need (title, link, text))
    
    (by default selenium waite at driver.get() for the main page to load data)
    wait till element be located on the page WebDriverWait
    """

    delay = 3  # sec defaults

    try:
        # wait to the object in dom with id=main
        elem_main = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'main')))

        # from this object grub all tags articles
        article_list = elem_main.find_elements_by_tag_name('article')

        for article in article_list:
            # for ech article. print data

            link_obj = article.find_elements_by_class_name('entry-title')[0]
            title = link_obj.find_element_by_tag_name('a').get_attribute("text")
            url = link_obj.find_element_by_tag_name('a').get_attribute('href')
            text = article.find_elements_by_class_name("entry-summary")[0].text
            print(f"{title} -- {url} \n{text}\n")

    except TimeoutException:
        print('Loading took too much time!')

    finally:
        # close driver
        driver.quit()


if __name__ == '__main__':
    # locator()
    locator2()
