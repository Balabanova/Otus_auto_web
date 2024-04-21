import pytest
from HeaderElement import HeaderElement
from CatalogPage import CatalogDesktopsPage
from MainPage import MainPage


def check_cur_char(cur_char, element):
    for p in element:
        assert cur_char in p.text, f"There is no {cur_char} in {p.text}"


@pytest.mark.parametrize("currency", ["EUR", "GBR", "USD"])
def test_change_currency(driver, base_url, currency):
    """
    Тест проеряет изменение валюты у товаров
    на главной странице и в каталоге при изменении валюты в верхнем навигационном меню
    """
    element = HeaderElement(driver, base_url)
    catalog = CatalogDesktopsPage(driver, base_url)
    main = MainPage(driver, base_url)

    # Переходим на главную страницу
    element.go_to_home_page()

    # Меняем валюту
    cur_char = element.change_currency(currency)

    # Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара
    prod_prices = main.get_products_prices()
    check_cur_char(cur_char, prod_prices)

    # Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара без налога
    prod_taxes = main.get_products_taxes()
    check_cur_char(cur_char, prod_taxes)

    # Переходим в каталог
    catalog.go_to_desktops_page()

    # Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара
    prod_prices = catalog.get_products_prices()
    check_cur_char(cur_char, prod_prices)

    # Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара без налога
    prod_taxes = catalog.get_products_taxes()
    check_cur_char(cur_char, prod_taxes)
