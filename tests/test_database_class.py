"""
Unit tests for the office_space Class
"""
import unittest
from mock import MagicMock, mock, patch

from models.database import Database, Person, Room


class DatabaseClassTest(unittest.TestCase):
    """Testing Database Class"""

    def setUp(self):
        self.db = Database()
        self.person = Person()
        self.room = Room()

    def test_database_instance(self):
        self.assertIsInstance(
            self.db, Database, msg='The object should be an instance of the `Database` class')

    def test_person_instance(self):
        self.assertIsInstance(
            self.person, Person, msg='The object should be an instance of the `Person` class')

    def test_room_instance(self):
        self.assertIsInstance(
            self.room, Room, msg='The object should be an instance of the `Room` class')

    def test_engine_and_session(self):
        database_path = 'sqlite:///./database/dojo.db'
        sqlalchemy = MagicMock()
        sqlalchemy.create_engine = MagicMock(return_value=mock)
        fake_engine = sqlalchemy.create_engine(database_path)

        Base.metadata = MagicMock()
        Base.metadata.create_all = MagicMock()
        Base.metadata.create_all(fake_engine)

        sqlalchemy.orm = MagicMock()
        sqlalchemy.orm.sessionmaker = MagicMock(return_value=mock)
        sqlalchemy.orm.sessionmaker(bind=fake_engine)

        self.db.create('dojo')
        sqlalchemy.create_engine.assert_called_with(database_path)
        sqlalchemy.orm.sessionmaker.assert_called_with(bind=fake_engine)
