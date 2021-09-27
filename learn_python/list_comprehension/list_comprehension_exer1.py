from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import json

engine = create_engine('sqlite:///:memory:', echo=True)
session = sessionmaker(engine)()

session.execute('create table users ( username VARCHAR not null,'
                'userid INTEGER not null ,'
                'active VARCHAR, '
                'PRIMARY KEY(userid) )')
session.commit

session.execute("insert into users (username, userid, active) values ('koos', 1, null) ")
session.commit

resultproxy = session.execute("select * from users ")
session.close

a, d = [], {}

d = {column:value for row in resultproxy for column, value in row.items()}


print(d)
y = json.loads(json.dumps(d))
print(json.dumps(d))
print(y)
print(type(json.dumps(d)))
print(type(d))







