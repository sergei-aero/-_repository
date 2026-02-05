import pytest
import json
from src.utils import read_json


def test_read_valid_json_file(tmp_path):
    """Тест чтения корректного JSON файла"""
    test_data = {"key": "value", "number": 123}
    file_path = tmp_path / "test.json"

    with open(file_path, "w", encoding="UTF-8") as f:
        json.dump(test_data, f)

    result = read_json(str(file_path))
    assert result == test_data


def test_file_not_found():
    """Тест обработки отсутствующего файла"""
    with pytest.raises(FileNotFoundError):
        read_json("/non/existent/file.json")


def test_invalid_json_format(tmp_path):
    """Тест обработки некорректного JSON формата"""
    file_path = tmp_path / "invalid.json"

    with open(file_path, "w", encoding="UTF-8") as f:
        f.write("{invalid json}")

    with pytest.raises(json.JSONDecodeError):
        read_json(str(file_path))
