from my_selenium_testing.cards_site.pages.nav_menu import HeaderNav


class PageBase:
    """
    provide accesses to navbar thu all pages
    """

    def __init__(self, driver):
        self.header_nav = HeaderNav(driver)
