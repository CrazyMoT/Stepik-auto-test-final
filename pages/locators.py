from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    BASKET_FREE = (By.CSS_SELECTOR, "#content_inner > p")


class BookPageLocators():
    BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    BOOK_NAME_PAGE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BOOK_PRICE_PAGE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class LoginPageLocators():
    REG = (By.ID, "register_form")
    LOGIN = (By.ID, "login_form")
    EMAIL = (By.ID, "id_registration-email")
    PASS1 = (By.ID, "id_registration-password1")
    PASS2 = (By.ID, "id_registration-password2")
    LOGIN_SUCSS = (By.CSS_SELECTOR, "#messages > div.alert.alert-success.fade.in > div > i")
    BUTTON = (By.CSS_SELECTOR, "#register_form > button")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")