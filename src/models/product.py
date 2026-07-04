class Product:
    """Класс для представления конкретного товара и его характеристик."""

    name: str  # Наименование номенклатуры товара
    description: str  # Описание товара
    price: float  # Цена единицы товара
    quantity: int  # Количество единиц товара

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # Название товара (например, "Iphone 15")
        self.description = description  # Описание товара
        self.price = price  # Цена товара (дробное число)
        self.quantity = quantity  # Количество товара на складе (целое число)

    # Добавляем магический метод отображения объекта в списках
    def __repr__(self) -> str:  # значок показывает, что мы переписали встроенный метод Python
        # f-строка вернет красивый понятный текст вместо технической абракадабры
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"

    # def to_list(self):
    #     # Вот этот метод уже вернет тип данных list
    #     return [self.name, self.description, self.price, self.quantity]
