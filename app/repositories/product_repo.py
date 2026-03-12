# app/repositories/product_repo.py

from sqlalchemy.orm import Session
from app.models.product import Product, Category


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all_products(self):

        return self.db.query(Product).all()

    def get_products_by_category(self, category_id: int):

        return (
            self.db.query(Product)
            .filter(Product.category_id == category_id)
            .all()
        )

    def get_menu_tree(self):

        categories = self.db.query(Category).all()

        menu = []

        for category in categories:

            menu.append(
                {
                    "id": category.id,
                    "name": category.name,
                    "products": [
                        {
                            "id": p.id,
                            "name": p.name,
                            "price": p.price,
                        }
                        for p in category.products
                    ],
                }
            )

        return menu
