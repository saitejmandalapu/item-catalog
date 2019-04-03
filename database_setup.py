import sys

import os

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship, backref

from sqlalchemy import create_engine

Base = declarative_base()

# class to store owner information


class Owner(Base):
    __tablename__ = "owner"

    id = Column(Integer, primary_key=True)
    owner_name = Column(String(250), nullable=False)
    owner_email = Column(String(250), nullable=False)
    owner_picture = Column(String(250))


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    owner_id = Column(Integer, ForeignKey("owner.id"))
    owner = relationship(Owner)

    @property
    def serialize(self):
        """Return object data in  easily seriazible format"""
        return {
           "name": self.name,
           "id": self.id
           }
# class to store shoe database


class Item_Details(Base):
    __tablename__ = "item_details"
    id = Column(Integer, primary_key=True)
    brandname = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    image = Column(String(450), nullable=False)
    color = Column(String(250))
    price = Column(String(250))
    description = Column(String(250), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"))
    category = relationship(Category)
    ownerid = Column(Integer, ForeignKey("owner.id"))
    owner = relationship(Owner)
    # We added this serialize function to be
    # able to send JSON objects in a serializable format

    @property
    def serialize(self):
        return {
              "id": self.id,
              "brandname": self.brandname,
              "model": self.model,
              "image": self.image,
              "color": self.color,
              "price": self.price,
              "description": self.description,
              "category_id": self.category_id
             }


engine = create_engine("sqlite:///shoeland.db")
Base.metadata.create_all(engine)
