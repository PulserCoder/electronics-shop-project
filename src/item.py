import csv

from src.exceptions import AddPhoneException

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value[:10]

    @classmethod
    def instantiate_from_csv(cls, path: str) -> None:
        """
            Создает экземпляры товаров из CSV-файла и добавляет их в список.

            Args:
                path (str): Путь к CSV-файлу.
        """
        with open(path, newline='', encoding='latin-1') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        :param number is string: The number to convert to integer
        :return: The number to converted to string
        """
        a = float(number)
        return int(a)

    def __add__(self, other) -> float:
        if isinstance(other, Item):
            return self.quantity + other.quantity
        if issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        raise AddPhoneException(f"Невозможно сложить {self.__class__} с {other.__class__}")
