from pathlib import Path

from src.models import Category, LawnGrass, Order, Product, ProductIterator, Smartphone
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

    # Блок из задания 16.1
    # -----------------------------------
    print("=======Запущен Блок 16.1=======")
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)

    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)

    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)

    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)

    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)

    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)

    print(category_smartphones.products)

    print(Category.product_count)

    try:
        # noinspection PyTypeChecker
        category_smartphones.add_product("Not a product")  # type: ignore
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")

        print("=======Отработан Блок 16.1=======")
    # -----------------------------------

    # Блок из задания 15.1
    # -----------------------------------
    print("=======Запущен Блок 15.1=======")
    print(str(product1))
    print(str(product2))
    print(str(product3))
    print("=======Отработан Блок 15.1=======")
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
    print("=======Запущен Блок 15.2 (Итератор) =======")
    print("\n--- Проверка итератора товаров ---")
    iterator = ProductIterator(category1)

    for prod in iterator:
        print(f"Товар из итератора: {prod.name}, цена: {prod.price} руб.")
    print("=======Отработан Блок 15.1=======")
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

    # Блок из задания 16.2 (дополнтельный Заказ)
    # -----------------------------------
    # Блок проверки нового класса Заказ (Order)
    print("\n--- Проверка создания Заказа ---")

    # Создаем заказ №1 на 2 айфона (берем product2 из кода выше)
    order1 = Order("Заказ №1", product2, 2)

    # Печатаем заказ (сработает метод __str__ из Order)
    print(order1)

    # Проверяем защиту: пробуем передать в заказ обычную строку вместо продукта
    try:
        # noinspection PyTypeChecker
        invalid_order = Order("Заказ-ошибка", "Просто строка", 1)  # type: ignore
    except TypeError:
        print("Защита сработала: нельзя оформить заказ на не-товар!")
    # -----------------------------------

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
