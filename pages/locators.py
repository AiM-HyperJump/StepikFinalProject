from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class PageObjectLocators():    
    BTN_ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_AT_MES_ADDED_TO_BASKET = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    NAME_OF_BOOK = (By.CSS_SELECTOR,".col-sm-6.product_main h1")
    BASKET_COST = (By.CSS_SELECTOR, ".alertinner p strong")
    BOOK_COST = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    
class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BTN = (By.CSS_SELECTOR, ".btn-group .btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class BasketPageLocators():
    ANY_BOOK_AT_BASKET = (By.CSS_SELECTOR, ".col-sm-6.h3")
    MSG_EMPTY_BASKET = (By.CSS_SELECTOR, "div p")
    
class LoginPageLocators():
    REGISTRATION_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REG_EMAIL_ADDRESS_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    REG_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REG_PASSWORD_FIELD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    LOG_IN_BTN = (By.CSS_SELECTOR, "[name='registration_submit']")