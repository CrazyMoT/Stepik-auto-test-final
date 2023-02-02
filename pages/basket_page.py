import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import MainPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((MainPageLocators.BASKET_LINK))).click(), "Error locate button"
        assert WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((MainPageLocators.BASKET_FREE))).text != "", "Basket not free"

