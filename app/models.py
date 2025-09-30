"""
Database models for the Stress Diary application.
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """User model for authentication and user management."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with stress events
    stress_events = db.relationship('StressEvent', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        """Set password hash for the user."""
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        """Check if provided password matches the hash."""
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class StressEvent(db.Model):
    """Stress event model for tracking stress incidents."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=True)
    stress_level = db.Column(db.Integer, nullable=False)  # 1-10 scale
    category = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(200), nullable=True)
    triggers = db.Column(db.Text, nullable=True)  # What triggered the stress
    symptoms = db.Column(db.Text, nullable=True)  # Physical/emotional symptoms
    coping_strategies = db.Column(db.Text, nullable=True)  # How you coped
    related_events = db.Column(db.Text, nullable=True)  # JSON string of related event IDs
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f'<StressEvent {self.title}>'
