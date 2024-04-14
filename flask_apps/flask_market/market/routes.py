from flask import render_template
from  market import app
from market.models import Item

@app.route("/", strict_slashes=False)
@app.route("/home", strict_slashes=False)
def home_route():
    """ Print Hello HBNB! on the browser """
    return render_template('home.html')

@app.route('/items', strict_slashes=False)
def items_route():
    items = Item.query.all()
    return render_template("items.html", items_info=items)
