import os

from sqlalchemy import (Boolean, Column, create_engine, Integer, String,
                        ForeignKey, Table)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

BASE = declarative_base()

association = Table('association', BASE.metadata,
                    Column('room_id', Integer, ForeignKey('room.id')),
                    Column('person_id', Integer, ForeignKey('person.id')))


class Room(BASE):
    """Create Room Schema"""
    __tablename__ = 'room'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(225), nullable=False)
    room_mates = relationship('Person',
                              secondary=association,
                              backref='room',
                              order_by=id)
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'room',
        'polymorphic_on': type
    }


class office_space(Room):
    '''office space schema'''
    __tablename__ = 'office_space'
    id = Column(Integer, ForeignKey('room.id'), primary_key=True)
    capacity = Column(Integer, default=4)

    __mapper_args__ = {
        'polymorphic_identity': 'office_space',
    }


class living_space(Room):
    '''living space schema'''
    __tablename__ = 'living_space'
    id = Column(Integer, ForeignKey('room.id'), primary_key=True)
    capacity = Column(Integer, default=6)

    __mapper_args__ = {
        'polymorphic_identity': 'living_space',
    }


class Person(BASE):
    """Person Schema"""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=True)
    nationality = Column(String(10), nullable=True)
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }


class Fellow(Person):
    '''Fellow Schema'''
    __tablename__ = 'fellow'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)
    wants_accomodation = Column(String(50), default='Y')

    __mapper_args__ = {
        'polymorphic_identity': 'fellow'
    }


class Staff(Person):
    '''staff Schema'''
    __tablename__ = 'staff'
    id = Column(Integer, ForeignKey('person.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'staff'
    }


class Database():

    def __init__(self, database=None):
        self.db_name = None
        self.session = None
        self.engine = None

    def create(self, db_name):
        self.db_name = db_name
        self._create_engine(self.db_name)
        self._create_session()
        return self

    def read(self, db_name):
        self.db_name = db_name
        self._create_engine(self.db_name)
        self._create_session()

    def clear(self):
        connection = self.engine.connect()
        connection = connection.begin()
        for table in reversed(BASE.metadata.sorted_tables):
            connection.execute(table.delete())
        connection.commit()

    def save(self):
        self.session.commit()
        self.session.close()

    def drop(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            print("{}.db has been deleted!".format(self.db_name))

    def _create_engine(self, db_name):
        self.engine = create_engine('sqlite:///' + db_name + '.db')
        BASE.metadata.create_all(self.engine)
        return self

    def _create_session(self):
        session = sessionmaker(bind=self.engine)
        self.session = session()
