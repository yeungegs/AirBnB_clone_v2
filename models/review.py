#!/usr/bin/python3
"""
Review Class from Models Module
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review class handles all application reviews"""

    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024),nullable=False)

    def __init__(self, *args, **kwargs):
        """instantiates a new review"""
        super().__init__(self, *args, **kwargs)
