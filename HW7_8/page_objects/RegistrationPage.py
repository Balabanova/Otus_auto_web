from HW7_8.page_objects.BaseApp import BasePage
from HW7_8.locators import RegisterPage as RP
import allure


class RegistrationPage(BasePage):

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)
        self.url = self.base_url + "/index.php?route=account/register"

    def go_to_registration_page(self):
        return self.driver.get(self.url)

    def fill_personal_details(self, firstname, lastname, email, telephone):
        with allure.step("Заполнение персональных данных"):
            self.input_f_name(firstname)
            self.input_l_name(lastname)
            self.input_email(email)
            self.input_telephone(telephone)

    def input_f_name(self, f_name):
        self.input_text(RP.LOCATOR_FIRSTNAME_INPUT, f_name)

    def input_l_name(self, l_name):
        self.input_text(RP.LOCATOR_LASTNAME_INPUT, l_name)

    def input_email(self, email):
        self.input_text(RP.LOCATOR_EMAIL_INPUT, email)

    def input_telephone(self, tel):
        self.input_text(RP.LOCATOR_TELEPHONE_INPUT, tel)

    def fill_passwords(self, password):
        self.input_password(password)
        self.input_confirm(password)

    def input_password(self, passwd):
        self.input_text(RP.LOCATOR_PASSWORD_INPUT, passwd)

    def input_confirm(self, c_passwd):
        self.input_text(RP.LOCATOR_CONFIRM_INPUT, c_passwd)

    def fill_agreement(self):
        self.click_on_element(RP.LOCATOR_AGREE_CHECKBOX)

    def confirm(self):
        self.click_on_element(RP.LOCATOR_CONTINUE_BUTTON)

