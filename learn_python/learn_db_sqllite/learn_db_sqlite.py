import unittest

from sqlalchemy import create_engine, engine, Column, Integer, String,  ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)

def get_engine_sqllite_in_mem():
    sqlite_engine = create_engine('sqlite:///:memory:', echo=True) # echo=True sql dump when engien is used
    return sqlite_engine

def get_engine_sqllite_in_file():
    sqlite_engine = create_engine('sqlite:///user.db', echo=True) # echo=True sql dump when engien is used
    return sqlite_engine

def get_session_sqlite_file():
    sqlite_engine = get_engine_sqllite_in_file()
    Base.metadata.create_all(bind=sqlite_engine)
    Session = sessionmaker(bind=sqlite_engine)  # session factory bind to a engine
    session = Session()  # a session from the factory
    return session

def add_user_in_mem():
    sqlite_engine = get_engine_sqllite_in_mem()
    Base.metadata.create_all(bind=sqlite_engine)
    Session = sessionmaker(bind=sqlite_engine)  # session factory bind to a engine
    session = Session()  # a session from the factory
    user = User()
    user.id = 0
    user.username = "Alice"
    session.add(user)
    session.commit()
    session.close

def show_user_in_file():
    session = get_session_sqlite_file()
    users = session.query(User).all()
    for user in users:
        print(f"{user.id} : {user.username}")

    session.close
    pass

def get_last_id_in_file():
    pass
    session = get_session_sqlite_file()
    users = session.query(User).all()

def find_user_in_file():
    session = get_session_sqlite_file()
    users = session.query(User).all()

def add_user_in_file():
    session = get_session_sqlite_file()
    user = User()
    user.id = 0
    user.username = "Alice"
    session.add(user)
    session.commit()
    session.close

add_user_in_mem()
#add_user_in_file()
show_user_in_file()


class test_sqlalchemy_10min(unittest.TestCase):
    def test_connect_sqlite_in_memory(self):
        self.assertIsInstance(get_engine_sqllite_in_mem(),
                              engine.base.Engine,
                              "Get engine for sqllite in memory instance")

    def test_Person_class(self):
        pass
