from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, DATE
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass
class Foodstuff(Base):
    __tablename__ = 'foodstuffs'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    serving_size = Column(Integer)
    calories = Column(Integer)
    protein = Column(Integer)
    carbs = Column(Integer)
    fiber = Column(Integer)
    fat = Column(Integer)

    def _init__(self, id, description, serving_size, calories, protein, carbs, fiber, fat):
        self.id = id
        self.description = description
        self.serving_size = serving_size
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fiber = fiber
        self.fat = fat


@dataclass
class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    serving_size = Column(Integer)
    user_id = Column(Integer)
    actual_date = Column(DATE)
    entry1 = Column(Integer)
    entry2 = Column(Integer)
    entry3 = Column(Integer)
    entry4 = Column(Integer)
    entry5 = Column(Integer)
    entry6 = Column(Integer)
    entry7 = Column(Integer)
    entry8 = Column(Integer)
    entry9 = Column(Integer)
    entry10 = Column(Integer)
    entry11 = Column(Integer)
    entry12 = Column(Integer)


    def _init__(self, id, description, serving, user_id,  entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12):
        self.id = id
        self.NAME = description
        self.serving = serving
        self.user_id = user_id
        self.entry1 = entry1
        self.entry2 = entry2
        self.entry3 = entry3
        self.entry4 = entry4
        self.entry5 = entry5
        self.entry6 = entry6
        self.entry7 = entry7
        self.entry8 = entry8
        self.entry9 = entry9
        self.entry10 = entry10
        self.entry11 = entry11
        self.entry12 = entry12


@dataclass
class Day(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    email = Column(String)
    password = Column(String)


    def _init__(self, id, user_name, email, password):
        self.id = id
        self.user_name = user_name
        self.email = email
        self.password = password
