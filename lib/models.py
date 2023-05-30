#!/usr/bin/env python3

## Don't need PrimaryKeyConstraint this time, but leaving it in for later reference##
from sqlalchemy import (PrimaryKeyConstraint, Column, String, Integer)
from sqlalchemy.ext.declarative import declarative_base
## Don't need sessionmaker this time, (BECAUSE THEY PUT IT IN THE TESTS???) but leaving it in for later reference##
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Dog(Base):
    __tablename__ = "dogs"

    # Index('index_name', 'name')  ## Don't need it this time ##

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    breed = Column(String())

    ## Not needed, but useful to have humans able to read the data ##
    def __repr__(self):
        return f"Dog ID: {self.id} " \
            + f"Dog Name: {self.name} " \
            + f"Dog Breed: {self.breed}"



