#!/usr/bin/python3
'''that method update the id 2 with New Mexico value in state table'''

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    myQuery = session.query(State).filter_by(id=2).first()
    myQuery.name = 'New Mexico'

    session.commit()
