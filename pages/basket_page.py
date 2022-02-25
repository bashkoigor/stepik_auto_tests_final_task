from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS), \
            "Products are presented, but should not be"

    def should_be_text_basket_is_empty(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE)
        assert "Your basket is empty." in message.text, "The text does not present."
