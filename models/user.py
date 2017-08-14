#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

class User(BaseModel):
    """User class handles all application users"""

    __tablename__ = 'users'
    email = Column(String(128),nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship('Place', backref='user')
    reviews = relationship('Review', backref='user')

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
