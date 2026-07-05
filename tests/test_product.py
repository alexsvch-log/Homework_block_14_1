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
