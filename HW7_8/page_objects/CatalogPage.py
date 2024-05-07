from HW7_8.page_objects.BaseApp import BasePage
from HW7_8.locators import CatalogPage as CP
import pytest


class CatalogDesktopsPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = self.base_url + "/desktops"

    def go_to_desktops_page(self):
        return self.driver.get(self.url)

    def get_products_prices(self):
        return self.find_elements(CP.LOCATOR_PRODUCT_PRICE)

    def get_products_taxes(self):
        return self.find_elements(CP.LOCATOR_PRODUCT_TAX)
