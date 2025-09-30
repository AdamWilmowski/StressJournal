#!/usr/bin/env python3
"""
Script to change admin user password.
Works both locally and on Heroku.
"""

import os
import sys
from app import create_app
from app.models import db, User

def change_admin_password():
    """Change admin user password."""
    app = create_app()
    
    with app.app_context():
        print("=== Change Admin Password ===")
        
        # Get admin username
        admin_username = input("Admin username (default: admin): ").strip() or "admin"
        
        # Find the admin user
        admin_user = User.query.filter_by(username=admin_username).first()
        if not admin_user:
            print(f"❌ Admin user '{admin_username}' not found!")
            return False
        
        print(f"✅ Found admin user: {admin_user.username} ({admin_user.email})")
        
        # Get new password
        new_password = input("Enter new password: ").strip()
        if not new_password:
            print("❌ Password cannot be empty!")
            return False
        
        # Confirm password
        confirm_password = input("Confirm new password: ").strip()
        if new_password != confirm_password:
            print("❌ Passwords don't match!")
            return False
        
        try:
            # Update password
            admin_user.set_password(new_password)
            db.session.commit()
            print(f"✅ Password updated successfully for user '{admin_username}'!")
            print(f"   New password: {new_password}")
            return True
            
        except Exception as e:
            print(f"❌ Error updating password: {str(e)}")
            db.session.rollback()
            return False

def change_admin_password_non_interactive(username, new_password):
    """Change admin password non-interactively (for scripts)."""
    app = create_app()
    
    with app.app_context():
        try:
            # Find the admin user
            admin_user = User.query.filter_by(username=username).first()
            if not admin_user:
                print(f"❌ Admin user '{username}' not found!")
                return False
            
            # Update password
            admin_user.set_password(new_password)
            db.session.commit()
            print(f"✅ Password updated successfully for user '{username}'!")
            return True
            
        except Exception as e:
            print(f"❌ Error updating password: {str(e)}")
            db.session.rollback()
            return False

if __name__ == "__main__":
    if len(sys.argv) == 3:
        # Non-interactive mode: python change_admin_password.py username password
        username = sys.argv[1]
        password = sys.argv[2]
        change_admin_password_non_interactive(username, password)
    else:
        # Interactive mode
        change_admin_password()
