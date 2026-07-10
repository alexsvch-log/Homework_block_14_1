from abc import ABC, abstractmethod


class BaseStorage(ABC):
    """Абстрактный класс для категорий и заказов, имеющих имя и работающих с товарами."""

    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def __str__(self) -> str:
        """Обязательный метод отображения для категорий и заказов."""
        pass
