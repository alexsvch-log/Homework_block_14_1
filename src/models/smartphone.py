from .product import Product


class Smartphone(Product):
    """Класс-наследник класса Product для представления смартфона."""

    # Подсказки типов для свойств объекта пишем строго ТУТ (на уровне класса)
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):

        # Вызываем метод базового класса
        super().__init__(name, description, price, quantity)
        # Дополнительные характеристики нового подкласса
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
