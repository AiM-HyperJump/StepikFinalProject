from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        print("bsvsd")
        
    def test_guest_should_see_login_link(self, browser):
        print("bsvsd")