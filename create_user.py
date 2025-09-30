#!/usr/bin/env python3
"""
Script to create a new user for the Stress Diary application.
This script should be run to create the initial admin user.
"""

import sys
import os
from werkzeug.security import generate_password_hash

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from app.models import db, User

def create_user():
    """Create a new user interactively."""
    app = create_app()
    with app.app_context():
        # Create tables if they don't exist
        db.create_all()
        
        print("=== Stress Diary User Creation ===")
        print("This script will create a new user account.")
        print()
        
        # Get user input
        username = input("Enter username: ").strip()
        if not username:
            print("Username cannot be empty!")
            return
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            print(f"Username '{username}' already exists!")
            return
        
        email = input("Enter email: ").strip()
        if not email:
            print("Email cannot be empty!")
            return
        
        # Check if email already exists
        if User.query.filter_by(email=email).first():
            print(f"Email '{email}' is already registered!")
            return
        
        password = input("Enter password: ").strip()
        if not password:
            print("Password cannot be empty!")
            return
        
        if len(password) < 6:
            print("Password must be at least 6 characters long!")
            return
        
        # Create the user
        user = User(username=username, email=email)
        user.set_password(password)
        
        try:
            db.session.add(user)
            db.session.commit()
            print(f"\n✅ User '{username}' created successfully!")
            print(f"Email: {email}")
            print("\nYou can now login to the Stress Diary application.")
        except Exception as e:
            print(f"❌ Error creating user: {e}")
            db.session.rollback()

def list_users():
    """List all existing users."""
    app = create_app()
    with app.app_context():
        users = User.query.all()
        if not users:
            print("No users found in the database.")
            return
        
        print("=== Existing Users ===")
        for user in users:
            print(f"Username: {user.username}")
            print(f"Email: {user.email}")
            print(f"Created: {user.created_at}")
            print("-" * 30)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "list":
        list_users()
    else:
        create_user()

