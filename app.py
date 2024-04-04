from flask import Flask, render_template,redirect, url_for, request, flash, send_file
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import  db,init_db,Product,User 
from config import Config
from flask_login import LoginManager, current_user,login_user, logout_user, login_required
import os
from io import BytesIO

# Create a Flask app instance
app = Flask(__name__)
app.config.from_object(Config)


init_db(app) # Initialize the database

migrate = Migrate(app, db)

# After initializing your app and database
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'contact'


# Define a user loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



# Define a route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/product')
def product():
    # Query all images from the database
    products = Product.query.limit(3).all()
    return render_template('product.html',products=products)

@app.route('/popular')
def popular():
    return render_template('popular.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')



def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

# add product to database

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

# update product
@app.route('/admin/update_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def update_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form.get('name')
        product.description = request.form.get('description')
        product.price = request.form.get('price')
        # Handle image update if necessary
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('display_admin_images'))
    return render_template('admin/update_product.html', product=product)


# delet product
@app.route('/admin/delete_product/<int:product_id>', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('display_admin_images'))



# to display images in admin page
@app.route('/admin/images')
def display_admin_images():
    # Query all images from the database
    images = Product.query.all()
    return render_template('admin/image.html', images=images)  


# to retrive image from database
@app.route('/image/<int:product_id>')
def serve_image(product_id):
    product=Product.query.get_or_404(product_id)
    if not product.image_data:
        return 'No image found', 404
    return send_file(BytesIO(product.image_data), mimetype= 'image/png')


@app.route('/save_contact', methods=['POST'])
def save_contact():
    if request.method =='POST':
        # Retrieve from data
        username=request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username already exists
        existing_contact = User.query.filter_by(username=username).first()
        if existing_contact:
            flash('Username already exists. Please choose a different username.', 'error')
            return redirect(url_for('register'))
        
        # create a new User instance
        new_user = User(username=username, email=email, password_hash=password)
        new_user.set_password(password)# Hash the password

        # Add new user to the database
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the home page or elsewhere after saving
        return redirect(url_for('index'))
     
@app.route('/login_contact', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        flash('Invalid email or password')
    return render_template('contact.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
