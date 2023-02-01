from pages.main_page import MainPage
from pages.product_page import BookPage
import pytest

# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = BookPage(browser, link)
#     page.open()
#     page.should_be_book_to_basket()


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"

urls = [f"{product_base_link}?promo=offer{no}" if no != "???"
        else pytest.param("bugged_link", marks=pytest.mark.xfail) for no in range(10)]


@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = BookPage(browser, link)
    page.open()
    page.should_be_book_to_basket()
