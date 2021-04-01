"""
will hold the page functionality that all pages have in common like footer , navbar etc.
this one os concentrate the all common functional
"""

from my_selemium.royale.page.header_nav import HeaderNav


class PageBase:
    def __init__(self, driver):
        self.header_nav = HeaderNav(driver)
