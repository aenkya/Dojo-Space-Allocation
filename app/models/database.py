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
    capacity = Column(String(225), nullable=False)
    room_mates = relationship('Person',
                              secondary=association,
                              backref='room',
                              order_by=id)


class Person(BASE):
    """Person Schema"""
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(250), nullable=False)
    gender = Column(String(20), nullable=True)
    nationality = Column(String(10), nullable=True)

    __mapper_args__ = {
        'polymorphic_identity': 'person',
        'polymorphic_on': type
    }


class Fellow(Person):
    '''Fellow Schema'''
    __tablename__ = 'fellow'


class Database:

    def __init__(self, database=None):
        if database:
            self.database = database
            if '.sqlite' not in self.database:
                self.database += '.sqlite'
        else:
            self.database = 'dojo.sqlite'
        self.engine = create_engine('sqlite:///' + self.database)
        session = sessionmaker(bind=self.engine)
        self.session = session()
        BASE.metadata.create_all(self.engine)

    def clear(self):
        connection = self.engine.connect()
        connection = connection.begin()
        for table in reversed(BASE.metadata.sorted_tables):
            connection.execute(table.delete())
        connection.commit()

    def save(self):
        self.session.commit()
        self.session.close()
