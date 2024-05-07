from HW7_8.page_objects.BaseApp import BasePage
from HW7_8.locators import AdminDashboardPage as AP
import allure


class HeaderElement(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = self.base_url + "/admin"

    def log_out(self):
        with allure.step("Выход из админки"):
            self.find_element(AP.LOCATOR_LOGOUT_BUTTON).click()

