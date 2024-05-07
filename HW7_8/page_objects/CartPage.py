from BaseApp import BasePage
from HW7_8.locators import CartPage as CP
import pytest


class CartPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = self.base_url + "/index.php?route=checkout/cart"

    def go_to_cart_page(self):
        return self.driver.get(self.url)

    def get_products_in_cart(self):
        return self.find_elements(CP.LOCATOR_PRODUCTS_NAMES)

    def get_products_in_cart_list(self):
        products = self.get_products_in_cart()
        names_cart_list = []
        for p in products:
            names_cart_list.append(p.text)
        return names_cart_list