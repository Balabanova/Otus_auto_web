import pytest
from locators import Navigation, MainPage, CatalogPage
from service import find_element, find_elements


def check_cur_char(cur_char, element):
    for p in element:
        assert cur_char in p.text, f"There is no {cur_char} in {p.text}"


@pytest.mark.parametrize("locator", [Navigation.LOCATOR_CURRENCY_EUR_BUTTON,
                                     Navigation.LOCATOR_CURRENCY_GBP_BUTTON,
                                     Navigation.LOCATOR_CURRENCY_USD_BUTTON])
def test_change_currency(browser, base_url, locator):
    """
    Тест проеряет изменение валюты у товаров
    на главной странице и в каталоге при изменении валюты в верхнем навигационном меню
    """
    # Переходим на главную страницу
    browser.get(base_url)

    # Находим элемент, переключающий валюту, переключаем валюту и запоминаем условный знак
    find_element(browser, Navigation.LOCATOR_CURRENCY_BUTTON).click()
    cur = find_element(browser, locator)
    cur_char = (cur.text)[0]
    cur.click()

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
