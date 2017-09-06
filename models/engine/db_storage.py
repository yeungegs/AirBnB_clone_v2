#!/usr/bin/python3
"""setup ORM so storage engine to use SQLAlchemy
"""
import os
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models import base_model, amenity, city, place, review, state, user
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.user import User
from models.state import State
from models.review import Review
from models.city import City
from models.amenity import Amenity
from models.place import Place, PlaceAmenity
from models.engine.file_storage import FileStorage


class DBStorage:
    """docstring
    """

    DNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    __engine = None
    __session = None

    def __init__(self):
        """drop all tables if the environment variable
        HBNB_ENV is equal to test"""

        self.__engine = create_engine("mysql+mysqldb://" +
                                      os.getenv('HBNB_MYSQL_USER') + ":" +
                                      os.getenv('HBNB_MYSQL_PWD') + "@" +
                                      os.getenv('HBNB_MYSQL_HOST') + "/" +
                                      os.getenv('HBNB_MYSQL_DB'))
        if os.getenv('HBNB_MYSQL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """returns private attribute: __objects"""
        myclasses = ["User", "State", "City", "Amenity", "Place", "Review"]
        search = {}
        # Session = sessionmaker(bind=self.__engine)
        # self.__session = Session()
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

        if cls is None:
            '''for cls_name in myclasses:'''
            '''for query in self.__session.query(eval(cls_name)):
                    print (query)
                    search[query.__dict__[id]] = query'''
            for cls_name in myclasses:
                for query in self.__session.query(eval(cls_name)):
                    search[query.id] = query
        else:
            for query in self.__session.query(eval(cls)):
                search[query.id] = query

        return search

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be imported
        before calling Base.metadata.create_all(engine))
        create the current database session (self.__session)
        from the engine (self.__engine)
        """
        Base.metadata.create_all(self.__engine)
        """Session = sessionmaker(bind=self.__engine)"""
        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj is None:
            return
        self.__session.delete(obj)

    def close(self):
        self.__session.remove()
