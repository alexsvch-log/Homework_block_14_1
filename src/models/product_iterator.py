from src.models import Category, Product


class ProductIterator:
    """Вспомогательный класс для перебора товаров конкретной категории."""

    def __init__(self, category_obj: Category) -> None:
        # Просим у категории (Category) список живых объектов используя публичный метод в классе Category
        self.products: tuple[Product, ...] = category_obj.get_products()
        self.index = 0  # Начинаем перебор с нулевого индекса

    def __iter__(self) -> "ProductIterator":
        """Возвращает сам объект-итератор."""
        return self

    def __next__(self) -> Product:
        """Возвращает следующий объект товара категории при каждой итерации."""
        if self.index < len(self.products):
            product = self.products[self.index]
            self.index += 1
            return product
        else:
            # Когда товары закончились, останавливаем цикл for
            raise StopIteration
