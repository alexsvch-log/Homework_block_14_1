from pathlib import Path

from src.models import Category, Product
from src.readers import create_objects_from_json

# 1. Задаем путь к папке data в корне проекта, где лежит файл с данными
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"  # это путь к файлам с данными
json_path = DATA_DIR / "products.json"

# --- ЧАСТЬ 1: Исходный код задания. Инициализация объектов и ручная проверка счетчиков классов.  ---
if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    # --- ЧАСТЬ 2: Загрузка данных о товарах и категориях из файла JSON и проверка счетчиков. ---
    print("--- Загрузка данных из JSON ---")

    # Сбрасываем счетчики перед загрузкой из файла, чтобы они не суммировались с ЧАСТЬЮ 1
    Category.category_count = 0
    Category.product_count = 0

    # Вызываем функцию, которая загружает и обрабатывает данные из json-файла
    loaded_categories = create_objects_from_json(json_path)

    # Переменная для подсчета товаров в живых объектах
    total_products_in_json = 0

    # Благодаря методу __repr__, товары внутри списка выведутся красиво!
    # Выводим результат загрузки
    for cat in loaded_categories:
        print(f"Категория: {cat.name} ({len(cat.products)} шт. товаров)")
        print(f"Товары: {cat.products}")

    # Печатаем итог напрямую из класса Category
    print(f"\n📊 Итог из JSON: Категорий - {Category.category_count}, Товаров - {Category.product_count}")
