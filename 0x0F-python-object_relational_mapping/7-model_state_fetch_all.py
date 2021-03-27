#!/usr/bin/python3
''' this module list all State Objects form the database hbtn'''

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
    sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

Session = sessionmaker(engine)
session = Session()


if __name__ == "__main__":
    Base.metadata.create_all(engine)

    myQuery = session.query(State.id, State.name).all()

    for i in myQuery:
        print('{}: {}'.format(i[0], i[1]))
