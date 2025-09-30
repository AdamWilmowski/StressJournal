"""
Stress Diary Flask Application Package
"""

import os
from flask import Flask
from .models import db
from .blueprints.auth import auth
from .blueprints.main import main
from .blueprints.events import events
from .blueprints.analysis import analysis

def create_app():
    """Application factory pattern."""
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    
    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-this-in-production')
    
    # Database configuration - use PostgreSQL on Heroku, SQLite locally
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        # Heroku PostgreSQL
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    else:
        # Local SQLite
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stress_diary.db'
    
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize extensions
    db.init_app(app)
    
    # Register blueprints
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(main, url_prefix='/')
    app.register_blueprint(events, url_prefix='/')
    app.register_blueprint(analysis, url_prefix='/')
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app
