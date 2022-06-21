from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def no_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Product present in basket"

    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"
