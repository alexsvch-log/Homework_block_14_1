from pathlib import Path

from src.models import Category, Product, ProductIterator
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

    # Блок из задания 15.1
    # -----------------------------------
    print(str(product1))
    print(str(product2))
    print(str(product3))
    # -----------------------------------

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Блок из задания 15.1
    # -----------------------------------
    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
    # -----------------------------------

    # Блок из задания 15.2 (Итератор)
    # -----------------------------------
    print("\n--- Проверка итератора товаров ---")
    iterator = ProductIterator(category1)

    for prod in iterator:
        print(f"Товар из итератора: {prod.name}, цена: {prod.price} руб.")
    # -----------------------------------

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

    # --- ЧАСТЬ 2: Загрузка данных о товарах и категориях из файла JSON и проверка счетчиков. ---
    print("--- Загрузка данных из JSON ---")

    # Сбрасываем счетчики перед загрузкой из файла, чтобы они не суммировались с ЧАСТЬЮ 1
    Category.category_count = 0
    Category.product_count = 0

    # Вызываем функцию, которая загружает и обрабатывает данные из json-файла
    loaded_categories = create_objects_from_json(json_path)

    # Выводим результат загрузки
    for cat in loaded_categories:
        # Так как cat.products возвращает строку, где товары разделены переносом строки '\n',
        # мы можем легко узнать количество товаров, посчитав количество строк через .count('\n') + 1.
        # Если товаров вдруг нет (строка пустая), количество будет 0.
        product_count_in_cat = cat.products.count("\n") + 1 if cat.products else 0

        print(f"Категория: {cat.name} ({product_count_in_cat} шт. товаров)")
        print(f"Товары:\n{cat.products}")  # Добавили \n для красивого вывода в столбик

    # Печатаем итог напрямую из класса Category
    print(f"\n Итог из JSON: Категорий - {Category.category_count}, Товаров - {Category.product_count}")
