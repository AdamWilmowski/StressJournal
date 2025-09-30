#!/usr/bin/env python3
"""
Quick script to set admin password immediately.
Use this as a workaround until PostgreSQL is added.
"""

import os
import sys
from app import create_app
from app.models import db, User

def set_password_immediately():
    """Set admin password immediately."""
    app = create_app()
    
    with app.app_context():
        print("=== Set Admin Password Now ===")
        
        # Get admin username
        admin_username = input("Admin username (default: admin): ").strip() or "admin"
        
        # Get new password
        new_password = input("Enter new password: ").strip()
        if not new_password:
            print("❌ Password cannot be empty!")
            return False
        
        try:
            # Find or create admin user
            admin_user = User.query.filter_by(username=admin_username).first()
            if not admin_user:
                # Create new admin user
                admin_user = User(username=admin_username, email='admin@stressdiary.com')
                print(f"✅ Created new admin user: {admin_username}")
            else:
                print(f"✅ Found existing admin user: {admin_username}")
            
            # Set password
            admin_user.set_password(new_password)
            db.session.commit()
            
            print(f"✅ Password set successfully!")
            print(f"   Username: {admin_username}")
            print(f"   Password: {new_password}")
            print()
            print("⚠️  Note: This password will be reset on next app restart")
            print("   To make it permanent, add PostgreSQL to Heroku:")
            print("   heroku addons:create heroku-postgresql:hobby-dev")
            
            return True
            
        except Exception as e:
            print(f"❌ Error setting password: {str(e)}")
            db.session.rollback()
            return False

if __name__ == "__main__":
    set_password_immediately()
