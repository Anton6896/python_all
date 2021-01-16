from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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


if __name__ == '__main__':
    mac_tes()
