#!/usr/bin/python3
"""
City Class from Models Module
"""

from models.base_model import BaseModel


class City(BaseModel):
    """City class handles all application cities"""
    
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship('Place', backref="cities")

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
