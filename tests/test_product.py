from unittest.mock import patch

from src.models import Product


def test_product_init(sample_product: Product) -> None:
    """Проверка корректности инициализации объекта Product."""
    assert sample_product.name == "Тестовый телефон"
    assert sample_product.description == "Описание"
    assert sample_product.price == 1000.0
    assert sample_product.quantity == 10
    # Ошибка TypeError: Product.__init__() missing 1 required positional argument: 'description' произошла потому,
    # что в последней строчке теста была попытка создать объект Product, но ему не передали аргумент description:
    # Ошибка тут: переданы только name, price и quantity
    # Product(name='Тестовый телефон', price=1000.0, quantity=10)
    # Вспоминаем конструктор класса: def __init__(self, name, description, price, quantity).
    # Он строго требует все 4 параметра. Без описания Python просто отказывается создавать объект.
    # По умолчанию Python сравнивает объекты по их адресу в памяти. Для него sample_product (созданный в фикстуре)
    # и новый Product(...) (созданный прямо в строке assert) — это двf абсолютно разных товара, даже если у них внутри
    # одинаковые надписи.
    # Как можно исправить:
    # Вариант 1. Проверить текстовое представление (Самый простой путь, что и делаем).
    # Вариант 2. Научить Python сравнивать объекты через __eq__.
    assert repr(sample_product) == "Product(name='Тестовый телефон', price=1000.0, quantity=10)"

    # Если добавить его в src/models/product.py:python    def __eq__(self, other):
    #         if not isinstance(other, Product):
    #             return False
    #         # Продукты равны, если у них совпадают имя, описание, цена и количество
    #         return (self.name == other.name and
    #                 self.description == other.description and
    #                 self.price == other.price and
    #                 self.quantity == other.quantity)
    # Тогда  проверка в тесте (с добавленным описанием!)
    # сработает идеально:
    #     assert sample_product == Product("Тестовый телефон", "Описание", 1000.0, 10)


def test_product_new_product() -> None:
    """Проверка фабричного класс-метода new_product."""
    product_data = {"name": "Новый телефон", "description": "256GB", "price": 50000.0, "quantity": 3}
    prod = Product.new_product(product_data)

    assert prod.name == "Новый телефон"
    assert prod.description == "256GB"
    assert prod.price == 50000.0
    assert prod.quantity == 3


def test_product_price_setter_normal(sample_product: Product) -> None:
    """Проверка обычного повышения цены через сеттер."""
    sample_product.price = 1200.0
    assert sample_product.price == 1200.0


def test_product_price_setter_negative(sample_product: Product) -> None:
    """Проверка защиты от отрицательной и нулевой цены."""
    sample_product.price = -100.0
    assert sample_product.price == 1000.0  # Цена не должна измениться

    sample_product.price = 0
    assert sample_product.price == 1000.0  # Цена не должна измениться


def test_product_price_setter_decrease_confirm(sample_product: Product) -> None:
    """Проверка снижения цены при согласии пользователя (ввод 'y')."""
    # Имитируем ввод пользователя 'y' через patch
    with patch("builtins.input", return_value="y"):
        sample_product.price = 800.0

    assert sample_product.price == 800.0  # Цена успешно снизилась


def test_product_price_setter_decrease_reject(sample_product: Product) -> None:
    """Проверка отмены снижения цены при отказе пользователя (ввод 'n')."""
    # Имитируем ввод пользователя 'n'
    with patch("builtins.input", return_value="n"):
        sample_product.price = 800.0

    assert sample_product.price == 1000.0  # Цена осталась прежней


def test_new_product_with_duplicate(sample_product: Product) -> None:
    """Проверка работы new_product при обнаружении дубликата в списке."""
    # sample_product из фикстуры имеет: name="Тестовый телефон", price=1000.0, quantity=10
    current_products = [sample_product]

    # Передаем данные дубликата с БОЛЬШЕЙ ценой
    duplicate_data = {"name": "Тестовый телефон", "description": "Новое описание", "price": 1500.0, "quantity": 5}

    # Вызываем метод класса, передавая список для проверки
    result = Product.new_product(duplicate_data, current_products)

    # Метод должен вернуть тот же самый объект из списка
    assert result is sample_product
    # Количество должно сложиться: 10 + 5 = 15
    assert result.quantity == 15
    # Цена должна измениться на более высокую: 1500.0
    assert result.price == 1500.0


def test_new_product_no_duplicate(sample_product: Product) -> None:
    """Проверка работы new_product, когда список передан, но дубликата в нем нет."""
    # В списке лежит только "Тестовый телефон"
    current_products = [sample_product]

    # Передаем данные совершенно другого товара
    new_product_data = {"name": "Другой телефон", "description": "Описание", "price": 5000.0, "quantity": 2}

    result = Product.new_product(new_product_data, current_products)

    # Метод должен вернуть НОВЫЙ объект, а не старый из списка
    assert result is not sample_product
    assert result.name == "Другой телефон"
    assert result.price == 5000.0
    assert result.quantity == 2

    # Старый товар в списке должен остаться нетронутым
    assert sample_product.quantity == 10
    assert sample_product.price == 1000.0
