import pytest
from src.product_and_category import Product, Category
from src.sub_product import Smartphone, LawnGrass


@pytest.fixture()
def product_1():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture()
def product_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture()
def product_3():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture()
def category_1(product_1, product_2, product_3):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения"
        "дополнительных функций для удобства жизни",
        products=[product_1, product_2, product_3],
    )


@pytest.fixture()
def smartphone1():
    return Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
        efficiency=95.5,
        model="S23 Ultra",
        memory=256,
        color="Серый",
    )


@pytest.fixture()
def smartphone2():
    return Smartphone(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8,
        efficiency=98.2,
        model="15",
        memory=512,
        color="Gray space",
    )


@pytest.fixture()
def smartphone3():
    return Smartphone(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
        efficiency=90.3,
        model="Note 11",
        memory=1024,
        color="Синий",
    )


@pytest.fixture()
def grass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture()
def grass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")
