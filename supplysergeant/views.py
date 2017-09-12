import datetime
import mistune
from flask import render_template, abort

from . import app
from .database import session, Item


@app.route("/", methods=["GET","POST"])
@app.route("/page/<int:page>", methods=["GET","POST"])
@app.route("/?limit=<int:per_page>", methods=["GET","POST"])
@app.route("/page/<int:page>?limit=<int:per_page>", methods=["GET","POST"])
def items(page=1):
    # Zero-indexed page
    page_index = page - 1

    if request.args.get('limit'):
        per_page = request.args.get('limit', type=int)  # if limit is added to the url
    else:
        per_page = 10  # default

    count = session.query(Item).count()

    if per_page > count:
        per_page = count

    start = page_index * per_page
    end = start + per_page

    total_pages = (count - 1) // per_page + 1
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
        total_pages=total_pages,
        per_page=per_page
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
