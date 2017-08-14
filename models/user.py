#!/usr/bin/python3
"""
User Class from Models Module
"""

from models.base_model import BaseModel


class User(BaseModel):
    """User class handles all application users"""

    __tablename__ = 'users'
    email = Column(String(128),nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship('Place'. backref='user')
    reviews = relationship('Review', backref='user')

    def __init__(self, *args, **kwargs):
        """instantiates a new user"""
        super().__init__(self, *args, **kwargs)
