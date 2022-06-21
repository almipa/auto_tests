import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
LOGIN_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"

#@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket(True)
    product_page.product_should_be_added_to_basket()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.no_success_message_for_basket()

def test_guest_cant_see_success_message(browser):    
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.no_success_message_for_basket()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, PRODUCT_LINK)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.success_message_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url);
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url) 
    basket_page.no_product_in_basket()
    basket_page.basket_is_empty()

@pytest.mark.need_review
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        email = str(time.time()) + "@fakemail.org"
        login_page.register_new_user(email, 'qq12345678')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):    
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.no_success_message_for_basket()

    def test_user_can_add_product_to_basket(self, browser):
        product_page = ProductPage(browser, PRODUCT_LINK)
        product_page.open()
        product_page.add_product_to_basket()
        product_page.product_should_be_added_to_basket()


