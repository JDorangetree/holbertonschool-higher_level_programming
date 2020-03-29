#!/usr/bin/python3
"""lists all State objects from the database hbtn_0e_6_usa
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
    states_list = New_session.query(State).order_by(State.id).all()
    print(states_list)
    for states in states_list:
        print("{}: {}".format(states.id, states.name))

    New_session.close()
