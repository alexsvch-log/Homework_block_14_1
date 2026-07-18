from typing import Any

from .base_product import BaseProduct
from .print_mixin import PrintMixin  # Импортируем наш миксин


class Product(PrintMixin, BaseProduct):
    """Класс для представления конкретного товара и его характеристик."""

    name: str  # Наименование номенклатуры товара
    description: str  # Описание товара
    __price: float  # Цена единицы товара
    quantity: int  # Количество единиц товара

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        """Конструктор базового продукта с валидацией количества."""
        # Жесткая проверка: количество не может быть нулем (или отрицательным)
        if quantity <= 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен.")

        # ШАГ 1: Сначала сохраняем все свойства в объект! Это при наличии миксина
        self.name = name  # Название товара (например, "Iphone 15")
        self.description = description  # Описание товара
        self.__price = price  # Цена товара (дробное число)/ Делаем цену полностью приватной
        self.quantity = quantity  # Количество товара на складе (целое число)
        # ШАГ 2: Только когда объект полностью наполнен данными,
        # вызываем super() и отправляем поезд в PrintMixin! Если бы миксина не было, то эта строка
        # стояла бы ДО определения свойств.
        super().__init__()  # Если у BaseProduct нет своего __init__, вызываем встроенный

    @classmethod
    def new_product(cls, product_data: dict[str, Any], current_products: list["Product"] | None = None) -> "Product":
        """Класс-метод для создания товара с проверкой на дубликаты."""
        name: str = str(product_data.get("name"))
        description: str = str(product_data.get("description", ""))
        price: float = float(product_data.get("price", 0.0))
        quantity: int = int(product_data.get("quantity", 0))

        if current_products:
            for product in current_products:
                if product.name == name:
                    product.quantity += quantity
                    # Меняем цену через сеттер .price
                    product.price = max(product.price, price)
                    return product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер для безопасного чтения приватной цены снаружи."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для валидации и подтверждения снижения цены."""
        # 1. Проверка на корректность значения
        if new_price <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            return  # Сразу выходим, дальше проверять не нужно

        # 2. Проверка на понижение цены
        if new_price < self.__price:
            user_answer = input(f"Вы уверены, что хотите снизить цену с {self.__price} до {new_price}? (y/n): ")
            if user_answer.lower() == "y":
                self.__price = new_price
                print("Цена успешно снижена.")
            else:
                print("Действие отменено. Цена осталась прежней.")
        else:
            # Если цена повышается или не изменилась, просто записываем её
            self.__price = new_price

    # Добавляем магический метод отображения объекта в списках
    def __str__(self) -> str:  # значок показывает, что мы переписали встроенный метод Python
        # f-строка вернет красивый понятный текст вместо технической абракадабры
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        """Магический метод для сложения двух товаров.
        Разрешает сложение только строго одинаковых классов продуктов.
        """
        # Проверяем, что типы (классы) левого и правого объекта абсолютно идентичны
        if type(self) is not type(other):
            raise TypeError("Складывать можно только товары одного и того же класса")

        # Если проверка прошла, считаем полную стоимость на складе
        self_total_price = self.price * self.quantity
        other_total_price = other.price * other.quantity

        return self_total_price + other_total_price

    # def to_list(self):
    #     # Вот этот метод уже вернет тип данных list
    #     return [self.name, self.description, self.price, self.quantity]
