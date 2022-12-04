#!/usr/bin/python3
""" List all State objs from database
"""
from model_state import Base, State
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sys import argv
from sqlalchemy import create_engine

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        session.close()
