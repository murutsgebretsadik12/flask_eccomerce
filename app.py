from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import  init_db, db

# Create a Flask app instance
app = Flask(__name__)
app.config.from_pyfile('config.py')

init_db(app)  # Initialize the database

migrate = Migrate(app, db)



# Define a route for the root URL

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



if __name__ == '__main__':
    app.run(debug=True)
