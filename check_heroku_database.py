#!/usr/bin/env python3
"""
Script to check what database Heroku is using and its status.
"""

import os
from app import create_app
from app.models import db, User

def check_database_status():
    """Check database status and configuration."""
    app = create_app()
    
    with app.app_context():
        print("=== Heroku Database Status ===")
        
        # Check database URL
        database_url = os.environ.get('DATABASE_URL')
        if database_url:
            print(f"🔗 Database URL: {database_url[:30]}...")
            if 'postgres' in database_url:
                print("✅ Using PostgreSQL (persistent)")
            else:
                print("⚠️  Using non-PostgreSQL database")
        else:
            print("⚠️  No DATABASE_URL found - using SQLite (ephemeral)")
        
        # Check current database URI
        current_uri = app.config.get('SQLALCHEMY_DATABASE_URI', 'Not set')
        print(f"🔗 Current URI: {current_uri[:30]}...")
        
        # Check if we can connect to database
        try:
            # Try to query users
            user_count = User.query.count()
            print(f"👥 Users in database: {user_count}")
            
            # List all users
            users = User.query.all()
            for user in users:
                print(f"   - {user.username} ({user.email})")
                
        except Exception as e:
            print(f"❌ Database connection error: {str(e)}")
        
        # Check environment variables
        print("\n=== Environment Variables ===")
        print(f"ADMIN_USERNAME: {os.environ.get('ADMIN_USERNAME', 'Not set (default: admin)')}")
        print(f"ADMIN_EMAIL: {os.environ.get('ADMIN_EMAIL', 'Not set (default: admin@stressdiary.com)')}")
        print(f"ADMIN_PASSWORD: {os.environ.get('ADMIN_PASSWORD', 'Not set (default: admin123)')}")

if __name__ == "__main__":
    check_database_status()
