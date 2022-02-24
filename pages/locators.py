from selenium.webdriver.common.by import By


class LoginPageLocators():
    LOGIN_LINK = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    LINK = (By.CSS_SELECTOR, "#add_to_basket_form button.btn")
    PRODUCT_NAME_CART_INFO = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE_CART_INFO = (By.CSS_SELECTOR, "#messages p strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")
