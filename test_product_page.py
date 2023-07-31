#from .pages.main_page import MainPage
from .pages.locators import LoginPageLocators
from .pages.product_page import ProductPage
import pytest
import time



# # pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  # #@pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  # #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# #def test_guest_can_add_product_to_basket(browser, link):
    # #page = PageObject(browser, link)
    # #page.open()
    # #page.push_to_add_to_basket()
    # #time.sleep(1)
    # #page.solve_quiz_and_get_code()
    # #time.sleep(1)
    # #page.should_be_msg_add_book_to_basket()
    # #page.should_book_cost_match_basket_cost()

#link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"    

# @pytest.mark.xfail
# def test_cant_see_success_message_after_adding_product_to_basket(browser):
    # page = ProductPage(browser, link)
    # page.open()
    # page.push_to_add_to_basket()
    # page.guest_cant_see_success_message_after_adding_product_to_basket()

# def test_guest_cant_see_success_message(browser):
    # page = ProductPage(browser, link)
    # page.open()
    # page.guest_cant_see_success_message()
    
# @pytest.mark.xfail  
# def test_message_disappeared_after_adding_product_to_basket(browser):
    # page = ProductPage(browser, link)
    # page.open()
    # page.push_to_add_to_basket()
    # page.message_disappeared_after_adding_product_to_basket()
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    
def test_guest_can_go_to_login_page_from_product_page (browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()