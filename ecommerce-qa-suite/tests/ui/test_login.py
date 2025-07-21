import pytest
from ecommerce-qa-suite.pages.login_page import LoginPage

@pytest.mark.ui
def test_successful_login(driver):
    driver.get("http://example.com/login")
    login_page = LoginPage(driver)
    login_page.login("testuser", "testpassword")
    assert "dashboard" in driver.current_url, "Login failed"
