from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import declarative_base, sessionmaker, relationship



Base = declarative_base()

class Category(Base):
    """ Модель категории. """
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

class Product(Base):
    """ Модель товара. """
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    img_url = Column(String)
    price = Column(DECIMAL(8, 2))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category")
