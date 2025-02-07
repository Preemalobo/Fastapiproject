#Declarative base is a base template for tables
from sqlalchemy import Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

#Base as a blueprint that helps SQLAlchemy understand what tables look like.
Base=declarative_base()

class User(Base):
    __tablename__="user"
    id:int=Column(Integer,primary_key=True,index=True)
    name:str=Column(String(50),index=True)
    age:str=Column(Integer)
    email:str = Column(String(50), unique=True, index=True)
    password:str=Column(String(50))
