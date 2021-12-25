#!/usr/bin/python3
"""
contains the class definition of a State and an instance
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, create_engine


Base = declarative_base()


class State(Base):
    """ Represents the table 'states' as a python class """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
