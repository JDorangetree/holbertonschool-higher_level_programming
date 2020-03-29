#!/usr/bin/python3
"""lscript that deletes all State objects with
 a name containing the letter a from the
  database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    New_session = Session()
    query = New_session.query(State).filter(State.name.like("%a%"))
    states_list = query.all()
    for state in states_list:
        New_session.delete(state)

    New_session.commit()
    New_session.close()
