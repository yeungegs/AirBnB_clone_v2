#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class Amenity(BaseModel):
    """Amenity class handles all application amenities"""
    
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("PlaceAmenity", backref="amenities")

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)


class PlaceAmenity(BaseModel, Base):
    """ amenity """

    __tablename__ = 'place_amenities'
    amenity_id = Column(String(50), ForeignKey('amenities.id'))
    place_id = Column(String(50), ForeignKey('place.id'))
