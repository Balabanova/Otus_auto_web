from BaseApp import BasePage
from AdminLoginPage import AdminLoginPage
from HW7_8.locators import AdminProductPage as APP
from HW7_8.locators import AdminNewProductPage as ANPP
import random
import string
import allure


def _random_string():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


class AdminNewProductsPage(BasePage):
    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def go_to_new_product_creator(self):
        self.find_element(APP.LOCATOR_ADD_PRODUCT).click()

    def create_new_product(self):
        with allure.step("Создание нового товара"):
            name = _random_string()
            self.input_name(name)

            tag = _random_string()
            self.input_tag(tag)

            self.click_on_element(ANPP.LOCATOR_DATA_BUTTON)
            model = _random_string()
            self.input_model(model)

            self.click_on_element(ANPP.LOCATOR_SAVE_BUTTON)

            return [name, tag, model]

    def input_name(self, name):
        self.input_text(ANPP.LOCATOR_GENERAL_NAME, name)

    def input_tag(self, tag):
        self.input_text(ANPP.LOCATOR_GENERAL_TAG_TITLE, tag)

    def input_model(self, model):
        self.input_text(ANPP.LOCATOR_DATA_MODEL, model)