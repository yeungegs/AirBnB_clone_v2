#!/usr/bin/python3
"""
Review Class from Models Module
"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class Review(BaseModel, Base):
    """Review class handles all application reviews"""

    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024),nullable=False)

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
