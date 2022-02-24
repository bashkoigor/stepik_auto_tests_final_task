from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        link = self.browser.find_element(*ProductPageLocators.LINK)
        link.click()

    def get_product_name(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product.text

    def get_product_price(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product.text

    def did_product_add_to_cart(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_CART_INFO)
        product_name = self.get_product_name()
        assert product.text == product_name, "Product name does not match with product name added to cart."

    def is_price_match(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_CART_INFO)
        product_price = self.get_product_price()
        assert product.text == product_price, "Product price does not match with product price added to cart."
