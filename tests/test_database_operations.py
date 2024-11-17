import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import init_db
from models import Product, Category  # Импорты ваших моделей

@pytest.fixture
def db_session():
    """Фикстура для создания временной базы данных и сессии."""
    # Создаем временную базу данных в памяти
    engine = create_engine("sqlite:///:memory:")
    init_db(engine)  # Инициализация схемы базы данных
    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # Передаем сессию в тест

    session.close()


def test_database_operations(db_session):
    """Тест CRUD операций с базой данных."""
    # Создаем категорию
    category = Category(name="Тестовая категория")
    db_session.add(category)
    db_session.commit()

    # Проверяем, что категория добавлена
    saved_category = db_session.query(Category).filter_by(
        name='Тестовая категория'
    ).first()
    assert saved_category is not None
    assert saved_category.name == 'Тестовая категория'

    # Создаем продукт в этой категории
    product = Product(
        name='Тестовый продукт',
        description='Описание тестового продукта',
        price=35.50,
        img_url='https://example.com/example.jpg',
        category_id=saved_category.id
    )
    db_session.add(product)
    db_session.commit()

    # Проверяем, что продукт добавлен
    saved_product = db_session.query(Product).filter_by(
        name='Тестовый продукт'
    ).first()
    assert saved_product is not None
    assert saved_product.name == 'Тестовый продукт'
    assert saved_product.category_id == saved_category.id

    # Удаляем продукт
    db_session.delete(saved_product)
    db_session.commit()

    # Проверяем, что продукт удален
    deleted_product = db_session.query(Product).filter_by(
        name='Тестовый продукт'
    ).first()
    assert deleted_product is None
