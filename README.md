# Проект учета товаров в интернет-магазине (Блоки 14.1, 14.2, 15.1)

Модули для бэкенд-приложение на Python для управления категориями товаров и автоматического ведения складского учета с использованием объектно-ориентированного программирования (ООП).

## Содержание
- [Требования](#требования)
- [Настройка окружения и зависимостей](#настройка-окружения-и-зависимостей)
- [Инструменты разработки (Linting)](#инструменты-разработки-linting)
- [Использование](#использование)
- [Логгирование (logging)](#логгирование-logging)
- [Тестирование и покрытие (Coverage)](#тестирование-и-покрытие-coverage)
- [Документация](#документация)
- [Лицензия](#лицензия)


### Требования
Для запуска и разработки проекта вам понадобятся:

* **Python 3.14+** (проект использует современные возможности типизации)
* **Poetry** — инструмент для управления зависимостями и виртуальными окружениями.

### Настройка окружения и зависимостей
Управление зависимостями осуществляется через Poetry (без использования requirements.txt).

**1. Клонирование репозитория**
```bash
git clone https://github.com/alexsvch-log/homework_block_14_1.git
```
**2. Установка зависимостей**

```bash
poetry install
```
**3. Запуск и активация окружения**

Активация виртуального окружения: 
```bash
poetry shell
```
Запуск скриптов напрямую:
```bash
poetry run python main.py
```

### Инструменты разработки (Linting)
В проекте настроена автоматическая проверка качества кода (`black`, `flake8`, `mypy`). Все конфигурации линтеров объединены в файле `pyproject.toml`.

**1. Установка инструментов:**
```bash
poetry install --with lint
```
**2. Быстрый запуск всех проверок (Windows):**
```bash
.\lint
```

## Использование

Пакет разработан как бэкенд-сервис для интеграции с веб-интерфейсом (фронтендом). Параметры (наполнение интернет-магазина товаром) передаются с фронтенда в виде JSON-пакета.

**Запуск приложения (Точка входа):**
```bash
poetry run python main.py
```

При запуске `main.py` последовательно отрабатывают два аналитических блока:

1. **Исходный код задания:** Инициализация объектов и ручная проверка счетчиков классов.
2. **Данные из файла JSON:** Загрузка данных о товарах и категориях из файла JSON и проверка счетчиков.

### Как запустить

Убедитесь, что вы находитесь в корневой директории проекта, и выполните команду в терминале:

```bash
python main.py
```

### Документация функций

Детальное описание параметров доступно внутри docstrings каждого модуля. Краткая карта функций проекта:

| Модуль                      | Функция / Атрибут              | Назначение                                                                                                          |
|:----------------------------|:-------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| **models.base_product**     | `BaseProduct`                  | **[Абстрактный класс]** Дедушка всех товаров. Фиксирует обязательные методы для продуктов.                          |                                                                                                                                         |
| **models.base_storage**     | `BaseStorage`                  | **[Абстрактный класс]** Общий родитель для категорий и заказов. Хранит и типизирует имя.                            |                                                                                                                                                    |
| **models.print_mixin**      | `PrintMixin`                   | **[Класс-миксин]** Примесь для автоматического логирования и печати инфо о создаваемых объектах.                    |                                                                                                                                                                                                                                                         |
| **models.category**         | `Category`                     | Класс для представления категории. Наследуется от `BaseStorage`.                                                    |
| **models.category**         | `Category.__init__()`          | Настраивает объект категории и автоматически запускает подсчет глобальных счетчиков.                                |
| **models.category**         | `Category.category_count`      | Переменная уровня класса. Счетчик общего количества созданных категорий в системе.                                  |
| **models.category**         | `Category.product_count`       | Переменная уровня класса. Счетчик общего количества уникальных товаров во всех категориях.                          |
| **models.category**         | `Category.add_product()`       | Добавляет продукт в приватный список категории с **[Валидацией типа]** (разрешены только Product и его наследники). |
| **models.category**         | `Category.get_products()`      | Возвращает неизменяемый кортеж объектов товаров для безопасной внешней итерации.                                    |
| **models.category**         | `Category.products` (property) | **[Геттер]** Возвращает оптимизированную строку со всеми продуктами в определенном формате.                         |
| **models.category**         | `Category.__str__()`           | **[Магический метод]** Возвращает строку с названием категории и суммой штук всех её товаров.                       |
| **models.category**         | `Category.middle_price()`      | **[Новый метод]** Рассчитывает средний ценник товаров. Обрабатывает **[ZeroDivisionError]** для пустых категорий.   |
| **models.product**          | `Product`                      | Базовый класс товара. Наследуется от **[PrintMixin]** и **[BaseProduct]** одновременно.                             |
| **models.product**          | `Product.__init__()`           | Инициализирует объект товара, заполняя его базовые свойства при создании.                                           |
| **models.product**          | `Product.new_product()`        | **[Класс-метод]** Создает товар из словаря с проверкой на дубликаты на складе.                                      |
| **models.product**          | `Product.price` (property)     | **[Геттер]** Для безопасного чтения приватной цены снаружи (для реализации контроля цен).                           |
| **models.product**          | `Product.price` (setter)       | **[Сеттер]** Для валидации цены и интерактивного подтверждения её снижения.                                         |
| **models.product**          | `Product.__repr__()`           | **[Магический метод]** Возвращает понятное техническое представление товара внутри списков.                         |
| **models.product**          | `Product.__str__()`            | **[Магический метод]** Возвращает пользовательское строковое представление товара по шаблону ТЗ.                    |
| **models.product**          | `Product.__add__()`            | **[Магический метод]** Складывает два товара **[Строго одного класса]**, возвращая общую стоимость на складе.       |
| **models.product_iterator** | `ProductIterator`              | **[Вспомогательный класс]** Позволяет перебирать товары одной категории в цикле `for`.                              |
| **models.product_iterator** | `ProductIterator.__init__()`   | Принимает объект категории и сохраняет защищенный кортеж товаров для перебора.                                      |
| **models.product_iterator** | `ProductIterator.__iter__()`   | **[Магический метод]** Подготавливает и возвращает сам объект-итератор для цикла.                                   |
| **models.product_iterator** | `ProductIterator.__next__()`   | **[Магический метод]** Поочередно выдает очередной объект товара или останавливает цикл.                            |
| **models.order**            | `Order`                        | **[Новый класс]** Представление заказа на один товар. Наследуется от **[BaseStorage]**.                             |                                |                                                                                                                     |
| **models.smartphone**       | `Smartphone`                   | **[Класс-наследник]** Представление смартфона с уникальными свойствами (модель, память, цвет, производительность).  |
| **models.lawn_grass**       | `LawnGrass`                    | **[Класс-наследник]** Представление газонной травы с уникальными свойствами (страна, цвет, срок прорастания).       |                            |                                |                                                                                                                  |
| **readers**                 | `reader_json`                  | Безопасно считывает JSON-файл и возвращает его содержимое в исходном виде словаря.                                  |
| **readers**                 | `create_objects_from_json`     | Основная утилита. Парсит данные из `reader_json` и собирает их в готовые списки объектов `Category` и `Product`.    |
### Пример запуска
## Пример использования в коде (`src/main.py`)

Этот скрипт демонстрирует ручное создание номенклатуры и автоматическую потоковую загрузку данных из внешнего JSON-файла.

```text
from pathlib import Path
from src.models import Category, Product, ProductIterator, Smartphone, LawnGrass
from src.readers import create_objects_from_json

if __name__ == "__main__":
    print("=======Запущен Блок 17.1 Часть 1 Проверка на ошибку=======")
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт"
            " с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    print("=======Зкончен Блок 17.1 Часть 1 Проверка на ошибку=======")
    # --- ЧАСТЬ 1: Исходный код задания. Реализация работы с приватным атрибутом Category.products. ---
    # ---Реализация классов-наследников класса Product Smartphone и LawnGrass
    
    # Создание smartphone1, smartphone2, smartphone3
    
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

    # Создание grass1, grass2

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
        category_smartphones.add_product("Not a product")
    except TypeError:
        print("Возникла ошибка TypeError при добавлении не продукта")
    else:
        print("Не возникла ошибка TypeError при добавлении не продукта")

    # Создание исходных продуктов
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Проверка пользовательского строкового отображения продуктов (__str__)
    print(str(product1))
    print(str(product2))
    print(str(product3))

    # Инициализация категории товаров
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Проверка строкового отображения категории (__str__)
    print(str(category1))

    # Вывод списка товаров через оптимизированный геттер
    print(category1.products)

    # Проверка сложения полной стоимости товаров на складе (__add__)
    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    # Проверка работы вспомогательного класса-итератора (ProductIterator)
    print("\n--- Проверка итератора товаров ---")
    iterator = ProductIterator(category1)

    for prod in iterator:
        print(f"Товар из итератора: {prod.name}, цена: {prod.price} руб.")

    # Добавление нового продукта и проверка обновления счетчиков
    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)
    
    # Создание товара через фабричный класс-метод из словаря
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет...",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    
    # Проверка работы сеттера цены (валидация на понижение и отрицательные значения)
    new_product.price = 800  # Вызовет интерактивное подтверждение в консоли
    new_product.price = -100 # Выведет ошибку валидации
    new_product.price = 0    # Выведет ошибку валидации
    
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
        
    print("=======Запущен Блок 17.1 Часть 2 Расчет среднего значения=======")
    # 1. Считаем среднюю цену в заполненной категории смартфонов (созданной в Части 1)
    print(f"Средняя цена в категории Смартфоны: {category1.middle_price()}")

    # 2. Создаем пустую категорию и проверяем защиту от деления на ноль через try-except
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена в пустой категории: {category_empty.middle_price()}")

    print("=======Закончен Блок 17.1 Часть 2 Расчет среднего значения=======")

    # --- ЧАСТЬ 2: Бонусное задание. Загрузка данных о товарах и категориях из файла JSON и проверка счетчиков. ---
    print("--- Загрузка данных из JSON ---")

    # Безопасный расчет пути к файлу в корне проекта через Path
    ROOT_DIR = Path(__file__).resolve().parent.parent
    json_path = ROOT_DIR / "data" / "products.json"

    # Сбрасываем счетчики перед загрузкой из файла, чтобы они не суммировались с ЧАСТЬЮ 1
    Category.category_count = 0
    Category.product_count = 0

    # Вызываем функцию, которая загружает и обрабатывает данные из json-файла
    loaded_categories = create_objects_from_json(json_path)

    # Выводим результат загрузки
    for cat in loaded_categories:
        product_count_in_cat = cat.products.count("\n") + 1 if cat.products else 0
        print(f"Категория: {cat.name} ({product_count_in_cat} шт. товаров)")
        print(f"Товары:\n{cat.products}")
    print(f"\n Итог из JSON: Категорий - {Category.category_count}, Товаров - {Category.product_count}")
    

```

### Ожидаемый вывод в консоли для части 1

```text
=======Запущен Блок 17.1 Часть 1 Проверка на ошибку=======
Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством
=======Зкончен Блок 17.1 Часть 1 Проверка на ошибку=======
Был создан объект класса Product ('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Был создан объект класса Product ('Iphone 15', '512GB, Gray space', 210000.0, 8)
Был создан объект класса Product ('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
=======Запущен Блок 16.1=======
Был создан объект класса Smartphone ('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Был создан объект класса Smartphone ('Iphone 15', '512GB, Gray space', 210000.0, 8)
Был создан объект класса Smartphone ('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5
95.5
S23 Ultra
256
Серый
Iphone 15
512GB, Gray space
210000.0
8
98.2
15
512
Gray space
Xiaomi Redmi Note 11
1024GB, Синий
31000.0
14
90.3
Note 11
1024
Синий
Был создан объект класса LawnGrass ('Газонная трава', 'Элитная трава для газона', 500.0, 20)
Был создан объект класса LawnGrass ('Газонная трава 2', 'Выносливая трава', 450.0, 15)
Газонная трава
Элитная трава для газона
500.0
20
Россия
7 дней
Зеленый
Газонная трава 2
Выносливая трава
450.0
15
США
5 дней
Темно-зеленый
2580000.0
16750.0
Возникла ошибка TypeError при попытке сложения
Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.
Iphone 15, 210000 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.
5
Возникла ошибка TypeError при добавлении не продукта
=======Запущен Блок 15.1=======
Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.
Iphone 15, 210000 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.
=======Отработан Блок 15.1=======
Смартфоны, количество продуктов: 27 шт.
Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.
Iphone 15, 210000 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.
2580000.0
1334000.0
2114000.0
=======Запущен Блок 15.2 (Итератор) =======

--- Проверка итератора товаров ---
Товар из итератора: Samsung Galaxy S23 Ultra, цена: 180000.0 руб.
Товар из итератора: Iphone 15, цена: 210000.0 руб.
Товар из итератора: Xiaomi Redmi Note 11, цена: 31000.0 руб.
=======Отработан Блок 15.1=======
Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.
Iphone 15, 210000 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.
Был создан объект класса Product ('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)
Samsung Galaxy S23 Ultra, 180000 руб. Остаток: 5 шт.
Iphone 15, 210000 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.
55" QLED 4K, 123000 руб. Остаток: 7 шт.
9
Был создан объект класса Product ('Samsung Galaxy S23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Samsung Galaxy S23 Ultra
256GB, Серый цвет, 200MP камера
180000.0
5
Вы уверены, что хотите снизить цену с 180000.0 до 800? (y/n): n
Действие отменено. Цена осталась прежней.
180000.0
Цена не должна быть нулевой или отрицательной
180000.0
Цена не должна быть нулевой или отрицательной
180000.0

--- Проверка создания Заказа ---
Заказ №1: Iphone 15, 2 шт. Итого: 420000.0 руб.
Защита сработала: нельзя оформить заказ на не-товар!
=======Запущен Блок 17.1 Часть 2 Расчет среднего значения=======
Средняя цена в категории Смартфоны: 136000.0
Средняя цена в пустой категории: 0.0
=======Закончен Блок 17.1 Часть 2 Расчет среднего значения=======
--- Загрузка данных из JSON ---
Был создан объект класса Product ('Samsung Galaxy C23 Ultra', '256GB, Серый цвет, 200MP камера', 180000.0, 5)
Был создан объект класса Product ('Iphone 15', '512GB, Gray space', 210000.0, 8)
Был создан объект класса Product ('Xiaomi Redmi Note 11', '1024GB, Синий', 31000.0, 14)
Был создан объект класса Product ('55" QLED 4K', 'Фоновая подсветка', 123000.0, 7)
Категория: Смартфоны (3 шт. товаров)
Товары:
Samsung Galaxy C23 Ultra, 180000 руб. Остаток: 5 шт.
Iphone 15, 210000 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000 руб. Остаток: 14 шт.
Категория: Телевизоры (1 шт. товаров)
Товары:
55" QLED 4K, 123000 руб. Остаток: 7 шт.

 Итог из JSON: Категорий - 2, Товаров - 4

```

## Логгирование (logging)
**В разработке**

## Тестирование и покрытие (Coverage)
Для запуска тестов используется фреймворк `pytest`. Все общие фикстуры вынесены в `tests/conftest.py`.

**1. Запуск всех тестов:**
```bash
poetry run pytest
```

**2. Анализ покрытия кода (Terminal):**
```bash
poetry run pytest --cov=src
```

**3. Генерация подробного HTML-отчета:**
```bash
poetry run pytest --cov=src --cov-report=html
```
*Интерактивный отчет создается в папке `htmlcov/index.html` и показывает каждую не протестированную строку кода.*

## Документация:

Основная информация о работе пакета приведена в текущем файле `README.md`. 

Все модули и функции задокументированы с использованием **Python Docstrings**. Вы можете получить интерактивную справку по любой функции прямо в интерактивной оболочке Python:

```python
from src.readers import create_objects_from_json
help(create_objects_from_json)
```
## Лицензия:
Проект распространяется под лицензией MIT.
