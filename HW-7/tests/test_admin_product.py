import pytest
from AdminLoginPage import AdminLoginPage
from AdminProductsPage import AdminProductsPage as APP
from AdminNewProductPage import AdminNewProductsPage as ANPP
from selenium.common.exceptions import TimeoutException
import time


@pytest.fixture(scope="class")
def setup(driver, base_url):
    page = AdminLoginPage(driver, base_url)
    prod_page = APP(driver, base_url)
    new_prod_page = ANPP(driver, base_url)
    page.go_to_admin_login_page()
    page.log_in("user", "bitnami")
    try:
        page.wait_title("Dashboard")
    except:
        pytest.skip("Can't login to admin")
    yield prod_page, new_prod_page


pytest.global_variable_1 = ""


class TestAdminProduct:

    def test_add_product(self, setup):
        prod_page, new_prod_page = setup
        prod_page.go_to_products_page()
        # Переходим на страницу создания нового продукта
        new_prod_page.go_to_new_product_creator()

        # Заполняем обязательные поля и сохраняем
        new_pod = new_prod_page.create_new_product()
        pytest.global_variable_1 = new_pod[0]

        # Проверяем, что вернулись на страницу продуктов
        assert prod_page.wait_title("Products")

        # Проверяем, что продукт создался
        prod = prod_page.find_product_by_name(pytest.global_variable_1)
        assert len(prod) == 1

    def test_delete_product(self, setup):
        prod_page, new_prod_page = setup

        prod_page.delete_product_by_name(pytest.global_variable_1)
        prod_page.accept_browser()
        with pytest.raises(TimeoutException):
            prod_page.find_product_by_name(pytest.global_variable_1, 3)








