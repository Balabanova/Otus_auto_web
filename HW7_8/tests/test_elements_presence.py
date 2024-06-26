from HW7_8.page_objects.MainPage import MainPage
from HW7_8.page_objects.CatalogPage import CatalogDesktopsPage
from HW7_8.page_objects.ProductPage import ProductPage
from HW7_8.page_objects.AdminLoginPage import AdminLoginPage
from HW7_8.page_objects.RegistrationPage import RegistrationPage
import HW7_8.locators as locators
import allure


class TestT:
    """
    Набор тестов проверяет наличие элементов на 5 страницах:
    главная страница, каталог, карточка товара, страница логина в админку, страница регистрации пользователя
    """
    @allure.title("Проверка наличия элементов на главной странице")
    def test_main_page(self, driver, base_url):
        main = MainPage(driver, base_url)
        main.go_to_home_page()
        assert main.find_element(locators.MainPage.LOCATOR_COMPANIES_CAROUSEL)
        assert main.find_element(locators.MainPage.LOCATOR_FEATURED_PRODUCT_BUTTONS)
        assert main.find_element(locators.MainPage.LOCATOR_FEATURED_PRODUCT_CAPTION)
        assert main.find_element(locators.MainPage.LOCATOR_FEATURED_PRODUCT_IMAGE)
        assert main.find_element(locators.MainPage.LOCATOR_SLIDE_SHOW)

    @allure.title("Проверка наличия элементов на странице каталога")
    def test_catalog_page(self, driver, base_url):
        catalog = CatalogDesktopsPage(driver, base_url)
        catalog.go_to_desktops_page()
        assert catalog.find_element(locators.CatalogPage.LOCATOR_PRODUCTS_LIST_GROUP)
        assert catalog.find_element(locators.CatalogPage.LOCATOR_LIST_VIEW_BUTTON)
        assert catalog.find_element(locators.CatalogPage.LOCATOR_INPUT_SORT_INPUT_LIST)
        assert catalog.find_element(locators.CatalogPage.LOCATOR_INPUT_LIMIT_INPUT)
        assert catalog.find_element(locators.CatalogPage.LOCATOR_GRID_VIEW_BUTTON)

    @allure.title("Проверка наличия элементов на странице товара")
    def test_product_page(self, driver, base_url):
        product = ProductPage(driver, base_url)
        product.go_to_product_page()
        assert product.find_element(locators.ProductPage.LOCATOR_ADD_TO_CART_BUTTON)
        assert product.find_element(locators.ProductPage.LOCATOR_ADD_TO_WISHLIST_BUTTON)
        assert product.find_element(locators.ProductPage.LOCATOR_QUANTITY_TEXTBOX)
        assert product.find_element(locators.ProductPage.LOCATOR_RATING_DIV)
        assert product.find_element(locators.ProductPage.LOCATOR_WRITE_REVIEW_LINK)

    @allure.title("Проверка наличия элементов на странице логина в админку")
    def test_admin_login_page(self, driver, base_url):
        admin_login = AdminLoginPage(driver, base_url)
        admin_login.go_to_admin_login_page()
        assert admin_login.find_element(locators.AdminLoginPage.LOCATOR_HELP_BLOCK_HREF)
        assert admin_login.find_element(locators.AdminLoginPage.LOCATOR_SUBMIT_BUTTON)
        assert admin_login.find_element(locators.AdminLoginPage.LOCATOR_USERNAME_INPUT)
        assert admin_login.find_element(locators.AdminLoginPage.LOCATOR_PASSWORD_INPUT)
        assert admin_login.find_element(locators.AdminLoginPage.LOCATOR_FA_ICON)

    @allure.title("Проверка наличия элементов на странице регистрации")
    def test_register_page(self, driver, base_url):
        registration = RegistrationPage(driver, base_url)
        registration.go_to_registration_page()
        assert registration.find_element(locators.RegisterPage.LOCATOR_CONTINUE_BUTTON)
        assert registration.find_element(locators.RegisterPage.LOCATOR_PRIVATE_POL_HREF)
        assert registration.find_element(locators.RegisterPage.LOCATOR_PASSWORD_INPUT)
        assert registration.find_element(locators.RegisterPage.LOCATOR_LOGIN_HREF)
        assert registration.find_element(locators.RegisterPage.LOCATOR_ACCOUNT_BLOCK)