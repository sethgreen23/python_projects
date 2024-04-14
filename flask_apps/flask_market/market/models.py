from market import db

class Item(db.Model):
    """Class that describe an Item"""
    __tablename__ = "item"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    price = db.Column(db.Integer, nullable=False)
    barcode = db.Column(db.String(120), nullable=False, unique=True)
    description = db.Column(db.String(1024), nullable=False, unique=True)
    
    def __repr__(self):
        """Representation function"""
        return f'Item {self.name}'
