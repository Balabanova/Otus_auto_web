from BaseApp import BasePage
from locators import MainPage as MP


class MainPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def get_products_prices(self):
        return self.find_elements(MP.LOCATOR_PRODUCT_ROW_PRICE)

    def get_products_taxes(self):
        return self.find_elements(MP.LOCATOR_PRODUCT_ROW_TAX)