import pytest
from ecommerce-qa-suite.pages.login_page import LoginPage
from ecommerce-qa-suite.utils.config_loader import load_config

@pytest.mark.ui
def test_successful_login(driver):
    config = load_config()
    driver.get(config['base_url'] + config['endpoints']['login'])
    login_page = LoginPage(driver)
    login_page.login(config['credentials']['username'], config['credentials']['password'])
    assert "dashboard" in driver.current_url, "Login failed"
