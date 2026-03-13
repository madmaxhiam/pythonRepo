import pytest
from pages.Base_Page import BasePage
from page_config import main_page_locators, smartphone_page_locators

@pytest.mark.regression
def test_open_smartphones(set_up, page) -> None:
    main_page = BasePage(page, main_page_locators)
    main_page.click('smart_phones')

    phones_page = BasePage(page, smartphone_page_locators)
    phones_page.is_visible('title', timeout=3000)

@pytest.mark.xfail(condition=True, reason="временно изменились локаторы на сайте")
@pytest.mark.regression
def test_add_to_cart(set_up, page) -> None:
    main_page = BasePage(page, main_page_locators)
    main_page.click('smart_phones')

    phones_page = BasePage(page, smartphone_page_locators)
    item_data = phones_page.get_item_data('goods', 'title_and_price', 1)
    phones_page.open_item('goods', 'title_and_price', 1)
    phones_page.click('offers_count')
    phones_page.add_to_cart_fun(1)
    phones_page.click("goto_cart")
    phones_page.wait_for_element('goto_placing')
    assert item_data['name'] in page.content()
