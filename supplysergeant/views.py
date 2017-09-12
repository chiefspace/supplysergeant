from flask import render_template

from . import app
from .database import session, Item

@app.route("/")
def items():
    items = session.query(Item)
    items = items.order_by(Item.datetime.desc())
    items = items.all()
    return render_template("items.html",
        items=items
    )