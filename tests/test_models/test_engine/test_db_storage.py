import unittest
import os.path
from os import getenv
from datetime import datetime
from models.base_model import Base
from models.amenity import *
from models.engine.db_storage import DBStorage
from models.state import State
from models import *


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE', 'fs') != 'db', "db")
class Test_DBStorage(unittest.TestCase):
    """Test the database storage class
    """
    @classmethod
    def setUpClass(cls):
        """create a session"""
        storage._DBStorage__session.close()
        cls.test_dbstorage = DBStorage()
        test_args = {'updated_at':
                     datetime.datetime(2017, 8, 16, 21, 51, 33, 669555),
                     'id': "0234",
                     'created_at':
                     datetime.datetime(2017, 8, 16, 21, 53, 26, 563266),
                     'name': 'protoss[<0;73;15M'}
        cls.model = Amenity(**test_args)
        cls.store.reload()
        cls.test_len = 0

    @classmethod
    def tearDownClass(cls):
        cls.test_dbstorage._DBStorage__session.close()
        storage.reload()

    def test_all(self):
        result = self.test_dbstorage.all('Amenity')
        self.assertEqual(len(result), self.test_len)

    def test_all_blank(self):
        result = self.test_dbstorage.all('')
        self.assertEqual(result, [])

    def test_all_user(self):
        result = self.test_dbstorage.all(self, cls=User)
        self.assertEqual(len(result), self.test_len)

    def test_all_state(self):
        result = self.test_dbstorage.all(self, cls=State)
        self.assertEqual(result, [])

    def test_all_city(self):
        result = self.test_dbstorage.all(self, cls=City)
        self.assertEqual(result, [])

    def test_all_amenity(self):
        result = self.test_dbstorage.all(self, cls=Amenity)
        self.assertEqual(len(result), self.test_len)

    def test_all_place(self):
        result = self.test_dbstorage.all(self, cls=Place)
        self.assertEqual(results, [])

    def test_new(self):
        pass

    def test_save(self):
        pass

    def test_reload(self):
        self.test_dbstorage.reload()
        self.assertNotEqual(self.test_dbstorage._DBStorage__session, None)

if __name__ == "__main__":
    unittest.main()
