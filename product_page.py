from selenium.webdriver.common.by import By
from base import BasePage


class ProductPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    FIRST_PRODUCT_ADD_BTN = (By.XPATH, "(//a[contains(@class, 'add-to-cart')])[1]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
    CART_HEADER_LINK = (By.XPATH, "//a[contains(@href, '/view_cart')]")
    CART_ITEM_NAME = (By.XPATH, "//td[contains(@class, 'cart_description')]//a")
    
    def open(self):
        self.open_url("https://automationexercise.com/products")
    
    def search_product(self, product_name):
        self.type_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)
    
    def add_first_product_to_cart(self):
        self.click(self.FIRST_PRODUCT_ADD_BTN)
        self.click(self.CONTINUE_SHOPPING_BTN)
    
    def go_to_cart(self):
        self.click(self.CART_HEADER_LINK)
    
    def get_cart_item_name(self):
        return self.get_text(self.CART_ITEM_NAME)
