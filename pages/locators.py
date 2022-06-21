from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    pass
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")

    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PASSWORD = (By.ID, "id_registration-password1")
    REGISTER_RPASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_ALERT= (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_PRICE_INFO = (By.CSS_SELECTOR, ".product_main .price_color")

class BasketPageLocators():
    EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
