import pytest
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
    def test_login(self, setup):
        page, _ = setup

        # Входим в админку
        page.log_in("user", "bitnami")

        # Проверяем, что тайтл страницы изменился
        assert page.wait_title("Dashboard")

    def test_logout(self, setup):
        page, header = setup

        # Выходим из админки
        header.log_out()

        # Проверяем, что тайтл страницы изменился
        assert page.wait_title("Administration")
