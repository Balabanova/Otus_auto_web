from BaseApp import BasePage
from HW7_8.locators import MainPage as MP
import random
import allure


class MainPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def get_products_prices(self):
        return self.find_elements(MP.LOCATOR_PRODUCT_ROW_PRICE)

    def get_products_taxes(self):
        return self.find_elements(MP.LOCATOR_PRODUCT_ROW_TAX)

    def get_all_products(self):
        return self.find_elements(MP.LOCATOR_PRODUCT_ROW_CART_BUTTON)

    def get_random_product(self):
        products = self.get_all_products()
        random_el = random.randint(0, len(products)-1)
        name_el = self.find_elements(MP.LOCATOR_PRODUCT_ROW_NAME)[random_el].text
        return random_el, name_el

    def add_to_cart(self, elem):
        with allure.step("Добавление товара в корзину"):
            products = self.get_all_products()
            products[elem].click()
