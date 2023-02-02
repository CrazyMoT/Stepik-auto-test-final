import time
from random import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN), "Login form not detected"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG), "Reg form not detected"

    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(random())

        input1 = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((LoginPageLocators.EMAIL)))
        input1.send_keys(email)
        assert "Error write e-mail"

        input2 = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((LoginPageLocators.PASS1)))
        input2.send_keys(password)
        assert "Error write password"

        input3 = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((LoginPageLocators.PASS2)))
        input3.send_keys(password)
        assert "Error write password 2"

        WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((LoginPageLocators.BUTTON))).click()

        assert WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located((LoginPageLocators.LOGIN_SUCSS))), "Not register"

