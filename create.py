from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

firstRestaurant = Restaurant(name = "Pizza Palace")
session.add(firstRestaurant)
session.commit()
session.query(Restaurant).all()

