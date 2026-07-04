import pytest

from src.models import Category, Product


@pytest.fixture
def sample_product() -> Product:
    """Фикстура для создания тестового продукта."""
    return Product("Тестовый телефон", "Описание", 1000.0, 10)


@pytest.fixture
def sample_category(sample_product: Product) -> Category:
    """Фикстура для создания тестовой категории."""
    # Важно: сбрасываем счетчики перед каждым тестом
    Category.category_count = 0
    Category.product_count = 0
    return Category("Электроника", "Гаджеты", [sample_product])


@pytest.fixture
def mock_json_list() -> list[dict]:
    """Сокращенные тестовые данные в формате СПИСКА категорий."""
    return [
        {
            "name": "Смартфоны",
            "description": "Гаджеты",
            "products": [
                {"name": "Iphone 15", "description": "512GB", "price": 210000.0, "quantity": 8},
                {"name": "Xiaomi", "description": "1024GB", "price": 31000.0, "quantity": 14},
            ],
        },
        {
            "name": "Телевизоры",
            "description": "ТВ",
            "products": [{"name": '55" QLED 4K', "description": "4K", "price": 123000.0, "quantity": 7}],
        },
    ]


@pytest.fixture
def mock_json_dict() -> dict:
    """Сокращенные тестовые данные в формате одиночного СЛОВАРЯ."""
    return {
        "name": "Смартфоны",
        "description": "Гаджеты",
        "products": [{"name": "Iphone 15", "description": "512GB", "price": 210000.0, "quantity": 8}],
    }
