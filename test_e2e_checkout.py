from login_page import LoginPage
from product_page import ProductPage
from checkout_page import CheckoutPage


def test_complete_e2e_order_placement(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("vmurugavel877@gmail.com", "muru@123")
    
    # Add product to cart
    product_page = ProductPage(driver)
    product_page.open()
    product_page.search_product("Tshirt")
    product_page.add_first_product_to_cart()
    
    # Go to cart and checkout
    product_page.go_to_cart()
    
    checkout_page = CheckoutPage(driver)
    checkout_page.proceed_to_checkout()
    checkout_page.enter_order_comment("Automated Order Test")
    checkout_page.click_place_order()
    
    # Enter payment details
    checkout_page.enter_payment_details("Murugavel", "4111111111111111", "123", "12", "2028")
    checkout_page.click_pay_and_confirm()
    
    # Verify success
    success_message = checkout_page.get_success_message()
    assert "order placed" in success_message.lower() or "congratulations" in success_message.lower()
