from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Базовый абстрактный класс, описывающий общую функциональность всех продуктов."""

    @abstractmethod
    def __str__(self) -> str:
        """Абстрактный метод для строкового отображения продукта.
        Все наследники обязаны уметь возвращать информацию о себе в виде строки.
        """
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        """Абстрактный метод для сложения продуктов.
        Все наследники обязаны уметь складывать стоимости товаров на складе.
        """
        pass
