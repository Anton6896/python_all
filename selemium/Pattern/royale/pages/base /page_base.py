"""
the common functionality for all pages (like an Navbar , footer etc.)
all pages will inherit the page base (functional)
"""
from selemium.Pattern.royale.pages.header_nav import HeaderNav


class PageBase:
    def __init__(self, driver):
        self.header_nav = HeaderNav(driver)
