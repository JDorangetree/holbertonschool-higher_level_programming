#!/usr/bin/python3
"""ladds the State object “Louisiana” to the database
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

    Session = sessionmaker(bind=engine)
    New_session = Session()
    query = New_session.query(State).order_by(State.id)
    state_to_add = State(name="Louisiana")
    New_session.add(state_to_add)
    New_session.commit()
    print(state_to_add.id)

    New_session.close()
