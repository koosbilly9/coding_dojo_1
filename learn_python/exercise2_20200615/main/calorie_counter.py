from sqlalchemy import create_engine, Column, Integer, String, Numeric
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class foodTab(Base):

    __tablename__ = "food"

    id = Column('id', Integer, primary_key=True)
    name = Column('name', String)
    calories = Column('calories', Integer)


class db_handeling():
    def get_sqlite_inMem_session():
        Engine = create_engine('sqlite:///:memory:', echo=True)
        Base.metadata.create_all(bind=Engine)
        Session = sessionmaker(Engine)()
        return Session

    def insert_food(food_item) -> "return something":
        db_session = db_handeling.get_sqlite_inMem_session()

        print(db_session.query(foodTab).count())

        new_food = foodTab()
        new_food.id = db_session.query(foodTab).count() + 1
        new_food.name = food_item

        db_session.add(new_food)
        db_session.commit()
        db_session.close

        return food_item

    def get_food(food):
        return food

if __name__ == '__main__':
    db_handeling.insert_food('apple')
    db_handeling.insert_food('pear')
    db_handeling.insert_food('pine')