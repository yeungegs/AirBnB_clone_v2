#!/usr/bin/python3
import os
from models.engine import file_storage
from models.engine import db_storage
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place, PlaceAmenity
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy import MetaData

CNC = file_storage.FileStorage.CNC
DNC = db_storage.DBStorage.DNC
if os.getenv('HBNB_TYPE_STORAGE', 'fs') == 'db':
    storage = db_storage.DBStorage()
    storage.reload()
else:
    storage = file_storage.FileStorage()
    storage.reload()
