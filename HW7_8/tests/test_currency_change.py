import pytest
from HW7_8.page_objects.HeaderElement import HeaderElement
from HW7_8.page_objects.CatalogPage import CatalogDesktopsPage
from HW7_8.page_objects.MainPage import MainPage
import allure


def check_cur_char(cur_char, element):
    with allure.step("Проверка наличия символа валюты в цене"):
        for p in element:
            assert cur_char in p.text, f"There is no {cur_char} in {p.text}"


@allure.title("Проверка изменения валюты")
@allure.description(
    """
    Тест проеряет изменение валюты у товаров
    на главной странице и в каталоге при изменении валюты в верхнем навигационном меню
    """
)
@pytest.mark.parametrize("currency", ["EUR", "GBR", "USD"])
def test_change_currency(driver, base_url, currency, logger):
    element = HeaderElement(driver, base_url)
    catalog = CatalogDesktopsPage(driver, base_url)
    main = MainPage(driver, base_url)

    element.go_to_home_page()

    cur_char = element.change_currency(currency)
    logger.info(f"Символ валюты {currency}: {cur_char}")

    with allure.step("Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара"):
        prod_prices = main.get_products_prices()
        check_cur_char(cur_char, prod_prices)

    with allure.step("Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара без налога"):
        prod_taxes = main.get_products_taxes()
        check_cur_char(cur_char, prod_taxes)

    catalog.go_to_desktops_page()

    with allure.step("Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара"):
        prod_prices = catalog.get_products_prices()
        check_cur_char(cur_char, prod_prices)

    with allure.step("Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара без налога"):
        prod_taxes = catalog.get_products_taxes()
        check_cur_char(cur_char, prod_taxes)
