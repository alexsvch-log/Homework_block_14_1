from .base_product import BaseProduct  # Наш новый абстрактный дедушка
from .base_storage import BaseStorage  # Наш новый абстрактный класс
from .category import Category
from .lawn_grass import LawnGrass
from .order import Order  # Наш новый класс заказов
from .print_mixin import PrintMixin  # Наш новый миксин для логирования
from .product import Product
from .product_iterator import ProductIterator
from .smartphone import Smartphone

"""Пакет моделей для импорта категорий и продуктов.
Позволяет в main.py или файлах тестов писать короткий импорт
'from models import Product' вместо длинного 'from models.product import Product'.
Здесь сразу видно, какие классы экспортируются из пакета."""
