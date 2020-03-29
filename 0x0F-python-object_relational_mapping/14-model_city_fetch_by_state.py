#!/usr/bin/python3
"""lscript that deletes all State objects with
 a name containing the letter a from the
  database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    from model_city import City
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    New_session = Session()
    my_query = New_session.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id)
    state_city_list = my_query.all()
    for row in state_city_list:
        print("{}: ({}) {}".format(row[0], row[1], row[2]))

    New_session.close()
