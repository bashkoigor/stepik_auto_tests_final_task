from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.go_to_login_page()
        input1 = self.browser.find_element(*LoginPageLocators.EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.PASSWORD)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        input3.send_keys(password)

        button = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Registration form is not presented"
