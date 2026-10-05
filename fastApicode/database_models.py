from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()

class product(Base):

    __tablename__ ="product"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    description= Column(String)
    price= Column(Float)
    quantity= Column(Integer)

    