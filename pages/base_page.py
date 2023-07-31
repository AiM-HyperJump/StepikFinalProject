from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from .locators import BasketPageLocators
import math
import time

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)
        
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
                
    def solve_quiz_and_get_code(self):
        #self.browser.implicitly_wait(3)
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        time.sleep(4)
        try:
            alert = self.browser.switch_to.alert
            time.sleep(1)
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
            time.sleep(1)
        except NoAlertPresentException:
            print("No second alert presented")          
            
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
        
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
   
    def go_to_basket_page_by_btn(self):
        link = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        link.click()
 
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.ANY_BOOK_AT_BASKET), "Basket is not empty, but should be"
 
    def should_be_msg_about_empty_basket(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.MSG_EMPTY_BASKET).text, "Msg about empty basket is not presented, but should be"
 
    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"