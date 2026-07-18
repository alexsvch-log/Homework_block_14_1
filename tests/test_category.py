import pytest

from src.models import Category, Product


def test_category_init(sample_category: Category) -> None:
    """Проверка корректности инициализации объекта Category."""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Гаджеты"
    assert "Тестовый телефон" in sample_category.products


def test_category_counters(sample_category: Category) -> None:
    """Проверка правильности подсчета категорий и продуктов."""
    # Так как фикстура создала одну категорию с одним продуктом:
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_category_add_product(sample_category: Category) -> None:
    """Проверка добавления нового продукта в категорию."""
    new_prod = Product("Планшет", "Экран 10 дюймов", 15000.0, 5)

    # Добавляем продукт
    sample_category.add_product(new_prod)

    # Проверяем, что общий счетчик продуктов вырос до 2
    assert Category.product_count == 2
    # Проверяем, что новый товар появился в строке вывода геттера products
    assert "Планшет, 15000 руб. Остаток: 5 шт." in sample_category.products


def test_category_str(sample_category: Category) -> None:
    """Проверка строкового отображения категории с подсчетом суммы штук товаров."""
    # В sample_category лежит один товар в количестве 10 штук
    assert str(sample_category) == "Электроника, количество продуктов: 10 шт."


def test_category_add_product_type_error(sample_category: Category) -> None:
    """Проверка, что метод add_product выбрасывает TypeError при добавлении не-продукта."""
    with pytest.raises(TypeError):
        # Пытаемся добавить обычную строку вместо объекта Product
        sample_category.add_product("Not a product")  # type: ignore


def test_category_middle_price(sample_category: Category) -> None:
    """Проверка корректного расчета средней цены для заполненной категории."""
    # В sample_category из фикстуры уже лежит 1 товар с ценой 1000.0
    # Добавим еще один товар с ценой 5000.0
    another_product = Product("Второй телефон", "Описание", 5000.0, 5)
    sample_category.add_product(another_product)

    # Средняя цена должна быть: (1000.0 + 5000.0) / 2 = 3000.0
    assert sample_category.middle_price() == 3000.0


def test_category_middle_price_empty() -> None:
    """Проверка защиты: для пустой категории метод возвращает 0.0 без ошибок."""
    empty_category = Category("Пустая категория", "Описание", [])

    # Метод должен поймать ZeroDivisionError и безопасно вернуть 0.0
    assert empty_category.middle_price() == 0.0
