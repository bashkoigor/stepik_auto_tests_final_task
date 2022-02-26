from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    LINK = (By.CSS_SELECTOR, "#add_to_basket_form button.btn")
    PRODUCT_NAME_CART_INFO = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE_CART_INFO = (By.CSS_SELECTOR, "#messages p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCTS = (By.CSS_SELECTOR, "#basket_formset")
    BASKET_PAGE_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")


