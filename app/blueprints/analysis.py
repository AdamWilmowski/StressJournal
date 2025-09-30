"""
Analysis routes for the Stress Diary application.
"""

from datetime import date, timedelta
from flask import Blueprint, render_template
from ..models import db, StressEvent
from ..utils import login_required, get_current_user

analysis = Blueprint('analysis', __name__)

@analysis.route('/analysis')
@login_required
def stress_analysis():
    """Display stress analysis and statistics."""
    user = get_current_user()
    
    # Basic analysis
    total_events = StressEvent.query.filter_by(user_id=user.id).count()
    avg_stress = db.session.query(db.func.avg(StressEvent.stress_level)).filter_by(user_id=user.id).scalar() or 0
    
    # Category breakdown
    categories = db.session.query(StressEvent.category, db.func.count(StressEvent.id)).filter_by(user_id=user.id).group_by(StressEvent.category).all()
    
    # Recent trends (last 7 days)
    week_ago = date.today() - timedelta(days=7)
    recent_events = StressEvent.query.filter_by(user_id=user.id).filter(StressEvent.date >= week_ago).all()
    
    return render_template('analysis.html', 
                         total_events=total_events,
                         avg_stress=round(avg_stress, 1),
                         categories=categories,
                         recent_events=recent_events)
