import pytest
from AdminLoginPage import AdminLoginPage
from AdminProductsPage import AdminProductsPage as APP
import time


@pytest.fixture(scope="class")
def setup(driver, base_url):
    page = AdminLoginPage(driver, base_url)
    prod_page = APP(driver, base_url)
    page.go_to_admin_login_page()
    page.log_in("user", "bitnami")
    try:
        page.wait_title("Dashboard")
    except:
        pytest.skip("Can't login to admin")
    yield prod_page


class TestAdminProduct:
    def test_add_product(self, setup):
        prod_page = setup
        prod_page.go_to_products_page()

        # Переходим на страницу создания нового продукта
        prod_page.go_to_new_product_creator()

        # Заполняем обязательные поля и сохраняем
        new_pod = prod_page.create_new_product()

        assert




