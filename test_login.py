from login_page import LoginPage


def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("vmurugavel877@gmail.com", "muru@123")
    logged_in_text = login_page.is_logged_in()
    assert "Logged in as" in logged_in_text


def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("wrong_user@mail.com", "WrongPass")
    error_message = login_page.get_error_message()
    assert "Your email or password is incorrect" in error_message
