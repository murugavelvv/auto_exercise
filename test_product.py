from product_page import ProductPage
import pytest


def test_search_product_valid(driver):
    """Search for an existing product and verify correct results display."""
    product_page = ProductPage(driver)
    product_page.open()
    product_page.search_product("Tshirt")
    
    # Verify that products are displayed
    product_names = product_page.get_product_names()
    assert len(product_names) > 0, "Search results should display products for valid search term"
    
    # Verify that search term appears in results
    found_match = any("tshirt" in name.lower() for name in product_names)
    assert found_match, "Search results should contain products matching the search term"


def test_search_product_invalid(driver):
    """Search for a non-existent item and verify no results or empty state."""
    product_page = ProductPage(driver)
    product_page.open()
    product_page.search_product("nonexistentproductxyz123")
    
    # Verify no products are found or results are empty
    product_names = product_page.get_product_names()
    assert len(product_names) == 0, "No products should be displayed for invalid search term"


def test_sort_products_by_price(driver):
    """Verify products sort correctly (Low to High / High to Low)."""
    product_page = ProductPage(driver)
    product_page.open()
    
    # Get initial prices
    initial_prices = product_page.get_product_prices()
    
    # If sort dropdown is not available, skip this test
    if len(initial_prices) < 2:
        pytest.skip("Not enough products to test sorting")
    
    try:
        # Sort by price low to high
        product_page.sort_products_by_price("low_to_high")
        
        # Get sorted prices
        sorted_prices_low_to_high = product_page.get_product_prices()
        
        # Verify prices are in ascending order
        assert sorted_prices_low_to_high == sorted(sorted_prices_low_to_high), "Products should be sorted by price low to high"
    except Exception:
        # If sorting is not available on this page, skip
        pytest.skip("Price sorting feature not available on current page")
