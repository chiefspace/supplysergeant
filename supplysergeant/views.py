from flask import render_template

from . import app
from .database import session, Item

PAGINATE_BY = 10

@app.route("/")
@app.route("/page/<int:page>")
def items(page=1):
    # Zero-indexed page
    page_index = page - 1

    count = session.query(Item).count()

    start = page_index * PAGINATE_BY
    end = start + PAGINATE_BY

    total_pages = (count - 1) // PAGINATE_BY + 1
    has_next = page_index < total_pages - 1
    has_prev = page_index > 0

    items = session.query(Item)
    items = items.order_by(Item.date_assigned.desc())
    items = items[start:end]

    return render_template("items.html",
        items=items,
        has_next=has_next,
        has_prev=has_prev,
        page=page,
        total_pages=total_pages
    )