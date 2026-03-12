# app/models/product.py

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):

    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    products = relationship("Product", back_populates="category")


class Product(Base):

    __tablename__ = "products"

    id = Column(Integer, primary_key=True)

    name = Column(String, nullable=False)

    price = Column(Float, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))

    category = relationship("Category", back_populates="products")
