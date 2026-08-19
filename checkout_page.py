from selenium.webdriver.common.by import By
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
