import sys
import os
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Restaurant(Base):
    __tablename__ = 'restaurant'
    name = Column(String(250), nullable = False)
    id = Column(Integer, primary_key = True)
class menuItem(Base):
    __tablename__ = 'menu_item'
    name = Column(String(80),nullable = False)
    id = Column(Integer, primary_key = True)
    course = Column(String(250))
    price = Column(String(8))
    description = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    @property
    def serialize(self):
        return{
            'name':self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.coruse,
        }
 




###insert at the end of file ###
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.create_all(engine)
