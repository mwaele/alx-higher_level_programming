#!/usr/bin/python3
"""
script that changes the name of a State object from the
database hbtn_0e_6_usa
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
    q = session.query(State)
    q = q.filter(State.id == 2)
    r = q.one()
    r.name = "New Mexico"
    session.flush()
    session.commit()
    session.close()
