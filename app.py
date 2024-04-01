from flask import Flask, render_template,redirect, url_for, request, flash
import os
from werkzeug.utils import secure_filename

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import  db,init_db,Product 
from config import Config

# Create a Flask app instance
app = Flask(__name__)
app.config.from_object(Config)


init_db(app) # Initialize the database

migrate = Migrate(app, db)






# Define a route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    return render_template('product.html')

@app.route('/popular')
def popular():
    return render_template('popular.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/admin/add_product', methods=['GET', 'POST'])
def admin_add_product():
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        image_file = request.files.get('image')

        # Check if product name already exists
        existing_product = Product.query.filter_by(name=name).first()
        if existing_product:
            flash('A product with this name already exists.', 'error')
            return redirect(url_for('admin_add_product'))

        if image_file and allowed_file(image_file.filename):
            filename = secure_filename(image_file.filename)
            image_data = image_file.read()

            new_product = Product(
                name=name,
                description=description,
                price=price,
                image_data=image_data,
                image_filename=filename
            )
            
            try:
                db.session.add(new_product)
                db.session.commit()
                flash('Product added successfully!', 'success')
            except Exception as e:
                db.session.rollback()
                flash('An error occurred. Please try again.', 'error')
                app.logger.error(f"Error adding product: {e}")
        else:
            flash('Invalid file format.', 'error')

    return render_template('admin/add_product.html')

if __name__ == '__main__':
    app.run(debug=True)
