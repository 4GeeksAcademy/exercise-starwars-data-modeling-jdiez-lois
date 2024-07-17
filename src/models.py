import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum, Float, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    skin_color = Column(String(50))
    hair_color = Column(String(50))
    eye_color = Column(String(50))
    birth_year = Column(String(50))
    genre = Column(Enum('male', 'female'))
    description = Column(String(2000))

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    model_name = Column(String(250), nullable=False, unique=True)
    class_name = Column(String(200))
    manufacturer = Column(String(200))
    cost = Column(String(200))
    length = Column(Float)
    crew = Column(Integer)
    passengers = Column(Integer)
    velocity = Column(Integer)
    capacity = Column(Integer)
    consumable = Column(Integer)
    description = Column(String(2000))

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False, unique=True)
    weather = Column(String(200))
    diameter = Column(Integer)
    gravity = Column(Integer)
    population = Column(Integer)
    terrain = Column(String(250))
    water_surface = Column(Integer)
    description = Column(String(2000))

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(300), nullable=False)
    last_name = Column(String(300), nullable=False)
    subscription_date = Column(Date, nullable=False)
    email = Column(String(300), nullable=False, unique=True)
    password = Column(String(80), nullable=False)

class Favourites(Base):
    __tablename__ = 'favourites'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    character_id = Column(Integer, ForeignKey('characters.id'), primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'), primary_key=True)
    planet_id = Column(Integer, ForeignKey('planets.id'), primary_key=True)
    
    user = relationship('User')
    character = relationship('Characters')
    vehicle = relationship('Vehicles')
    planet = relationship('Planets')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
