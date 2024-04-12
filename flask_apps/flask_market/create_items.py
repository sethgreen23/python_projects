from app import app, db, Item
with app.app_context():
   db.create_all()
   item = Item(name="Samsung Tablet", price=4000, barcode="123456789789", description="Samsung Tablet that rocks")
   db.session.add(item)
   db.session.commit()
   Item.query.all()
