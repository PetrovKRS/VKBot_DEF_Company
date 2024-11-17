import pytest
from models import Session, Category, Product

@pytest.fixture
def db_session():
    """ Создаём временную БД для тестов. """
    session = Session()
    session.query(Product).delete()
    session.query(Category).delete()
    session.commit()
    yield session
    session.close()

def test_database_operations(db_session):
    """ Проверяем создание и чтение категорий и товаров. """

    # Создание категории
    category = Category(name="Торты")
    db_session.add(category)
    db_session.commit()

    # Проверка, что категория создалась
    assert db_session.query(Category).count() == 1

    # Добавление товара
    product = Product(
        name="Шоколадный торт",
        description="Вкусный торт",
        price=500,
        img_url="http://example.com/image.jpg",
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()

    # Проверка, что товар добавлен и связан с категорией
    assert db_session.query(Product).count() == 1
    assert db_session.query(Product).first().category_id == category.id
