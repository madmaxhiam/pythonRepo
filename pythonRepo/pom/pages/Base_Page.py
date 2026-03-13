from typing import Dict
from playwright.sync_api import Page
from page_config import smartphone_page_locators

class BasePage:
    def __init__(self, page: Page, locators: Dict[str, str]):
        self.page = page
        self.locators = locators

    def click(self,element_name : str):
        """Метод для клика по элементу"""
        locator = self.locators.get(element_name)
        if locator:
            self.page.locator(locator).click()
        else:
            raise ValueError(f"Locator for {element_name} not found")

    def fill(self, element_name: str, text: str):
        """Метод для ввода текста в поле"""
        locator = self.locators.get(element_name)
        if locator:
            self.page.locator(locator).fill(text)
        else:
            raise ValueError(f"Locator for {element_name} not found")

    def wait_for_element(self, element_name: str):
        """Метод для ожидания появления элемента"""
        locator = self.locators.get(element_name)
        if locator:
            self.page.locator(locator).wait_for()
        else:
            raise ValueError(f"Locator for {element_name} not found")

    def is_visible(self, element_name: str, timeout: int) -> bool:
        """Проверка видимости элемента"""
        locator = self.locators.get(element_name)
        if locator:
            return self.page.locator(locator).is_visible(timeout= timeout)
        raise ValueError(f"Locator for {element_name} not found")

    def open_item(self, element_name: str,  name_and_price: str, number: int):
        """Открыть карточку товара"""
        locator = self.locators.get(element_name)
        name_price_locator = self.locators.get(name_and_price)
        if locator and name_price_locator:
            self.page.locator(locator).nth(number).locator(name_price_locator).nth(1).click()
        else:
            raise ValueError(f"Locator for {element_name} not found")

    def get_item_data(self, element_name: str,  name_and_price: str, number: int) -> dict:
        """Получить цену и название товара"""
        locator = self.locators.get(element_name)
        name_price_locator = self.locators.get(name_and_price)
        if locator and name_price_locator :
            item_name = self.page.locator(locator).nth(number).locator(name_price_locator).nth(1).inner_text()
            item_price = self.page.locator(locator).nth(number).locator(name_price_locator).nth(0).inner_text()
            return {"name": item_name, "price": item_price}

        raise ValueError(f"Locator for {element_name} not found")

    def add_to_cart_fun(self, number: int) -> dict:
        """Получить цену и название товара"""
        locator = self.locators.get("add_to_cart")
        if locator :
            self.page.locator(locator).nth(number).click()
        else:
            raise ValueError(f"Locator for {smartphone_page_locators.add_to_cart} not found")  # pylint: disable=no-member
