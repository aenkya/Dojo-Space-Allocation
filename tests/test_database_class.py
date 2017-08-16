"""
Unit tests for the office_space Class
"""
import unittest
from mock import MagicMock, mock, patch
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


from app.models.database import Database, Person, Room

Base = declarative_base()


class DatabaseClassTest(unittest.TestCase):
    """Testing Database Class"""

    def setUp(self):
        self.db = Database()
        self.person = Person()
        self.room = Room()

    def tearDown(self):
        print('\nend of test', self.shortDescription())

    def test_database_instance(self):
        '''create instance'''
        self.assertIsInstance(
            self.db, Database, msg='The object should be an instance of the `Database` class')

    def test_person_instance(self):
        '''create person instance'''
        self.assertIsInstance(
            self.person, Person, msg='The object should be an instance of the `Person` class')

    def test_room_instance(self):
        '''create room instance'''
        self.assertIsInstance(
            self.room, Room, msg='The object should be an instance of the `Room` class')

    def test_engine_and_session(self):
        '''create engine'''
        database_path = 'sqlite:///dojo.db'
        sqlalchemy = MagicMock()
        sqlalchemy.create_engine = MagicMock(return_value=mock)
        fake_engine = sqlalchemy.create_engine(database_path)

        Base.metadata = MagicMock()
        Base.metadata.create_all = MagicMock()
        Base.metadata.create_all(fake_engine)

        self.db.create('dojo')
        sqlalchemy.orm = MagicMock()
        sqlalchemy.orm.sessionmaker = MagicMock(return_value=mock)
        sqlalchemy.orm.sessionmaker(bind=fake_engine)

        sqlalchemy.create_engine.assert_called_with(database_path)
        sqlalchemy.orm.sessionmaker.assert_called_with(bind=fake_engine)

    def test_read_creates_engine_for_existing_db(self):
        '''read database'''
        existing_path = 'sqlite:///existing_fake_db.db'
        sqlalchemy = MagicMock()
        sqlalchemy.create_engine = MagicMock(return_val=mock)
        fake_engine = sqlalchemy.create_engine(existing_path)

        sqlalchemy.orm = MagicMock()
        sqlalchemy.orm.sessionmaker = MagicMock(return_value=mock)
        sqlalchemy.orm.sessionmaker(bind=fake_engine)

        self.db.read('existing_fake_db')
        sqlalchemy.create_engine.assert_called_with(existing_path)
        sqlalchemy.orm.sessionmaker.assert_called_with(bind=fake_engine)

    @patch('app.models.database.os.path')
    @patch('app.models.database.os')
    def test_drop_delete_an_existing_database(self, mock_os, mock_path):
        '''delete database'''
        fake_file_path = 'files/fake_db.db'
        mock_path.exists.return_value = False
        self.db.drop(fake_file_path)

        self.assertFalse(mock_os.remove.called)

        mock_path.exists.return_value = True
        self.db.drop(fake_file_path)

        mock_os.remove.assert_called_with(fake_file_path)