

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# with app.app_context():
# 	db.create_all()

class Item(db.Model):
    """Class that describe an Item"""
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=False, unique=True)
    
    def __repr__(self):
        """Representation function"""
        return f'Item {self.name}'

@app.route("/", strict_slashes=False)
@app.route("/home", strict_slashes=False)
def home_route():
    """ Print Hello HBNB! on the browser """
    return render_template('home.html')

@app.route('/items', strict_slashes=False)
def items_route():
    items = Item.query.all()
    return render_template("items.html", items_info=items)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
