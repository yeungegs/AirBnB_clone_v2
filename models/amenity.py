#!/usr/bin/python3
"""
Amenity Class from Models Module
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class handles all application amenities"""
    
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("PlaceAmenity", backref="amenities")

    def __init__(self, *args, **kwargs):
        """instantiates a new amenity"""
        super().__init__(self, *args, **kwargs)
