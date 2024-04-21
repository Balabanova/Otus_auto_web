from selenium.webdriver.common.by import By


class MainPage:
    LOCATOR_SLIDE_SHOW = (By.CSS_SELECTOR, "#content .slideshow #slideshow0")
    LOCATOR_COMPANIES_CAROUSEL = (By.CSS_SELECTOR, "#content .carousel #carousel0")
    LOCATOR_FEATURED_PRODUCT_IMAGE = (By.CSS_SELECTOR, "#content .row div:first-child .image")
    LOCATOR_FEATURED_PRODUCT_CAPTION = (By.CSS_SELECTOR, "#content .row div:first-child .caption")
    LOCATOR_FEATURED_PRODUCT_BUTTONS = (By.CSS_SELECTOR, "#content .row div:first-child .button-group")
    LOCATOR_PRODUCT_ROW_CART_BUTTON = (By.CSS_SELECTOR, "#content  .row .product-layout button[onclick^=cart]")
    LOCATOR_PRODUCT_ROW_NAME = (By.CSS_SELECTOR, "#content  .row .product-layout .caption h4 a")
    LOCATOR_PRODUCT_ROW_PRICE = (By.CSS_SELECTOR, "#content .row p.price")
    LOCATOR_PRODUCT_ROW_TAX = (By.CSS_SELECTOR, "#content .row p.price .price-tax")


class CatalogPage:
    LOCATOR_PRODUCTS_LIST_GROUP = (By.CSS_SELECTOR, "#product-category #column-left .list-group")
    LOCATOR_LIST_VIEW_BUTTON = (By.CSS_SELECTOR, "#content .row #list-view")
    LOCATOR_GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#content .row #grid-view")
    LOCATOR_INPUT_SORT_INPUT_LIST = (By.CSS_SELECTOR, "#content .row #input-sort")
    LOCATOR_INPUT_LIMIT_INPUT = (By.CSS_SELECTOR, "#content .row #input-limit")
    LOCATOR_PRODUCT_NAME = (By.CSS_SELECTOR, "#content .col-sm-4 h1")
    LOCATOR_PRODUCT_PRICE = (By.CSS_SELECTOR, ".product-thumb p.price")
    LOCATOR_PRODUCT_TAX = (By.CSS_SELECTOR, ".product-thumb p.price .price-tax")


class ProductPage:
    LOCATOR_QUANTITY_TEXTBOX = (By.CSS_SELECTOR, "#product #input-quantity")
    LOCATOR_ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, "[onclick=\"wishlist.add('41');\"]")
    LOCATOR_ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#product #button-cart")
    LOCATOR_RATING_DIV = (By.CSS_SELECTOR, ".rating")
    LOCATOR_WRITE_REVIEW_LINK = (By.XPATH, "//*[contains(text(),'Write a review')]")


class AdminLoginPage:
    LOCATOR_HELP_BLOCK_HREF = (By.CSS_SELECTOR, ".help-block a[href]")
    LOCATOR_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type=\"submit\"]")
    LOCATOR_USERNAME_INPUT = (By.CSS_SELECTOR, "input#input-username")
    LOCATOR_PASSWORD_INPUT = (By.CSS_SELECTOR, "input#input-password")
    LOCATOR_FA_ICON = (By.CSS_SELECTOR, ".panel-body i.fa")


class RegisterPage:
    LOCATOR_CONTINUE_BUTTON = (By.CSS_SELECTOR, "#account-register .pull-right [value=\"Continue\"]")
    LOCATOR_PRIVATE_POL_HREF = (By.CSS_SELECTOR, "#account-register .pull-right a[href]")
    LOCATOR_LOGIN_HREF = (By.CSS_SELECTOR, "#account-register  #content a[href]")
    LOCATOR_ACCOUNT_BLOCK = (By.CSS_SELECTOR, "#account")
    LOCATOR_FIRSTNAME_INPUT = (By.CSS_SELECTOR, "#account-register input[id=\"input-firstname\"]")
    LOCATOR_LASTNAME_INPUT = (By.CSS_SELECTOR, "#account-register input[id=\"input-lastname\"]")
    LOCATOR_EMAIL_INPUT = (By.CSS_SELECTOR, "#account-register input[id=\"input-email\"]")
    LOCATOR_TELEPHONE_INPUT = (By.CSS_SELECTOR, "#account-register input[id=\"input-telephone\"]")
    LOCATOR_PASSWORD_INPUT = (By.CSS_SELECTOR, "#account-register input[id=\"input-password\"]")
    LOCATOR_CONFIRM_INPUT = (By.CSS_SELECTOR, "#account-register input[id=\"input-confirm\"]")
    LOCATOR_AGREE_CHECKBOX = (By.CSS_SELECTOR, "#content .buttons input[name=\"agree\"]")


class AdminDashboardPage:
    LOCATOR_LOGOUT_BUTTON = (By.CSS_SELECTOR, "#container .navbar-right .fa-sign-out")
    LOCATOR_MENU_CATALOG_BUTTON = (By.CSS_SELECTOR, "#menu-catalog")
    LOCATOR_MENU_CATALOG_PRODUCTS = (By.CSS_SELECTOR, "#menu-catalog  li:nth-of-type(2)")
    LOCATOR_MENU_CATALOG_ACTIVE = (By.CSS_SELECTOR, '#menu-catalog a[aria-expanded="true"]')


class AdminProductPage:
    LOCATOR_ADD_PRODUCT = (By.CSS_SELECTOR, '.page-header a[data-original-title="Add New"]')


class AdminNewProductPage:
    LOCATOR_GENERAL_NAME = (By.CSS_SELECTOR, "input#input-name1")
    LOCATOR_GENERAL_TAG_TITLE = (By.CSS_SELECTOR, "input#input-meta-title1")
    LOCATOR_DATA_BUTTON = (By.XPATH, "//*[contains(text(),'Data')]")
    LOCATOR_DATA_MODEL = (By.CSS_SELECTOR, "input#input-model")
    LOCATOR_SAVE_BUTTON = (By.CSS_SELECTOR, 'button[data-original-title="Save"]')


class CartPage:
    LOCATOR_PRODUCTS_NAMES = (By.CSS_SELECTOR, "#content .table-responsive tbody .text-left a[href]")


class Navigation:
    LOCATOR_CURRENCY_BUTTON = (By.CSS_SELECTOR, "#top #form-currency")
    LOCATOR_CURRENCY_EUR_BUTTON = (By.CSS_SELECTOR, "#top #form-currency .dropdown-menu button[name=EUR]")
    LOCATOR_CURRENCY_GBP_BUTTON = (By.CSS_SELECTOR, "#top #form-currency .dropdown-menu button[name=GBP]")
    LOCATOR_CURRENCY_USD_BUTTON = (By.CSS_SELECTOR, "#top #form-currency .dropdown-menu button[name=USD]")
    LOCATOR_MY_ACCOUNT = (By.XPATH, "//*[contains(text(),'My Account')]")
    LOCATOR_WISHLIST = (By.CSS_SELECTOR, "#top .list-inline #wishlist-total")