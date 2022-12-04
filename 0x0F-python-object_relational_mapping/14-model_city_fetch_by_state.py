#!/usr/bin/python3
"""
contains the class definition of a City.
"""
if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
    import sqlalchemy
    from sqlalchemy.orm import sessionmaker
    from sys import argv
    from sqlalchemy import join
    from sqlalchemy.sql import select
    from sqlalchemy import create_engine

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                           argv[2], argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    session = Session()
    for city in session.query(City).join(State).order_by(City.id).all():
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))
    session.close()
