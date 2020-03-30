#!/usr/bin/python3
"""lists all State objects, and corresponding City
 objects, contained in the database hbtn_0e_101_usa
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    New_session = Session()
    query = New_session.query(City).order_by(City.id)
    cities_list = query.all()
    for x in cities_list:
        print("{}: {} -> {}".format(x.id, x.name, x.state.name))

    New_session.close()
