#!/usr/bin/python3
import os
from models.engine import file_storage
from models.engine import db_storage
from models.base_model import BaseModel
from models.amenity import Amenity, PlaceAmenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

CNC = file_storage.FileStorage.CNC
try:
    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        storage = db_storage.DBStorage()
        storage.reload()
    else:
        storage = file_storage.FileStorage()
        storage.reload()
except:
    """CNC - dictionary = { Class Name (string) : Class Type }\
"""

    storage = db_storage.DBStorage()
    storage.reload()
    pass
