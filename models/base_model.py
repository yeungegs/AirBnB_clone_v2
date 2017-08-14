#!/usr/bin/python3
"""
BaseModel Class of Models Module
"""

import json
import models
from uuid import uuid4, UUID
from datetime import datetime

now = datetime.now
strptime = datetime.strptime

Base = declarative_base()



class BaseModel:
    """attributes and functions for BaseModel class"""

    """Note! BaseModel does /not/ inherit from Base. 
    All other classes will inherit from BaseModel to get common values
    (id, created_at, updated_at), where inheriting from Base will actually
    cause SQLAlchemy to attempt to map it to a table.
    """

    """Add or replace in the class BaseModel:
    class attribute id
    - represents a column containing a unique string (60 characters)
    - can't be null
    - primary key
    """
    id = Column(String(60), nullable=False, primary_key=True)

    """Add or replace in the class BaseModel:
    class attribute created_at
    - represents a column containing a datetime
    - can't be null
    - default value is the current datetime (use datetime.utcnow())
    """
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    """Add or replace in the class BaseModel:
    class attribute updated_at
    - represents a column containing a datetime
    - can't be null
    - default value is the current datetime (use datetime.utcnow())
    """
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """instantiation of new BaseModel Class
        manage kwargs to create instance attribute from this dictionary.
        Ex: kwargs={ 'name': "California" } => self.name = "California"
        """
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = now()

    def __set_attributes(self, d):
        """converts kwargs values to python class attributes"""
        if 'id' not in d:
            d['id'] = str(uuid4())
        if 'created_at' not in d:n
            d['created_at'] = now()
        elif not isinstance(d['created_at'], datetime):
            d['created_at'] = strptime(d['created_at'], "%Y-%m-%d %H:%M:%S.%f")
        if 'updated_at' in d:
            if not isinstance(d['updated_at'], datetime):
                d['updated_at'] = strptime(d['updated_at'],
                                           "%Y-%m-%d %H:%M:%S.%f")
        if '__class__' in d:
            d.pop('__class__')
        self.__dict__ = d
        models.storage.new(self)

    def __is_serializable(self, obj_v):
        """checks if object is serializable"""
        try:
            nada = json.dumps(obj_v)
            return True
        except:
            return False

    def bm_update(self, name, value):
        """updates instance with name and value"""
        setattr(self, name, value)
        self.save()

    def save(self):
        """updates attribute updated_at to current time
        Move the models.storage.new(self) from def __init__(self, *args, **kwargs)
        to def save(self): and call it just before models.storage.save()
        """
        self.updated_at = now()
        models.storage.new(self)
        models.storage.save()

    def to_json(self):
        """returns json representation of self"""
        bm_dict = {}
        for k, v in (self.__dict__).items():
            if (self.__is_serializable(v)):
                bm_dict[k] = v
            else:
                bm_dict[k] = str(v)
        bm_dict["__class__"] = type(self).__name__
        return(bm_dict)

    def __str__(self):
        """returns string type representation of object instance"""
        cname = type(self).__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dict__)

    def delete(self):
        models.storage.delete(self.id)

