#!/usr/bin/env python3
"""
Script to set custom admin credentials for the Stress Diary application.
This script allows you to set custom admin username, email, and password.
"""

import os
import sys
from app import create_app
from app.models import db, User

def set_admin_credentials():
    """Set custom admin credentials."""
    app = create_app()
    
    with app.app_context():
        print("=== Stress Diary Admin Setup ===")
        print("Set custom admin credentials (or press Enter for defaults)")
        print()
        
        # Get custom credentials
        username = input("Admin username (default: admin): ").strip() or "admin"
        email = input("Admin email (default: admin@stressdiary.com): ").strip() or "admin@stressdiary.com"
        password = input("Admin password (default: admin123): ").strip() or "admin123"
        
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            print(f"⚠️  User '{username}' already exists!")
            overwrite = input("Do you want to update the password? (y/n): ").strip().lower()
            if overwrite == 'y':
                existing_user.set_password(password)
                existing_user.email = email
                db.session.commit()
                print(f"✅ User '{username}' updated successfully!")
            else:
                print("❌ Operation cancelled.")
                return
        else:
            # Create new admin user
            admin_user = User(username=username, email=email)
            admin_user.set_password(password)
            db.session.add(admin_user)
            db.session.commit()
            print(f"✅ Admin user '{username}' created successfully!")
        
        print()
        print("Login credentials:")
        print(f"  Username: {username}")
        print(f"  Email: {email}")
        print(f"  Password: {password}")
        print()
        print("You can now login to the Stress Diary application.")

if __name__ == "__main__":
    set_admin_credentials()

