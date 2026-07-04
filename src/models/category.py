from src.models.product import Product  # Импортируем Product для точной типизации


# Типизация: Вверху класса мы описываем, что хранится внутри объекта.В скобках __init__ мы описываем,
# что нужно передать на вход, чтобы этот объект построить.
class Category:
    category_count = 0
    product_count = 0
    """Класс Category для представления категории, содержащий список входящих в неё товаров."""
    name: str  # название
    description: str  # описание
    products: list[Product]  # УТОЧНИЛИ: это список, в котором лежат объекты Product

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.products = products  # Это список объектов Product

        # Увеличиваем счетчик категорий
        Category.category_count += 1
        # Увеличиваем счетчик уникальных товаров на количество элементов в списке
        Category.product_count += len(products)
