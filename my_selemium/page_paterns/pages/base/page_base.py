
from selemium_my.page_paterns.pages.header_nav import HeaderNav


class PageBase:
    """
    provide accesses to navbar thu all pages
    """
    def __init__(self, driver):
        self.header_nav = HeaderNav(driver)
