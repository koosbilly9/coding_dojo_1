from flask import Flask, jsonify, request
from sqlalchemy import create_engine, engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine_sqlite_inMem = create_engine('sqlite:///:memory:',echo=True)

x = 0 # only for testing

class User(Base):
    __tablename__ = "person"

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)


def get_db_session(db_engine=engine_sqlite_inMem):
    session_factory = sessionmaker(bind=db_engine)
    Base.metadata.create_all(bind=db_engine)
    session = session_factory()
    return session

def insert_sqlite_inMem():
    db_session = get_db_session(engine_sqlite_inMem)

    user = User()
    user.id = 0
    user.username = 'koos'
    db_session.add(user)
    db_session.commit()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(response1='Hello World')

@app.route('/inMem/get_user/<name>' , methods = ['GET', 'POST'])
def inMem_get_user(name):
    db_session = get_db_session(engine_sqlite_inMem)
    users = db_session.query(User).all()
    if request.method == 'GET':
        for user in users:
            if user.username == name :
                print(f"{user.id} : {user.username}")
                user_name = user.username
                user_id = user.id

        db_session.close
        return jsonify({'name':user_name, 'id':user_id})

    elif request.method == 'POST':
        user = User()
        user.id = x + 1
        user.username = name
        db_session.add(user)
        db_session.commit()
        db_session.close

        return jsonify({'name': user.username, 'id': user.id, 'status': 'insert done'})
        

if __name__ == '__main__':
    insert_sqlite_inMem()
    app.run(port=50012)