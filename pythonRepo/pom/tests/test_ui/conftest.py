import pytest
from pages.Base_Page import BasePage
from page_config import smartphone_page_locators, main_page_locators

@pytest.fixture
def set_up(page):
    page.goto('https://www.onliner.by/')
    yield page
    page.close()

@pytest.fixture
def set_up_with_item_in_cart(page):
    page.goto('https://www.onliner.by/')
    main_page = BasePage(page, main_page_locators)
    main_page.click('smart_phones')

    phones_page = BasePage(page, smartphone_page_locators)
    phones_page.open_item('goods', 'title_and_price', 1)
    phones_page.click('offers_count')
    phones_page.add_to_cart_fun(1)
    page.reload()
    yield page
    page.close()


def pytest_addoption(parser):
    parser.addoption(
        "--username", 
        action="store",
        default="test",
    )
    parser.addoption(
        "--password",
        action="store",
        default="test",
    )
