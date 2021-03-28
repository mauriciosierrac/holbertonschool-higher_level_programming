#!/usr/bin/python3

'''that method print the fields of containts char 'a' in state table'''

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    myQuery = session.query(State.id, State.name).filter(
        State.name == sys.argv[4]).all()

    if myQuery:
        for i in myQuery:
            if i.name == sys.argv[4]:
                print('{}'.format(i.id))
    else:
        print('Not Found')
