from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url

    def go_to_home_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator),
                                                         message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator),
                                                         message=f"Can't find elements by locator {locator}")

    def wait_title(self, title, timeout=10):
        return WebDriverWait(self.driver, timeout).until((EC.title_is(title)),
                                                         message=f"There is title={self.driver.title}, "
                                                                 f"but expected title={title} ")

    def input_text(self, locator, text):
        name_field = self.find_element(locator)
        name_field.send_keys(text)

    def click_on_element(self, locator):
        self.find_element(locator).click()


