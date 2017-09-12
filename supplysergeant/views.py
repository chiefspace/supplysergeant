import datetime
import mistune
from flask import render_template, abort

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
    

@app.route("/item/add", methods=["GET"])
def add_item_get():
    return render_template("add_item.html")

from flask import request, redirect, url_for

@app.route("/item/add", methods=["POST"])
def add_item_post():
    item = Item(
        item_name=request.form["item_name"],
        assignee_name=request.form["assignee_name"],
        item_description=request.form["item_description"],
        item_cost=request.form["item_cost"],
        date_assigned=datetime.datetime.today()
    )
    session.add(item)
    session.commit()
    return redirect(url_for("items"))
    
    
@app.route("/item/<int:item_id>")
def single_item(item_id):
    item = session.query(Item).filter(Item.id == item_id).first()
    return render_template("single_item.html", item=item)
    
    
@app.route("/item/<int:item_id>/edit", methods=["GET"])
def edit_item_get(item_id):
    item = session.query(Item).get(item_id)

    return render_template("edit_item.html", item=item)


@app.route("/item/<int:item_id>/edit", methods=["POST"])
def edit_item_item(item_id):
    if request.method == "POST":
        item = session.query(Item).get(item_id)
        item.item_name = request.form["item_name"],
        item.item_description = mistune.markdown(request.form["item_description"])
        session.add(item)
        session.commit()
        return redirect(url_for("items"))
        
@app.route("/item/<int:item_id>/delete", methods=["GET", "POST"])
def delete_item_get(item_id=1):
    item = session.query(Item).get(item_id)

    if item is None:
        abort(404)
    return render_template("delete_item.html", item=item)


@app.route("/delete/confirmation/<int:item_id>", methods=["GET"])
def delete_item_confirmed(item_id):
    item = session.query(Item).get(item_id)
    if item is None:
        abort(404)
    session.delete(item)
    session.commit()
    return render_template("delete_confirmation.html")
