from pcs_database.common import get_connection_string_from_alias
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os
os.chdir("..")
os.environ["HOME"] = os.getcwd()
os.environ["TWO_TASK"] = "tdipsp92_tdipsp92.w9.bmw.za"

def get_session_for_db_alias(dbuser_alias='IVS_SEL'):
    engine = create_engine(get_connection_string_from_alias(dbuser_alias), echo=False)
    scoped_session_factory = sessionmaker(bind=engine)
    session = scoped_session_factory()
    return session

def get_standort() -> "dictonary":

    sql_string = """
    select * from standort 
    """

    session = get_session_for_db_alias("IVS_SEL")

    resultproxy = session.execute(sql_string)
    session.close()
    # convert result to dictionary

    a = [{column: value for column, value in rowproxy.items()} for rowproxy in resultproxy]

    print(f"{a}")

    return f"{a}"

if __name__ == '__main__':
    get_standort()