"""
Utility functions for the Stress Diary application.
"""

from functools import wraps
from flask import session, redirect, url_for, flash
from .models import db, User

def login_required(f):
    """Decorator to require user login for protected routes."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function

def get_current_user():
    """Get the current logged-in user from session."""
    if 'user_id' in session:
        user = db.session.get(User, session['user_id'])
        if user is None:
            # User doesn't exist anymore, clear the session
            session.clear()
        return user
    return None
