import os
from flask import Flask
from flask_login import LoginManager
from models import db, User
from views_fixed import views  # Import the fixed Blueprint

def create_app():
    app = Flask(__name__)  # Define the app object first

    # Configure the Flask application
    app.config['SECRET_KEY'] = os.urandom(24)  # For session management
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///passport.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    
    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'views.login'
    login_manager.login_message = 'Please log in to access this page.'
    login_manager.login_message_category = 'error'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    with app.app_context():
        # Drop all existing tables and recreate them
        db.drop_all()
        db.create_all()
        print("Database tables created successfully!")

    # Register the Blueprint
    app.register_blueprint(views)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
