from MainPage import MainPage as MP
from CartPage import CartPage as CP


def test_add_to_basket(driver, base_url):
    """
    Тест выбирает для добавления в корзину рандомный товар с главной страницы
    У 2х товаров кнопка добавления в карзину пересылает на карточку товара, но не добавляет в карзину,
    поэтому временами тест падает
    """
    main = MP(driver, base_url)
    cart = CP(driver, base_url)

    main.go_to_home_page()

    # Находим все продукты на главной странице, выбираем рандомный, запоминаем его название и добавляем в корзину
    product, prod_name = main.get_random_product()
    main.add_to_cart(product)

    # Переходим на страницу корзины
    cart.go_to_cart_page()

    # Получаем список имен продуктов в корзине
    names_cart_list = cart.get_products_in_cart_list()

    # Проверяем наличие в списке товаров из корзины тот, который мы добавляли в карзину выше
    assert prod_name in names_cart_list
