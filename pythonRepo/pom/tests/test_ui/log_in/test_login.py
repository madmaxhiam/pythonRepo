import pytest
from pages.Base_Page import BasePage
from page_config import main_page_locators, login_page_locators

#@pytest.mark.smoke
def test_login_negative(set_up, page, pytestconfig) -> None:
    main_page = BasePage(page, main_page_locators)
    main_page.click('log_in')

    login_page = BasePage(page, login_page_locators)
    login_page.fill('username_input', pytestconfig.getoption("username"))
    login_page.fill('password_input', pytestconfig.getoption("password"))
    login_page.click('login_button')
    login_page.is_visible('error', timeout=3000)


@pytest.mark.smoke
def test_login_empty(set_up, page) -> None:
    main_page = BasePage(page, main_page_locators)
    main_page.click('log_in')

    login_page = BasePage(page, login_page_locators)
    login_page.click('login_button')
    login_page.is_visible('err_email', timeout=3000)
    login_page.is_visible('err_pass', timeout=3000)


@pytest.mark.parametrize("user",[
'test@test.cum', '1211111488', '+37511222344'
])
#@pytest.mark.smoke
def test_login_restore_negative(set_up, page, user) -> None:
    page.set_viewport_size({"width": 1024, "height": 768})
    main_page = BasePage(page, main_page_locators)
    main_page.click('log_in')

    login_page = BasePage(page, login_page_locators)
    login_page.click('dont_remember_pass')
    login_page.is_visible('restore_pass', timeout=3000)
    login_page.fill('user_for_restore', user)
    login_page.click('login_button')
    login_page.wait_for_element('restore_error')


#@pytest.mark.smoke
def test_register_is_open(set_up, page) -> None:
    main_page = BasePage(page, main_page_locators)
    main_page.click('log_in')

    login_page = BasePage(page, login_page_locators)
    login_page.click('register')
    login_page.is_visible('register_opened', timeout=3000)
