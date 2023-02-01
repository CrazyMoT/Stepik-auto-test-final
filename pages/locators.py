from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


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


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")