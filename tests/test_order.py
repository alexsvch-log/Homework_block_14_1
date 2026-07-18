import pytest

from src.models import Order, Product


def test_order_init(sample_product: Product) -> None:
    """Проверка корректной инициализации заказа и подсчета стоимости."""
    # sample_product имеет цену 1000.0 (из твоей стандартной фикстуры)
    order = Order("Заказ №100", sample_product, 3)

    assert order.name == "Заказ №100"
    assert order.product == sample_product
    assert order.quantity == 3
    assert order.total_price == 3000.0  # 1000.0 * 3
    assert str(order) == "Заказ №100: Тестовый телефон, 3 шт. Итого: 3000.0 руб."


def test_order_type_error() -> None:
    """Проверка защитного замка: заказ нельзя оформить на обычную строку."""
    with pytest.raises(TypeError):
        # Передаем строку вместо объекта Product
        _ = Order("Заказ-ошибка", "Не продукт", 5)  # type: ignore
