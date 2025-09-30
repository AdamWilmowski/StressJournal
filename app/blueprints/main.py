"""
Main application routes for the Stress Diary application.
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from ..models import StressEvent
from ..utils import login_required, get_current_user

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def index():
    """Main dashboard page."""
    user = get_current_user()
    if user is None:
        flash('Sesja wygasła. Zaloguj się ponownie.', 'error')
        return redirect(url_for('auth.login'))
    
    events = StressEvent.query.filter_by(user_id=user.id).order_by(
        StressEvent.date.desc(), StressEvent.created_at.desc()
    ).limit(10).all()
    
    return render_template('index.html', events=events)
