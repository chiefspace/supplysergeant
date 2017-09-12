import os
import datetime
from flask_script import Manager

from supplysergeant import app

manager = Manager(app)

from supplysergeant.database import session, Item

@manager.command
def seed():
    item_description = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
    item_cost = 1099.99
    date_assigned =  datetime.datetime.now()

    for i in range(25):
        item = Item(
            item_name="Test Item #{}".format(i),
            assignee_name="Test Assignee #{}".format(i),
            item_description=item_description,
            item_cost=item_cost,
            date_assigned=date_assigned
        )
        session.add(item)
    session.commit()

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    manager.run()