from service import find_element
import locators


class TestT:
    """
    Набор тестов проверяет наличие элементов на 5 страницах:
    главная страница, каталог, карточка товара, страница логина в админку, страница регистрации пользователя
    """
    def test_main_page(self, browser, base_url):
        browser.get(base_url)
        assert find_element(browser, locators.MainPage.LOCATOR_COMPANIES_CAROUSEL)
        assert find_element(browser, locators.MainPage.LOCATOR_FEATURED_PRODUCT_BUTTONS)
        assert find_element(browser, locators.MainPage.LOCATOR_FEATURED_PRODUCT_CAPTION)
        assert find_element(browser, locators.MainPage.LOCATOR_FEATURED_PRODUCT_IMAGE)
        assert find_element(browser, locators.MainPage.LOCATOR_SLIDE_SHOW)

    def test_catalog_page(self, browser, base_url):
        browser.get(f"{base_url}/tablet")
        assert find_element(browser, locators.CatalogPage.LOCATOR_PRODUCTS_LIST_GROUP)
        assert find_element(browser, locators.CatalogPage.LOCATOR_LIST_VIEW_BUTTON)
        assert find_element(browser, locators.CatalogPage.LOCATOR_INPUT_SORT_INPUT_LIST)
        assert find_element(browser, locators.CatalogPage.LOCATOR_INPUT_LIMIT_INPUT)
        assert find_element(browser, locators.CatalogPage.LOCATOR_GRID_VIEW_BUTTON)

    def test_product_page(self, browser, base_url):
        browser.get(f"{base_url}/desktops/mac/imac")
        assert find_element(browser, locators.ProductPage.LOCATOR_ADD_TO_CART_BUTTON)
        assert find_element(browser, locators.ProductPage.LOCATOR_ADD_TO_WISHLIST_BUTTON)
        assert find_element(browser, locators.ProductPage.LOCATOR_QUANTITY_TEXTBOX)
        assert find_element(browser, locators.ProductPage.LOCATOR_RATING_DIV)
        assert find_element(browser, locators.ProductPage.LOCATOR_WRITE_REVIEW_LINK)

    def test_admin_login_page(self, browser, base_url):
        browser.get(f"{base_url}/admin")
        assert find_element(browser, locators.AdminLoginPage.LOCATOR_HELP_BLOCK_HREF)
        assert find_element(browser, locators.AdminLoginPage.LOCATOR_SUBMIT_BUTTON)
        assert find_element(browser, locators.AdminLoginPage.LOCATOR_USERNAME_INPUT)
        assert find_element(browser, locators.AdminLoginPage.LOCATOR_PASSWORD_INPUT)
        assert find_element(browser, locators.AdminLoginPage.LOCATOR_FA_ICON)

    def test_register_page(self, browser, base_url):
        browser.get(f"{base_url}/index.php?route=account/register")
        assert find_element(browser, locators.RegisterPage.LOCATOR_CONTINUE_BUTTON)
        assert find_element(browser, locators.RegisterPage.LOCATOR_PRIVATE_POL_HREF)
        assert find_element(browser, locators.RegisterPage.LOCATOR_PASSWORD_INPUT)
        assert find_element(browser, locators.RegisterPage.LOCATOR_LOGIN_HREF)
        assert find_element(browser, locators.RegisterPage.LOCATOR_ACCOUNT_BLOCK)
