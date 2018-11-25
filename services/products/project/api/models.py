# services/products/project/api/models.py

from project import db


class Product(db.Model):

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    stock = db.Column(db.Integer(), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    trademark = db.Column(db.String(128), nullable=False)
    category = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'stock': self.stock,
            'price': self.price,
            'trademark': self.trademark,
            'category': self.category,
            'active': self.active
        }

    def __init__(self, name, stock, price, trademark, category):
        self.name = name
        self.stock = stock
        self.price = price
        self.trademark = trademark
        self.category = category
