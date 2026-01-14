def test_task_init(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_task_init(category_1):
    assert category_1.name == "Смартфоны"
    assert category_1.description =="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert len(category_1.products) == 2
    assert category_1.category_count == 1