from .pages.main_page import MainPage
from .pages.locators import LoginPageLocators
from .pages.product_page import PageObject


link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

# def test_guest_can_go_to_login_page(browser):
    # page = MainPage(browser, link)
    # page.open()
    # page.go_to_login_page()
    # login_page = LoginPage(browser, browser.current_url)
    # login_page.should_be_login_page()
    
# def test_guest_should_see_login_link(browser):
    # page = MainPage(browser, link)
    # page.open()
    # page.should_be_login_link()
    
def test_add_book_to_basket(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.push_to_add_to_basket