import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    password = Column(String(50))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    density = Column(String(80), nullable=False)
    climate = Column(String(80), nullable=False)
    gravity = Column(String(80), nullable=False)


class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    height = Column(String(50),  nullable=False)
    

class FavPlanet(Base):
    __tablename__ = 'favPlanet'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship(User)
    planet = relationship(Planet)


class FavPersonaje(Base):
    __tablename__ = 'favPersonaje'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey('user.id'))
    personaje_id = Column(Integer, ForeignKey('personaje.id'))
    user = relationship(User)
    personaje = relationship(Personaje)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')