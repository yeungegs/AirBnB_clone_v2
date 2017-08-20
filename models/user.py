#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os


class User(BaseModel, Base):
    """User class handles all application users"""


    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship('Place', cascade="all, delete", backref='user')
    reviews = relationship('Review', cascade="all, delete", backref='user')


    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
