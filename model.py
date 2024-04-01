from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

# Define Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False) 
    image_data = db.Column(db.LargeBinary, nullable=True)
    image_filename = db.Column(db.String(255), nullable=False)  

    def __repr__(self):
        return f'<Product {self.name}>'
     



def init_db(app: Flask):
    db.init_app(app)
