from sqlalchemy.engine import Engine
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import Base


class Connection:
    def __init__(self) -> None:
        self.engine: Engine = create_engine('sqlite:///db/app_database.db', echo=True)

    def create_database(self) -> None:
        print('CREATE DATABASE')
        Base.metadata.create_all(bind=self.engine)