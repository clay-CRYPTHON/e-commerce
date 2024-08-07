from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(25), unique=True)
    first_name = Column(String(25))
    last_name = Column(String(25))
    email = Column(String(25), unique=True)
    password = Column(Text, nullable=True)
    is_staff = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    orders = relationship('Order', back_populates='user')

    def __repr__(self):
        return f'<user {self.username}>'


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), unique=True)
    price = Column(Integer)
    # stars_given = Column(Integer, nullable=False, default=1)
    description = Column(Text)

    def __repr__(self):
        return f'<user {self.name}>'


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')
    product_id = Column(Integer, ForeignKey('products.id'))
    product = relationship('Product', back_populates='orders')
    quantity = Column(Integer)
    price = Column(Integer)

    def __repr__(self):
        return f'<user {self.id}>'


class ReviewComment(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    comment = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='orders')
    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship('Order', back_populates='reviews')


