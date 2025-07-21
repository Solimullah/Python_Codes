from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchPage(BasePage):
    SEARCH_INPUT = (By.ID, "search-input")
    SEARCH_BUTTON = (By.ID, "search-button")

    def search(self, query):
        self.type_text(query, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BUTTON)
