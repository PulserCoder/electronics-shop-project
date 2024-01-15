import pytest
from src.item import Item
from src.phone import Phone


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

    def test_instantiate_from_csv(self) -> None:
        Item.instantiate_from_csv('../homework-2/items.csv')
        assert len(Item.all) == 8

    def test_string_to_number(self) -> None:
        assert Item.string_to_number('123') == 123

    def test_magic_methods(self):
        item1 = Item("Смартфон", 10000, 20)
        assert repr(item1) == "Item('Смартфон', 10000, 20)"
        assert str(item1) == 'Смартфон'

    def test_adding(self):
        phone1 = Phone('123', 1, 2, 2)
        item1 = Item('123', 2, 3)
        assert item1 + phone1 == 5

