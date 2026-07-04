import json
from pathlib import Path

from src.models import Category, Product


def reader_json(file_path: Path) -> list | dict:
    """Принимает на вход путь до JSON-файла с данными (словарь или список) и возвращает словарь (dict).
    Если файл пустой, поврежден, не найден или содержит не словарь и не список (например, строку или число),
    функция возвращает пустой словарь {}.
    Функция не проверяет считанный JSON-файл на правильность информации по всем транзакциям
    (наличие всех ключей и т.п.)"""

    try:
        with open(file_path, encoding="utf-8") as file:
            data = json.load(file)
            # Проверяем, что корневой элемент — это именно словарь (объект)
            if isinstance(data, (dict, list)):
                return data
            else:
                return {}  # Возвращаем пустой словарь, если там не-словарь

    except (FileNotFoundError, json.JSONDecodeError):
        # json.JSONDecodeError перехватит пустой или сломанный JSON-файл
        # FileNotFoundError перехватит отсутствие файла
        return {}


def create_objects_from_json(file_path: Path) -> list[Category]:
    """Запрашивает данные из reader_json и превращает их в объекты классов.
    При необходимости переводит словарь в список перед обработкой."""

    raw_data = reader_json(file_path)
    categories: list[Category] = []

    # ЕСЛИ ПРИШЕЛ СЛОВАРЬ (Ваша логика):
    # Мы проверяем, не пустой ли он, и переводим в список
    if isinstance(raw_data, dict):
        if not raw_data:  # Если вернулся {} из-за ошибки
            return categories
        raw_data = [raw_data]  # Оборачиваем в список для работы цикла

    # Теперь мы на 100% уверены, что в raw_data лежит список (list)
    for category_data in raw_data:
        if not isinstance(category_data, dict):
            continue

        products_list = []
        for product_data in category_data.get("products", []):
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products_list.append(product)

        category = Category(
            name=category_data["name"], description=category_data["description"], products=products_list
        )
        categories.append(category)

    return categories
