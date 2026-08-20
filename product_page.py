from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from base import BasePage


class ProductPage(BasePage):
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    FIRST_PRODUCT_ADD_BTN = (By.XPATH, "(//a[contains(@class, 'add-to-cart')])[1]")
    SECOND_PRODUCT_ADD_BTN = (By.XPATH, "(//a[contains(@class, 'add-to-cart')])[2]")
    CONTINUE_SHOPPING_BTN = (By.XPATH, "//button[contains(text(), 'Continue Shopping')]")
    CART_HEADER_LINK = (By.XPATH, "//a[contains(@href, '/view_cart')]")
    CART_ITEM_NAME = (By.XPATH, "//td[contains(@class, 'cart_description')]//a")
    CART_BADGE = (By.XPATH, "//a[contains(@href, '/view_cart')]/preceding-sibling::ul/li")
    NO_RESULTS_MSG = (By.XPATH, "//p[contains(text(), 'No products found') or contains(text(), 'Sorry')]")
    PRODUCT_PRICE = (By.XPATH, "//div[@class='productinfo text-center']//h2")
    SORT_DROPDOWN = (By.XPATH, "//select[@id='sort']")
    STOCK_STATUS = (By.XPATH, "//div[@class='productinfo text-center']//p")
    PRODUCT_NAMES = (By.XPATH, "//div[@class='productinfo text-center']//p")
    
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
    
    def add_second_product_to_cart(self):
        """Add second product to cart"""
        self.click(self.SECOND_PRODUCT_ADD_BTN)
        self.click(self.CONTINUE_SHOPPING_BTN)
    
    def get_cart_badge_count(self):
        """Get the number of items in cart badge"""
        try:
            badge_text = self.get_text(self.CART_BADGE)
            return int(badge_text.strip())
        except (TimeoutException, ValueError):
            return 0
    
    def is_no_results_displayed(self):
        """Check if 'No products found' message is displayed"""
        try:
            self.find(self.NO_RESULTS_MSG)
            return True
        except TimeoutException:
            return False
    
    def get_no_results_message(self):
        """Get the no results message text"""
        try:
            return self.get_text(self.NO_RESULTS_MSG)
        except TimeoutException:
            return ""
    
    def get_product_prices(self):
        """Get list of product prices on current page"""
        try:
            elements = self.driver.find_elements(*self.PRODUCT_PRICE)
            return [float(element.text.replace('Rs.', '').strip()) for element in elements]
        except (TimeoutException, ValueError):
            return []
    
    def sort_products_by_price(self, sort_order="low_to_high"):
        """Sort products by price. Options: 'low_to_high' or 'high_to_low'"""
        from selenium.webdriver.support.ui import Select
        select = Select(self.find(self.SORT_DROPDOWN))
        if sort_order == "low_to_high":
            select.select_by_visible_text("Price: Low to High")
        elif sort_order == "high_to_low":
            select.select_by_visible_text("Price: High to Low")
    
    def get_product_stock_status(self, index=1):
        """Get stock status of product at given index (1-based)"""
        try:
            elements = self.driver.find_elements(*self.STOCK_STATUS)
            if index <= len(elements):
                return elements[index - 1].text
            return ""
        except TimeoutException:
            return ""
    
    def is_product_in_stock(self, index=1):
        """Check if product at given index is in stock"""
        stock_text = self.get_product_stock_status(index)
        return "out of stock" not in stock_text.lower()
    
    def get_product_names(self):
        """Get list of product names on current page"""
        try:
            elements = self.driver.find_elements(*self.PRODUCT_NAMES)
            return [element.text for element in elements]
        except TimeoutException:
            return []
