from .base_page import BasePage
from .locators import PageObjectLocators
from selenium.webdriver.common.by import By

class PageObject(BasePage):
    def push_to_add_to_basket(self):
        btn = self.browser.find_element(*PageObjectLocators.BTN_ADD_BASKET)
        btn.click()
    
    def should_be_msg_add_book_to_basket(self):
        self.browser.find_element(*PageObjectLocators.BTN_ADD_BASKET)
        assert self.browser.find_element(*PageObjectLocators.NAME_OF_BOOK).text == self.browser.find_element(*PageObjectLocators.BOOK_NAME_AT_MES_ADDED_TO_BASKET).text, "Name of book not match"
        
    def should_book_cost_match_basket_cost(self):
        assert self.browser.find_element(*PageObjectLocators.BASKET_COST).text == self.browser.find_element(*PageObjectLocators.BOOK_COST).text, "Cost of book not matches basket cost"
        