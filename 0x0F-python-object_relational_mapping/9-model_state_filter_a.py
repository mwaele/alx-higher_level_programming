#!/usr/bin/python3
"""
lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    from model_state import Base, State
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    for state in session.query(State).order_by(State.id).all():
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))
    session.close()
