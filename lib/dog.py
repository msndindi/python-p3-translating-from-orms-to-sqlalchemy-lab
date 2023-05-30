from models import Dog

## Don't need "if __name__ == '__main__':" this time, but leaving it in for later reference##
if __name__ == '__main__':
    ## Don't need "engine = create_engine('sqlite:///dog.db')" this time, (BECAUSE THEY PUT IT IN THE TESTS???) but leaving it in for later reference##
    engine = create_engine('sqlite:///dog.db')
    base.metadata.create_all(engine)
	## Don't need Session this time, (BECAUSE THEY PUT IT IN THE TESTS???) but leaving it in for later reference##
    Session = sessionmaker(bind=engine)
	## Don't need session this time, (BECAUSE THEY PUT IT IN THE TESTS???) but leaving it in for later reference##
    session = Session()

def create_table(base, engine):
    ## Don't need "engine = create_engine('sqlite:///dog.db')" this time, (BECAUSE THEY PUT IT IN THE TESTS???) but commenting it below for later reference##
    # engine = create_engine('sqlite:///dog.db')
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()