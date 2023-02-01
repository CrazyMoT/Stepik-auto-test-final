import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import BookPageLocators


class BookPage(BasePage):
    def should_be_book_to_basket(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable((BookPageLocators.BASKET))).click(), "Error locate button"
        self.solve_quiz_and_get_code()
        time.sleep(3)
        assert self.browser.find_element(*BookPageLocators.BOOK_NAME).text == \
               self.browser.find_element(*BookPageLocators.BOOK_NAME_PAGE).text, "Error name of product"

        time.sleep(1)
        assert self.browser.find_element(*BookPageLocators.BOOK_PRICE).text == \
               self.browser.find_element(*BookPageLocators.BOOK_PRICE_PAGE).text, "Error price"
