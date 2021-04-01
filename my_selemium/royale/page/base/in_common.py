"""
will hold the page functionality that all pages have in common like footer , navbar etc.
"""



class PageBase:
    def __init__(self, driver):
        self.header_nav = HeaderNav(driver)
