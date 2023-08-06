from .base_page import BasePage
from .locators import LoginPageLocators
from .product_page import ProductPage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Invalid URL"
        self.browser.find_element(*LoginPageLocators.REGISTRATION_LINK).click()

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form not found"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form not found"
    
    def register_new_user(self, email, password):
        email_address_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL_ADDRESS_FIELD)  
        email_address_field.send_keys(email)
        self.browser.execute_script("window.scrollTo(0, 150);")
        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD)
        password_field.send_keys(password)
        password_field = self.browser.find_element(*LoginPageLocators.REG_PASSWORD_FIELD2)    
        password_field.send_keys(password)
        log_in_btn = self.browser.find_element(*LoginPageLocators.LOG_IN_BTN)
        log_in_btn.click()