#!/usr/bin/python3
"""lists all State objects that contain the
 letter a from the database hbtn_0e_6_usa
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
    query = New_session.query(State).order_by(State.id)
    states_list = query.all()
    for state in states_list:
        x = state.name.find("a")
        if x == -1:
            pass
        else:
            print("{}: {}".format(state.id, state.name))

    New_session.close()
