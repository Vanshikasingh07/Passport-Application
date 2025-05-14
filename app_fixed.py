import os
from flask import Flask

from models import db
from views_fixed import views  # Import the fixed Blueprint

app = Flask(__name__)  # Define the app object first

# Use absolute path for SQLite database URI
db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'instance', 'passport_application.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()  # Create tables in the database

# Register the Blueprint
app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True)
