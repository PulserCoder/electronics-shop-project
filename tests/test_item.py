import pytest
from src.item import Item


class TestItem:

    def test_item_added_to_all(self) -> None:
        """
        Тест проверяет, что созданный товар добавлен в список 'all' класса Item.
        """
        item = Item("123", 40.0, 4)

        assert item in Item.all

    def test_calculate_total_price(self) -> None:
        """
        Тест проверяет, что метод calculate_total_price возвращает правильное значение.
        """
        item = Item("123", 10.0, 2)

        assert item.calculate_total_price() == 20.0

    def test_apply_discount(self) -> None:
        """
        Тест проверяет, что метод apply_discount правильно применяет скидку к товару.
        """
        item = Item("123", 20.0, 3)

        Item.pay_rate = 0.8
        item.apply_discount()

        assert item.price == 20.0 * Item.pay_rate
