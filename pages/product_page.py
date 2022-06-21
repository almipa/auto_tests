from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):
    def add_product_to_basket(self, quiz = False):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        if quiz:
            self.solve_quiz_and_get_code()

    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text

    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def get_product_name_alert(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ALERT)
        return product_price.text

    def get_basket_price_info(self):
        product_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_INFO)
        return product_price.text
    
    def product_should_be_added_to_basket(self):
        assert self.get_product_name() == self.get_product_name_alert()
        assert self.get_product_price() == self.get_basket_price_info()
    
    def no_success_message_for_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_ALERT)
    
    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_ALERT)
