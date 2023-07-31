from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class PageObjectLocators():    
    BTN_ADD_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    BOOK_NAME_AT_MES_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    NAME_OF_BOOK = (By.CSS_SELECTOR,".col-sm-6.product_main h1")
    BASKET_COST = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_COST = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    
class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class LoginPageLocators():
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")