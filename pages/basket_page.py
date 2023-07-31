from .base_page import BasePage
from .base_page import BasePageLocators
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    def go_to_basket_page_by_btn(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        link.click()
 
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ANY_BOOK_AT_BASKET), "Basket is not empty, but should be"
 
    def should_be_msg_about_empty_basket(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.MSG_EMPTY_BASKET).text, "Msg about empty basket is not presented, but should be"