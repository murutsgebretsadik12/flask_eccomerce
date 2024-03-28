from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from model import  init_db, db

# Create a Flask app instance
app = Flask(__name__)
app.config.from_pyfile('config.py')

init_db(app)  # Initialize the database

migrate = Migrate(app, db)


# Define a route for the root URL
@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
