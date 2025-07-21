import pytest
from ecommerce-qa-suite.pages.login_page import LoginPage

@pytest.mark.ui
def test_login(driver):
    driver.get("http://example.com/login")
    login_page = LoginPage(driver)
    login_page.login("user", "password")
    assert "dashboard" in driver.current_url
