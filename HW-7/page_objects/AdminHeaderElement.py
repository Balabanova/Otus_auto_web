from BaseApp import BasePage
from locators import AdminDashboardPage as AP


class HeaderElement(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = self.base_url + "/admin"

    def log_out(self):
        self.find_element(AP.LOCATOR_LOGOUT_BUTTON).click()

