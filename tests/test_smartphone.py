from src.models import Smartphone


def test_smartphone_init() -> None:
    """Проверка корректной инициализации объекта Smartphone."""
    phone = Smartphone("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый")
    assert phone.name == "Samsung Galaxy S23 Ultra"
    assert phone.price == 180000.0
    assert phone.quantity == 5
    assert phone.efficiency == 95.5
    assert phone.model == "S23 Ultra"
    assert phone.memory == 256
    assert phone.color == "Серый"
