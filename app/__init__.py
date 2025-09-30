"""
Stress Diary Flask Application Package
"""

import os
from flask import Flask
from .models import db, User
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
    
    # Create database tables and admin user
    with app.app_context():
        db.create_all()
        try:
            create_admin_user()
        except Exception as e:
            print(f"⚠️  Warning: Could not create admin user: {str(e)}")
            print("   App will continue without admin user creation.")
    
    return app

def create_admin_user():
    """Create admin user if it doesn't exist."""
    admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_email = os.environ.get('ADMIN_EMAIL', 'admin@stressdiary.com')
    admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123')
    
    try:
        # Check if admin user already exists by username or email
        existing_admin = User.query.filter(
            (User.username == admin_username) | (User.email == admin_email)
        ).first()
        
        if not existing_admin:
            admin_user = User(username=admin_username, email=admin_email)
            admin_user.set_password(admin_password)
            db.session.add(admin_user)
            db.session.commit()
            print(f"✅ Admin user '{admin_username}' created successfully!")
            print(f"   Email: {admin_email}")
            print(f"   Password: {admin_password}")
        else:
            print(f"ℹ️  Admin user already exists (username: {existing_admin.username}, email: {existing_admin.email})")
            
    except Exception as e:
        print(f"⚠️  Error creating admin user: {str(e)}")
        db.session.rollback()
        # Try to continue without failing the app startup
