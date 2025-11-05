from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    LOGIN_BUTTON = (By.ID, "login-btn")

    def go_to_login(self):
        self.click(self.LOGIN_BUTTON)
