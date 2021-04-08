#!/usr/bin/python3
'''define a class State'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    '''this class inherits from SqlAlchemy Base'''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
