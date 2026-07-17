from .base_storage import BaseStorage
from .product import Product


class Order(BaseStorage):
    """Класс для оформления заказа на один товар."""

    product: Product
    quantity: int
    total_price: float

    def __init__(self, order_name: str, product: Product, quantity: int) -> None:
        # Передаем имя/номер заказа в абстрактный класс
        super().__init__(order_name)

        # Проверяем, что нам передали именно продукт (помним про безопасность!)
        if not isinstance(product, Product):
            raise TypeError("В заказе можно указать только объект класса Product или его наследников")

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self) -> str:
        return f"{self.name}: {self.product.name}, {self.quantity} шт. Итого: {self.total_price} руб."
