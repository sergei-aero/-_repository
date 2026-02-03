from tests.conftest import product_1, product_2, product_3, category_1


def test_task_product_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_task_category_init(category_1):
    assert category_1.name == "Смартфоны"
    assert (
        category_1.description
        == "Смартфоны, как средство не только коммуникации, но и получения"
        "дополнительных функций для удобства жизни"
    )
    assert len(category_1.product_list) == 3


def test_price_getter_returns_correct_value(product_1):
    """Тест: геттер price возвращает установленное значение цены"""
    # Проверяем, что геттер возвращает правильное значение
    assert product_1.price == 180000.0


def test_price_setter_sets_valid_price(product_1):
    """Тест: сеттер устанавливает корректную положительную цену"""
    product_1.price = 200000.0
    assert product_1.price == 200000.0


def test_price_setter_does_not_set_negative_price(product_1, capsys):
    """Тест: сеттер не устанавливает отрицательную цену и выводит сообщение"""
    original_price = product_1.price
    product_1.price = -500.0
    assert product_1.price == original_price
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_task_product_str(product_1):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_task_category_str(category_1):
    assert str(category_1) == "Смартфоны, количество продуктов: 27 шт."


def test_task_product_add(product_1, product_2, product_3):
    assert product_1 + product_2 == 2580000.0
    assert product_1 + product_3 == 1334000.0
    assert product_2 + product_3 == 2114000.0
