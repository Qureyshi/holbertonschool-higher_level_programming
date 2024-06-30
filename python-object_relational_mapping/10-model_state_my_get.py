#!/usr/bin/python3
"""
Sql alchemy
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db_name = sys.argv[3]
    srch_state = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(usr, pwd, db_name))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(State.name == srch_state).first()

    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()
