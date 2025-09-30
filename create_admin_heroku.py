#!/usr/bin/env python3
"""
Script to create admin user on Heroku.
Run this on Heroku console if automatic creation fails.
"""

import os
from app import create_app
from app.models import db, User

def create_admin_on_heroku():
    """Create admin user on Heroku."""
    app = create_app()
    
    with app.app_context():
        print("=== Creating Admin User on Heroku ===")
        
        # Default admin credentials
        admin_username = 'admin'
        admin_email = 'admin@stressdiary.com'
        admin_password = 'admin123'
        
        try:
            # Check if admin user already exists
            existing_admin = User.query.filter(
                (User.username == admin_username) | (User.email == admin_email)
            ).first()
            
            if existing_admin:
                print(f"ℹ️  Admin user already exists:")
                print(f"   Username: {existing_admin.username}")
                print(f"   Email: {existing_admin.email}")
                print(f"   Created: {existing_admin.created_at}")
            else:
                # Create new admin user
                admin_user = User(username=admin_username, email=admin_email)
                admin_user.set_password(admin_password)
                db.session.add(admin_user)
                db.session.commit()
                print(f"✅ Admin user created successfully!")
                print(f"   Username: {admin_username}")
                print(f"   Email: {admin_email}")
                print(f"   Password: {admin_password}")
                
        except Exception as e:
            print(f"❌ Error creating admin user: {str(e)}")
            db.session.rollback()
            return False
            
        return True

if __name__ == "__main__":
    create_admin_on_heroku()
