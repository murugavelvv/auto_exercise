from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from base import BasePage


class CheckoutPage(BasePage):
    PROCEED_TO_CHECKOUT_BTN = (By.XPATH, "//a[contains(text(), 'Proceed To Checkout')]")
    COMMENT_TEXTAREA = (By.NAME, "message")
    PLACE_ORDER_BTN = (By.XPATH, "//a[contains(@href, '/payment')]")
    CARD_NAME_INPUT = (By.NAME, "name_on_card")
    CARD_NUMBER_INPUT = (By.NAME, "card_number")
    CVC_INPUT = (By.NAME, "cvc")
    EXP_MONTH_INPUT = (By.NAME, "expiry_month")
    EXP_YEAR_INPUT = (By.NAME, "expiry_year")
    PAY_BUTTON = (By.XPATH, "//button[@data-qa='pay-button']")
    ORDER_SUCCESS_MSG = (By.XPATH, "//*[contains(text(), 'Order Placed!') or contains(text(), 'congratulations')]")
    EMPTY_CART_MSG = (By.XPATH, "//p[contains(text(), 'empty') or contains(text(), 'Your cart is empty')]")
    PAYMENT_ERROR_MSG = (By.XPATH, "//*[contains(text(), 'Invalid') or contains(text(), 'card number') or contains(text(), 'expired')]")
    CART_TOTAL = (By.XPATH, "//td[contains(@class, 'cart_total')]//span")
    CART_QUANTITY = (By.XPATH, "//td[contains(@class, 'cart_quantity')]//button")
    DELETE_ITEM_BTN = (By.XPATH, "//td[contains(@class, 'cart_delete')]//a")
    
    def proceed_to_checkout(self):
        self.click(self.PROCEED_TO_CHECKOUT_BTN)
    
    def enter_order_comment(self, comment):
        self.type_text(self.COMMENT_TEXTAREA, comment)
    
    def click_place_order(self):
        self.click(self.PLACE_ORDER_BTN)
    
    def enter_payment_details(self, name, card_num, cvc, month, year):
        self.type_text(self.CARD_NAME_INPUT, name)
        self.type_text(self.CARD_NUMBER_INPUT, card_num)
        self.type_text(self.CVC_INPUT, cvc)
        self.type_text(self.EXP_MONTH_INPUT, month)
        self.type_text(self.EXP_YEAR_INPUT, year)
    
    def click_pay_and_confirm(self):
        self.click(self.PAY_BUTTON)
    
    def get_success_message(self):
        return self.get_text(self.ORDER_SUCCESS_MSG)
    
    def is_cart_empty(self):
        """Check if cart is empty by looking for empty cart message"""
        try:
            self.find(self.EMPTY_CART_MSG)
            return True
        except TimeoutException:
            return False
    
    def get_empty_cart_message(self):
        """Get empty cart message text"""
        try:
            return self.get_text(self.EMPTY_CART_MSG)
        except TimeoutException:
            return ""
    
    def is_proceed_to_checkout_enabled(self):
        """Check if proceed to checkout button is enabled"""
        try:
            element = self.find(self.PROCEED_TO_CHECKOUT_BTN)
            return element.is_enabled()
        except TimeoutException:
            return False
    
    def get_payment_error_message(self):
        """Get payment error message for invalid card details"""
        try:
            return self.get_text(self.PAYMENT_ERROR_MSG)
        except TimeoutException:
            return ""
    
    def is_payment_error_displayed(self):
        """Check if payment error is displayed"""
        try:
            self.find(self.PAYMENT_ERROR_MSG)
            return True
        except TimeoutException:
            return False
    
    def get_cart_total(self):
        """Get the total amount in cart"""
        try:
            total_text = self.get_text(self.CART_TOTAL)
            return float(total_text.replace('Rs.', '').strip())
        except (TimeoutException, ValueError):
            return 0.0
    
    def get_item_quantity(self):
        """Get quantity of first item in cart"""
        try:
            quantity_text = self.get_text(self.CART_QUANTITY)
            return int(quantity_text)
        except (TimeoutException, ValueError):
            return 0
    
    def delete_first_item(self):
        """Delete first item from cart"""
        self.click(self.DELETE_ITEM_BTN)
    
    def get_order_summary_total(self):
        """Get order summary total from checkout page"""
        return self.get_cart_total()
    
    def clear_payment_fields(self):
        """Clear all payment form fields"""
        self.type_text(self.CARD_NAME_INPUT, "")
        self.type_text(self.CARD_NUMBER_INPUT, "")
        self.type_text(self.CVC_INPUT, "")
        self.type_text(self.EXP_MONTH_INPUT, "")
        self.type_text(self.EXP_YEAR_INPUT, "")
