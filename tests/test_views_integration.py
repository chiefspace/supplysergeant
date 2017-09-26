import os
import unittest
from urllib.parse import urlparse

from werkzeug.security import generate_password_hash

# Configure your app to use the testing database
os.environ["CONFIG_PATH"] = "supplysergeant.config.TestingConfig"

from supplysergeant import app
from supplysergeant.database import Base, engine, session, User, Item

class TestViews(unittest.TestCase):
    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)


    def test_add_item(self):

        response = self.client.post("/item/add", data={
            "item_name": "Test Item",
            "assignee_name": "Test Assignee",
            "item_description": "Test Item Description",
            "item_cost": 1909.99
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(urlparse(response.location).path, "/")
        items = session.query(Item).all()
        self.assertEqual(len(items), 1)

        item = items[0]
        self.assertEqual(item.item_name, "Test Item")
        self.assertEqual(item.assignee_name, "Test Assignee")
        self.assertEqual(item.item_description, "Test Item Description")
        self.assertEqual(item.item_cost, 1909.99)

    def tearDown(self):
        """ Test teardown """
        session.expunge_all()
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)

if __name__ == "__main__":
    unittest.main()