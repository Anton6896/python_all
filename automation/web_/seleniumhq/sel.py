from typing import final
from selenium import webdriver
import os
import time
import pathlib
import logging
import platform

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    # will put log ner the executed file
    filename="log_file.txt"
)


def web_sel():
    # ? for more from selenium check the doc , great libriry

    # for for the platform for put right path tfor drivr
    if platform.system() == "Darwin":
        print("using mac platform")

        # get driver for mac
        logging.debug('get path to the driver')
        chromedriver: final = os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'chromedriver_mac')

        driver: final = webdriver.Chrome(chromedriver)

        logging.debug('using driver')
        driver.get(
            'https://sites.google.com/a/chromium.org/chromedriver/help/clicking-issues')
        link = driver.find_element_by_xpath(
            '//*[@id="COMP_7221429159399122"]/div/ul/li[2]/div/a')
        link.click()

        logging.debug('exit driver')
        time.sleep(5)  # Let the user actually see something!

        # # exit
        driver.quit()
    
    elif platform.system() == "Linux":
        # get driver for mac
        logging.debug('get path to the driver')
        chromedriver: final = os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'chromedriver_linux')

        driver: final = webdriver.Chrome(chromedriver)

        logging.debug('using driver')
        driver.get(
            'https://sites.google.com/a/chromium.org/chromedriver/help/clicking-issues')
        link = driver.find_element_by_xpath(
            '//*[@id="COMP_7221429159399122"]/div/ul/li[2]/div/a')
        link.click()

        logging.debug('exit driver')
        time.sleep(5)  # Let the user actually see something!

        # # exit
        driver.quit()

    else:
        #  in my case using windows platform
        logging.debug('get path to the driver')
        chromedriver: final = os.path.join(pathlib.Path(
            __file__).parent.absolute(), 'chromedriver.exe')

        driver: final = webdriver.Chrome(chromedriver)

        logging.debug('using driver')
        driver.get(
            'https://sites.google.com/a/chromium.org/chromedriver/help/clicking-issues')
        link = driver.find_element_by_xpath(
            '//*[@id="COMP_7221429159399122"]/div/ul/li[2]/div/a')
        link.click()

        # # do some
        # search_box = driver.find_element_by_name('q')
        # search_box.send_keys('ChromeDriver')
        # search_box.submit()
        logging.debug('exit driver')
        time.sleep(5)  # Let the user actually see something!

        # # exit
        driver.quit()


if __name__ == "__main__":
    web_sel()
