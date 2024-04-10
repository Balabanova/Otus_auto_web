import pytest
from locators import Navigation, MainPage, CatalogPage
from service import find_element, find_elements
from HeaderElement import HeaderElement


def check_cur_char(cur_char, element):
    for p in element:
        assert cur_char in p.text, f"There is no {cur_char} in {p.text}"


@pytest.mark.parametrize("currency", ["EUR", "GBR", "USD"])
def test_change_currency(driver, base_url, currency):
    """
    Тест проеряет изменение валюты у товаров
    на главной странице и в каталоге при изменении валюты в верхнем навигационном меню
    """
    # Переходим на главную страницу
    element = HeaderElement(driver, base_url)

    element.change_currency(currency)

    # Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара
    prod_row_price = find_elements(browser, MainPage.LOCATOR_PRODUCT_ROW_PRICE)
    check_cur_char(cur_char, prod_row_price)

    # Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара без налога
    prod_row_tax = find_elements(browser, MainPage.LOCATOR_PRODUCT_ROW_PRICE)
    check_cur_char(cur_char, prod_row_tax)

    # Переходим в каталог
    browser.get(f"{base_url}/laptop-notebook")

    # Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара
    prod_price = find_elements(browser, CatalogPage.LOCATOR_PRODUCT_PRICE)
    check_cur_char(cur_char, prod_price)

    # Проходимся по всем продуктам, проверяя наличие условного знака валюты в цене товара без налога
    prod_tax = find_elements(browser, CatalogPage.LOCATOR_PRODUCT_TAX)
    check_cur_char(cur_char,prod_tax)