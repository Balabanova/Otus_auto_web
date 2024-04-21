from BaseApp import BasePage
from AdminLoginPage import AdminLoginPage
from locators import AdminProductPage as APP
from locators import AdminNewProductPage as ANPP
from locators import AdminDashboardPage as ADP
import random
import string
import time


def _random_string():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


class AdminProductsPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def go_to_products_page(self):
        self.click_on_element(ADP.LOCATOR_MENU_CATALOG_BUTTON)
        for i in range(5):
            try:
                self.click_on_element(ADP.LOCATOR_MENU_CATALOG_PRODUCTS)
                break
            except:
                time.sleep(0.5)

    def go_to_new_product_creator(self):
        self.find_element(APP.LOCATOR_ADD_PRODUCT).click()

    def create_new_product(self):
        name = _random_string()
        self.input_name(name)
        time.sleep(3)

        tag = _random_string()
        self.input_tag(tag)
        time.sleep(3)

        self.click_on_element(ANPP.LOCATOR_DATA_BUTTON)
        model = _random_string()
        self.input_model(model)
        time.sleep(3)

        self.click_on_element(ANPP.LOCATOR_SAVE_BUTTON)
        return [name, tag, model]

    def input_name(self, name):
        self.input_text(ANPP.LOCATOR_GENERAL_NAME, name)

    def input_tag(self, tag):
        self.input_text(ANPP.LOCATOR_GENERAL_TAG_TITLE, tag)

    def input_model(self, model):
        self.input_text(ANPP.LOCATOR_DATA_MODEL, model)

