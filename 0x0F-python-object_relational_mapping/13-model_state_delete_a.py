#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
"""
if __name__ == '__main__':
    from model_state import Base, State
    from sys import argv
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    for state in session.query(State).order_by(State.id).all():
        if 'a' in state.name:
            r = session.query(State).filter(State.name.contains('a'))
            r.delete(synchronize_session=False)
            session.flush()
            session.commit()
            session.close()
    session.close()
