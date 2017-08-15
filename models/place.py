#!/usr/bin/python3
"""
Place Class from Models Module
"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Table, MetaData, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

class Place(BaseModel, Base):
    """Place class handles all application places"""


    metadata = Base.metadata

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = ['', '']
    amenities = relationship('Amenity', secondary='place_amenity', viewonly=False)
    reviews = relationship('Review', backref='place')


    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)



class PlaceAmenity(Base):
    """ place amenity """

    metadata = Base.metadata
        
    __tablename__ = "place_amenity"
    place_id = Column(String(60), ForeignKey('places.id'),
                          primary_key=True, nullable=False)
    amenity_id = Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
