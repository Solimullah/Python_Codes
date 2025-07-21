from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        self.type_text(username, *self.USERNAME_INPUT)
        self.type_text(password, *self.PASSWORD_INPUT)
        self.click(*self.LOGIN_BUTTON)
