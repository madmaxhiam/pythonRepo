# Конфигурация локаторов для страницы входа

main_page_locators = {
    "log_in": "text ='Вход'",
    "smart_phones": "text='Смартфоны'",
    "cart": "a[title='Корзина']",
    "delete_from_cart": "//div[@class='cart-form__control']/a"
}
login_page_locators = {
    "username_input": "input[placeholder='Ник или e-mail']",
    "password_input": "input[placeholder='Пароль']",
    "login_button": "button[type='submit']",
    "error": "div:has-text('Неверный логин или пароль')",
    "err_email": "div:has-text('Укажите ник или e-mail')",
    "err_pass": "div:has-text('Укажите пароль')",
    "dont_remember_pass": "a:text('Я не помню пароль')",
    "restore_pass":"div:has-text('Восстановление пароля')",
    "user_for_restore":"input[placeholder='Ник, e-mail или номер телефона']",
    "restore_error":"//div[contains(text(), 'Такой пользователь не зарегистрирован')]",
    "register": "a:text('Зарегистрироваться на Onlíner')",
    "register_opened": "div:has-text('Регистрация')"
}

smartphone_page_locators = {
    "title": "h1:has-text('Мобильные телефоны')",
    "goods":".catalog-form__offers-item_primary",
    "title_and_price": "a.catalog-form__link.catalog-form__link_primary-additional",
    "offers_count": "span[itemprop='offerCount']",
    "add_to_cart": "a:has-text('В корзину')",
    "goto_cart":"a:has-text('Перейти в корзину')",
    "goto_placing": "a:has-text('Перейти к оформлению')",
}
