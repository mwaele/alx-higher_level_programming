#!/usr/bin/python3
"""script that prints the first State object from the database
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
    firstt = session.query(State).order_by(State.id).first()
    if firstt:
        print("{}: {}".format(firstt.id, firstt.name))
    else:
        print("Nothing")
    session.close()
