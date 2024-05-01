from BaseApp import BasePage
from locators import AdminProductPage as APP
from locators import AdminDashboardPage as ADP
from locators import get_unique_locator_xpath
import time
import allure


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

    def find_product_by_name(self, name, timeout=10):
        with allure.step(f"Находим товар по имени {name}"):
            locator = f"//*/div/table/tbody//*[contains(text(),'{name}')]"
            return self.find_elements(get_unique_locator_xpath(locator), timeout)

    def delete_product_by_name(self, name):
        with allure.step(f"Удаляем товар по имени {name}"):
            locator = f"//*/div/table/tbody/tr//*[contains(text(),'{name}')] /preceding-sibling::* /input"
            self.click_on_element(get_unique_locator_xpath(locator))
            self.click_on_element(APP.LOCATOR_DELETE_BUTTON)

