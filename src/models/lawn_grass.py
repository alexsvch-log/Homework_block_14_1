from .product import Product


class LawnGrass(Product):
    """Класс-наследник класса Product для представления газонной травы."""

    country: str  # Страна-производитель
    germination_period: str  # Срок прорастания (в днях)
    color: str  # Цвет

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        # Передаем базовые параметры в конструктор родительского класса Product
        super().__init__(name, description, price, quantity)

        # Сохраняем новые уникальные свойства травы
        self.country = country
        self.germination_period = germination_period
        self.color = color
