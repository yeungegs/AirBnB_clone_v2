#!/usr/bin/python3
"""
State Class from Models Module
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class handles all application states"""
    
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
