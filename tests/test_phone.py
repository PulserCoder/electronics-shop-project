import pytest

from src.item import Item
from src.phone import Phone

from src.exceptions import AddPhoneException


class TestPhoneClass:
    def test_creating_phone_object(self) -> None:
        """Testing creating a phone object"""
        phone1 = Phone('1', 2, 4, 2)
        assert phone1.__dict__ == {'_Item__name': '1', 'price': 2, 'quantity': 4, 'amount_of_sim': 2}

    def test_adding_phone_objects(self):
        phone1 = Phone('1', 2, 5, 2)
        phone2 = Phone('1', 2, 4, 2)
        item1 = Item('1', 3, 2)
        assert phone1 + phone2 == 9
        assert phone1 + item1 == 7

    def test_add_phone_exception(self):
        with pytest.raises(AddPhoneException):
            phone1 = Phone('1', 2, 4, 2)
            return phone1 + 2


