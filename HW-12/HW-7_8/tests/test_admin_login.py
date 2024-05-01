import pytest
import allure
from AdminLoginPage import AdminLoginPage
from AdminHeaderElement import HeaderElement


@pytest.fixture(scope="class")
def setup(driver, base_url):
    page = AdminLoginPage(driver, base_url)
    header = HeaderElement(driver, base_url)
    page.go_to_admin_login_page()
    yield page, header


class TestAdmin:
    """
    Набор тестов проверяет вход и выход в/из админки
    """
    @allure.title("Проверка входа в админку")
    def test_login(self, setup, driver):
        page, _ = setup

        # Входим в админку
        page.log_in("user", "bitnami")

        with allure.step("Проверяем, что тайтл страницы изменился"):
            assert page.wait_title("Dashboard")

    @allure.title("Проверка выхода из админки")
    def test_logout(self, setup):
        page, header = setup

        # Выходим из админки
        header.log_out()

        with allure.step("Проверяем, что тайтл страницы изменился"):
            assert page.wait_title("Administration")
