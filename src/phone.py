from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, amount_of_sim: int):
        super().__init__(name, price, quantity)
        self._amount_of_sim = amount_of_sim

    @property
    def amount_of_sim(self):
        return self._amount_of_sim

    @amount_of_sim.setter
    def amount_of_sim(self, new_value: int):
        if isinstance(new_value, int) and new_value > 0:
            self._amount_of_sim = new_value
        raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        return f"Phone('{self._Item__name}', {self.price}, {self.quantity}, {self.amount_of_sim})"
