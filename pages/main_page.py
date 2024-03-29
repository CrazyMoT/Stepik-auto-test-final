from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def should_be_open_basket(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((MainPageLocators.BASKET_LINK))).click(), "Error locate button"
        assert WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((MainPageLocators.BASKET_FREE))).text != "", "Basket not free"

