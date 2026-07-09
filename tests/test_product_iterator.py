import pytest

from src.models import Category, Product, ProductIterator


def test_product_iterator_success(sample_category: Category) -> None:
    """Проверка успешного последовательного перебора товаров через итератор."""
    # sample_category берется из фикстуры, в ней по умолчанию лежит 1 товар
    # Для полноты теста добавим в нее еще один продукт
    new_prod = Product("Второй телефон", "Описание 2", 20000.0, 5)
    sample_category.add_product(new_prod)

    # Создаем наш вспомогательный класс-итератор
    iterator = ProductIterator(sample_category)

    # Собираем все товары из итератора в список через цикл
    result_products = []
    for prod in iterator:
        result_products.append(prod)

    # Проверяем, что итератор вернул ровно 2 товара в правильном порядке
    assert len(result_products) == 2
    assert result_products[0].name == "Тестовый телефон"
    assert result_products[1].name == "Второй телефон"


def test_product_iterator_stop_iteration(sample_category: Category) -> None:
    """Проверка выброса исключения StopIteration, когда элементы закончились."""
    iterator = ProductIterator(sample_category)

    # В категории всего один товар, забираем его вручную через next()
    next(iterator)

    # Следующий вызов next() должен вызвать ошибку StopIteration, так как список пуст
    with pytest.raises(StopIteration):
        next(iterator)
