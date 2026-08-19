from product_page import ProductPage


def test_add_product_to_cart(driver):
    product_page = ProductPage(driver)
    product_page.open()
    product_page.search_product("Tshirt")
    product_page.add_first_product_to_cart()
    product_page.go_to_cart()
    cart_item_name = product_page.get_cart_item_name()
    assert "tshirt" in cart_item_name.lower()
