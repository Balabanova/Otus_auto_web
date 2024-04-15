from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_element(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(EC.presence_of_element_located(locator),
                                                 message=f"Can't find element by locator {locator}")


def find_elements(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(EC.presence_of_all_elements_located(locator),
                                                 message=f"Can't find elements by locator {locator}")


def wait_title(browser, title, timeout=10):
    return WebDriverWait(browser, timeout).until((EC.title_is(title)),
                                                 message=f"There is title={browser.title}, but expected title={title} ")
