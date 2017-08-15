#!/usr/bin/python39
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

    __engine =  None
    __session = None
    metadata = MetaData()
    def __init__(self):
        """drop all tables if the environment variable HBNB_ENV is equal to test"""
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        self.__engine = create_engine("mysql+mysqldb://" +
                                      os.environ["HBNB_MYSQL_USER"] + ":" +
                                      os.environ["HBNB_MYSQL_PWD"] + "@" +
                                      os.environ["HBNB_MYSQL_HOST"] + "/" +
                                      os.environ["HBNB_MYSQL_DB"])
        try:
            if os.environ['HBNB_MYSQL_ENV'] == "test":
                Base.metadata.drop_all(self.__engine)
        except KeyError:
            pass

    myclasses = ["User", "State", "City", "Amenity", "Place", "Review"]
    def all(self, cls=None):
        """returns private attribute: __objects"""
        search = {}

        print(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if cls is None:
            for cls_name in self.myclasses:
                que = self.__session.query(eval(cls_name))
                
        else:
            if cls not in self.myclasses:
                return
            for query in self.__session.query(eval(cls)):
                search[query.id] = query

        return search

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)
        """

        try:
            self.__session.commit()
        except:
            self.__session.rollback()
        finally:
            self.__session.close()
 
    def reload(self):
        """create all tables in the database (feature of SQLAlchemy)
        (WARNING: all classes who inherit from Base must be imported
        before calling Base.metadata.create_all(engine))
        create the current database session (self.__session) from the engine (self.__engine)
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine))
        
    def delete(self, obj=None):
        """delete from the current database session obj if not None
        """
        if obj is None:
            return
        self.__session.delete(obj)
