import pytest
from locators import AdminLoginPage, AdminDashboardPage
from service import find_element, wait_title


@pytest.fixture(scope="class")
def setup(browser, base_url):
    url = f"{base_url}/admin"
    browser.get(url)
    yield browser


class TestAdmin:
    """
    Набор тестов проверяет вход и выход в/из админки
    """
    def test_login(self, setup):
        browser = setup

        # Находим поле ввода логина и вводим user
        username_input = find_element(browser, AdminLoginPage.LOCATOR_USERNAME_INPUT)
        username_input.send_keys("user")
        # Находим поле ввода пароля и вводим bitnami
        password_input = find_element(browser, AdminLoginPage.LOCATOR_PASSWORD_INPUT)
        password_input.send_keys("bitnami")

        # Находим кнопку входа и нажимаем
        submit_button = find_element(browser, AdminLoginPage.LOCATOR_SUBMIT_BUTTON)
        submit_button.click()

        # Проверяем, что тайтл страницы изменился
        assert wait_title(browser, "Dashboard")

    def test_logout(self, setup):
        browser = setup

        # Находим кнопку выхода из админки и нажимаем
        logout_button = find_element(browser, AdminDashboardPage.LOCATOR_LOGOUT_BUTTON)
        logout_button.click()

        # Проверяем, что тайтл страницы изменился
        assert wait_title(browser, "Administration")
