from src.models import Category


def test_category_init(sample_category: Category) -> None:
    """Проверка корректности инициализации объекта Category."""
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Гаджеты"
    assert len(sample_category.products) == 1


def test_category_counters(sample_category: Category) -> None:
    """Проверка правильности подсчета категорий и продуктов."""
    # Так как фикстура создала одну категорию с одним продуктом:
    assert Category.category_count == 1
    assert Category.product_count == 1
