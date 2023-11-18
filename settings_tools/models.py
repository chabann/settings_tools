from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  Column, Integer, String, Text, DateTime


class Base(DeclarativeBase): pass

class Note(Base):
    __tablename__ = "notes"
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(20))
    text_body = Column(Text)
    short_body = Column(String(50))
    creation_date = Column(DateTime)
    modify_date = Column(DateTime)