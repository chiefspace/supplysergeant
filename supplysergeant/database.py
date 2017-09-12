import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime, Float

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    email = Column(String(128), unique=True)
    password = Column(String(128))

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    item_name = Column(String(1024))
    assignee_name = Column(String(1024))
    item_description = Column(Text)
    item_cost = Column(Float(precision=2))
    date_assigned = Column(DateTime, default=datetime.datetime.now)

Base.metadata.create_all(engine)