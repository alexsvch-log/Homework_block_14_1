import json
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock, mock_open, patch

from pytest_mock import MockFixture

from src.models import Category
from src.readers import create_objects_from_json, reader_json

MOCK_SUCCESS_DATA = {"user_currencies": ["USD", "EUR"], "user_stocks": ["AAPL", "AMZN", "GOOGL", "MSFT", "TSLA"]}

# =======================================================================
#   1. ТЕСТИРОВАНИЕ ФУНКЦИИ reader_json
# =======================================================================


# 1. Тест успешного получения списка словарей из json файла
@patch("builtins.open", new_callable=mock_open)
def test_reader_json_success(mock_file: MagicMock) -> None:
    # 1. Превращаем наш словарь в JSON-строку, которую якобы прочитают из файла
    json_string = json.dumps(MOCK_SUCCESS_DATA)
    mock_file.return_value.read.return_value = json_string

    # 2. Передаем в функцию фейковый путь (ведь реальный файл не откроется)
    fake_path = Path("fake_settings.json")
    result = reader_json(fake_path)

    # 3. Проверяем утверждения
    assert result == MOCK_SUCCESS_DATA

    # Проверяем, что встроенный open() вызывался именно с нашим путем и кодировкой
    mock_file.assert_called_once_with(fake_path, encoding="utf-8")


# 2. Тест неудачного получения списка словарей из json файла (там не словарь, а строка)
@patch("builtins.open", new_callable=mock_open)
def test_reader_json_not_dict(mock_file: MagicMock) -> None:
    # 1. Превращаем наш словарь в JSON-строку, которую якобы прочитают из файла
    json_string = json.dumps("1234asd")
    mock_file.return_value.read.return_value = json_string

    # 2. Передаем в функцию фейковый путь (ведь реальный файл не откроется)
    fake_path = Path("fake_settings.json")
    result = reader_json(fake_path)

    # 3. Проверяем утверждения
    assert result == {}

    # Проверяем, что встроенный open() вызывался именно с нашим путем и кодировкой
    mock_file.assert_called_once_with(fake_path, encoding="utf-8")


# 3. Тест неудачного получения списка словарей из json файла (файл сломан или пустой)
@patch("builtins.open", new_callable=mock_open)
def test_reader_json_file_empty_or_broken(mock_file: MagicMock) -> None:
    # Настраиваем чтение файла на выброс ошибки синтаксиса JSON.
    # Передаем обязательные аргументы для JSONDecodeError.
    mock_file.return_value.read.side_effect = json.JSONDecodeError("Expecting value", "broken text", 0)
    # 2. Передаем в функцию фейковый путь (ведь реальный файл не откроется)
    fake_path = Path("fake_settings.json")
    result = reader_json(fake_path)

    # 3. Проверяем утверждения
    assert result == {}
    # Проверяем, что файл всё-таки открывался
    mock_file.assert_called_once_with(fake_path, encoding="utf-8")


# 4. Тест неудачного получения списка словарей из json файла (файл пустой, содержит "")
@patch("builtins.open", new_callable=mock_open)
def test_reader_json_file_empty(mock_file: MagicMock) -> None:
    # Имитируем, что файл успешно открылся, но при чтении вернул пустую строку
    mock_file.return_value.read.return_value = ""

    fake_path = Path("fake_settings.json")
    result = reader_json(fake_path)

    # Функция наткнется на json.JSONDecodeError и должна вернуть {}
    assert result == {}
    mock_file.assert_called_once_with(fake_path, encoding="utf-8")

    # 3. Проверяем утверждения
    assert result == {}
    # Проверяем, что файл всё-таки открывался
    mock_file.assert_called_once_with(fake_path, encoding="utf-8")


# 5. Тест неудачного получения списка словарей из json файла (файл отсутствует)
@patch("builtins.open", new_callable=mock_open)
def test_reader_json_file_bad(mock_file: MagicMock) -> None:

    # Заставляем вызов open() выбросить ошибку отсутствия файла
    mock_file.side_effect = FileNotFoundError("Файл не найден")

    # 2. Передаем в функцию фейковый путь (ведь реальный файл не откроется)
    fake_path = Path("fake_settings.json")
    result = reader_json(fake_path)

    # 3. Проверяем утверждения
    assert result == {}
    mock_file.assert_called_once_with(fake_path, encoding="utf-8")


# =======================================================================
#   2. ТЕСТИРОВАНИЕ ФУНКЦИИ create_objects_from_json
# =======================================================================


def test_create_objects_from_json_with_list(mocker: MockFixture, mock_json_list: dict) -> None:
    """Тест создания объектов: подставляем СПИСОК данных из conftest."""

    # Мокаем чтение файла и отдаем список категорий
    mocker.patch("src.readers.reader_json", return_value=mock_json_list)

    # Сбрасываем счетчики перед тестом
    Category.category_count = 0
    Category.product_count = 0

    # Запускаем функцию с любым фейковым путем
    result = create_objects_from_json(Path("fake_path.json"))

    # Проверяем структуру (в списке должно быть 2 категории)
    assert len(result) == 2
    assert result[0].name == "Смартфоны"
    assert result[1].name == "Телевизоры"

    # Проверяем количество продуктов в первой категории
    assert len(result[0].products) == 2

    # Проверяем итоговые глобальные счетчики классов
    assert Category.category_count == 2
    assert Category.product_count == 3  # 2 смартфона + 1 телевизор


def test_create_objects_from_json_with_dict(mocker: MockFixture, mock_json_dict: dict) -> None:
    """Тест создания объектов: подставляем одиночный СЛОВАРЬ из conftest."""

    # Мокаем чтение файла и отдаем один словарь
    mocker.patch("src.readers.reader_json", return_value=mock_json_dict)

    Category.category_count = 0
    Category.product_count = 0

    result = create_objects_from_json(Path("fake_path.json"))

    # Проверяем, что функция успешно обработала словарь
    assert len(result) == 1
    assert result[0].name == "Смартфоны"
    assert len(result[0].products) == 1

    # Проверяем счетчики
    assert Category.category_count == 1
    assert Category.product_count == 1


def test_create_objects_from_json_empty_dict(mocker: MockFixture) -> None:
    """Тест на передачу пустого СЛОВАРЯ."""
    empty_dict: dict[str, Any] = {}
    mocker.patch("src.readers.reader_json", return_value=empty_dict)
    assert create_objects_from_json(Path("fake_path.json")) == []


def test_create_objects_from_json_not_dict(mocker: MockFixture) -> None:
    """Тест на передачу НЕ СЛОВАРЯ."""
    not_dict: list[Any] = ["123", 15, 45.0]
    mocker.patch("src.readers.reader_json", return_value=not_dict)
    assert create_objects_from_json(Path("fake_path.json")) == []
