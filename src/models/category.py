from src.models.product import Product  # Импортируем Product для точной типизации


# Типизация: Вверху класса мы описываем, что хранится внутри объекта.В скобках __init__ мы описываем,
# что нужно передать на вход, чтобы этот объект построить.
class Category:
    """Класс Category для представления категории, содержащий список входящих в неё товаров."""

    category_count: int = 0
    product_count: int = 0

    name: str  # название
    description: str  # описание

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products  # Это список объектов Product

        # Увеличиваем счетчик категорий
        Category.category_count += 1
        # # Увеличиваем счетчик уникальных товаров на количество элементов в списке
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет один продукт в приватный список текущей категории"""
        self.__products.append(product)  # Добавляем в наш приватный список
        Category.product_count += 1  # Увеличиваем счетчик всех товаров на 1

    @property
    def products(self) -> str:
        """Геттер, возвращает строку со всеми продуктами в приватном атрибуте products
         в виде строки определенного формата."""
        product_strings = []
        for prod in self.__products:
            # Формируем строку для каждого товара и добавляем в список
            product_strings.append(f"{prod.name}, {int(prod.price)} руб. Остаток: {prod.quantity} шт.")

        # Объединяем все строки через перенос строки (\n), чтобы каждый товар был с новой строчки
        return "\n".join(product_strings)
