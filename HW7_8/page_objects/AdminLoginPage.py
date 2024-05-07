from HW7_8.page_objects.BaseApp import BasePage
from HW7_8.locators import AdminLoginPage as AP
import allure


class AdminLoginPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = self.base_url + "/admin"

    def go_to_admin_login_page(self):
        return self.driver.get(self.url)
    
    def log_in(self, login, password):
        with allure.step("Логин в админку"):
            self.input_login(login)
            self.input_password(password)
            self.confirm()

    def input_login(self, login):
        self.input_text(AP.LOCATOR_USERNAME_INPUT, login)

    def input_password(self, password):
        self.input_text(AP.LOCATOR_PASSWORD_INPUT, password)
        
    def confirm(self):
        self.click_on_element(AP.LOCATOR_SUBMIT_BUTTON)
