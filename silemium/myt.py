from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import os
import time


def mac_tes():
    # mac chrome driver -> /usr/local/bin
    path_mac = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(path_mac)
    driver.get('https://www.google.com/')

    print(driver.title)

    #  get search result from google
    search = driver.find_element_by_name('q')  # <- search box in google page
    search.send_keys("test")
    search.send_keys(Keys.RETURN)
    time.sleep(4)  # <- time to over to search result

    # look for your data
    # main = search.find_element_by_class_name("LC20lb DKV0Md")
    main = search.find_element_by_class_name("tF2Cxc")

    # wright data to file
    # with open(str(os.getcwd()) + "/test.txt", "a+") as f:
    #     f.write(driver.page_source)
    # print(driver.page_source)

    driver.quit()


def linux_tes():
    """
    look for some blog entries 

    xpath :: https://www.guru99.com/xpath-selenium.html
    with xpath is more comfartable to make an search in page 

    """

    path_lin = "/usr/local/bin/chromedriver"
    driver = webdriver.Chrome(path_lin)
    driver.get('https://thejoyfuljourneyer1.blog/')

    print(f"driver title : \n{driver.title}\n")

    # to get data from web page , give to selenium to wait for the page be loaded !!
    # try:
    #     elements = WebDriverWait(driver, 20).until(
    #         EC.presence_of_element_located(
    #             (By.XPATH, "/html/body/div[1]/div[2]/div/div/div/div[1]/div")
    #         )
    #     )

    #     # with xpath of element will return the all data !
    #     # links = elements.find_elements_by_xpath('//*[@id="post-898"]/div/div[2]/h2/a')

    #     entires = elements.find_elements_by_class_name('entry-title')

    #     for i in entires:
    #         print(f"blog entire ::  {i.text}")
    #         print(f"\t===>  : {i.get_attribute('xpath')}")

    # finally:
    #     # if cant find till 10 sec of any other problent just quite
    #     driver.quit()

    """
    <h2 class="card-title entry-title">
    <a href="https://thejoyfuljourneyer1.blog/reflection-or-real/" title="Reflection? Or real?" rel="bookmark">Reflection? Or real?</a>
    </h2>
    """
    # web_element = driver.find_element_by_xpath("//*[text()='Reflection? Or real?']")
    web_element = driver.find_element_by_xpath(
        "//*[contains(text(),'Reflection')]")
    # Xpath=//tagname[@attribute='value']  <--
    print(web_element.text)
    print(web_element.get_attribute('href'))

    driver.quit()


if __name__ == '__main__':
    linux_tes()
