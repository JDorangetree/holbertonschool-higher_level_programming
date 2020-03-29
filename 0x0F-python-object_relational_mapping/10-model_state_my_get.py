#!/usr/bin/python3
"""lscript that prints the State object with
 the name passed as argument from the database
  hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    find_state = sys.argv[4]
    Session = sessionmaker(bind=engine)
    New_session = Session()
    query = New_session.query(State).filter(State.name == find_state)
    state_found = query.all()
    if state_found:
        print(state_found[0].id)
    else:
        print("Not found")

    New_session.close()
