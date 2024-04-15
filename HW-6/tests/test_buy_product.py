from service import find_elements
from locators import MainPage, CartPage
import random


def test_add_to_basket(browser, base_url):
    """
    Тест выбирает для добавления в корзину рандомный товар с главной страницы
    У 2х товаров кнопка добавления в карзину пересылает на карточку товара, но не добавляет в карзину,
    поэтому временами тест падает
    """
    browser.get(base_url)

    # Находим все продукты на главной странице, выбираем рандомный, запоминаем его название и добавляем в корзину
    products = find_elements(browser, MainPage.LOCATOR_PRODUCT_ROW_CART_BUTTON)
    random_el = random.randint(0, len(products)-1)
    name_el = find_elements(browser, MainPage.LOCATOR_PRODUCT_ROW_NAME)[random_el].text
    products[random_el].click()

    # Переходим на страницу корзины
    browser.get(f"{base_url}/index.php?route=checkout/cart")

    # Находим все добавленные в карзину продукты
    products_in_cart = find_elements(browser, CartPage.LOCATOR_PRODUCTS_NAMES)

    # Записываем все названия товаров в список
    names_cart_list = []
    for p in products_in_cart:
        names_cart_list.append(p.text)

    # Проверяем наличие в списке товаров из корзины тот, который мы добавляли в карзину выше
    assert name_el in names_cart_list
