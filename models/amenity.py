#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

class Amenity(BaseModel, Base):
    """Amenity class handles all application amenities"""

    if os.environ['HBNB_TYPE_STORAGE'] == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("PlaceAmenity", backref="amenities")
    else:
        name=""
        
    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)

