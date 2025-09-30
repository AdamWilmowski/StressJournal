"""
Event management routes for the Stress Diary application.
"""

from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..models import db, StressEvent
from ..forms import StressEventForm
from ..utils import login_required, get_current_user

events = Blueprint('events', __name__)

@events.route('/add', methods=['GET', 'POST'])
@login_required
def add_event():
    """Add a new stress event."""
    form = StressEventForm()
    if form.validate_on_submit():
        # Parse time if provided
        time_obj = None
        if form.time.data:
            try:
                time_obj = datetime.strptime(form.time.data, '%H:%M').time()
            except ValueError:
                flash('Nieprawidłowy format czasu. Użyj formatu GG:MM.', 'error')
                return render_template('add_event.html', form=form)
        
        user = get_current_user()
        event = StressEvent(
            title=form.title.data,
            description=form.description.data,
            date=form.date.data,
            time=time_obj,
            stress_level=form.stress_level.data,
            category=form.category.data,
            location=form.location.data,
            triggers=form.triggers.data,
            symptoms=form.symptoms.data,
            coping_strategies=form.coping_strategies.data,
            user_id=user.id
        )
        
        db.session.add(event)
        db.session.commit()
        flash('Wydarzenie stresowe zostało dodane pomyślnie!', 'success')
        return redirect(url_for('main.index'))
    
    return render_template('add_event.html', form=form)

@events.route('/events')
@login_required
def list_events():
    """List all stress events with pagination."""
    user = get_current_user()
    page = request.args.get('page', 1, type=int)
    events_paginated = StressEvent.query.filter_by(user_id=user.id).order_by(
        StressEvent.date.desc(), StressEvent.created_at.desc()
    ).paginate(page=page, per_page=20, error_out=False)
    
    return render_template('events.html', events=events_paginated)

@events.route('/event/<int:event_id>')
@login_required
def view_event(event_id):
    """View a specific stress event."""
    user = get_current_user()
    event = StressEvent.query.filter_by(id=event_id, user_id=user.id).first_or_404()
    return render_template('view_event.html', event=event)

@events.route('/edit/<int:event_id>', methods=['GET', 'POST'])
@login_required
def edit_event(event_id):
    """Edit a specific stress event."""
    user = get_current_user()
    event = StressEvent.query.filter_by(id=event_id, user_id=user.id).first_or_404()
    form = StressEventForm(obj=event)
    
    if form.validate_on_submit():
        # Parse time if provided
        time_obj = None
        if form.time.data:
            try:
                time_obj = datetime.strptime(form.time.data, '%H:%M').time()
            except ValueError:
                flash('Nieprawidłowy format czasu. Użyj formatu GG:MM.', 'error')
                return render_template('edit_event.html', form=form, event=event)
        
        event.title = form.title.data
        event.description = form.description.data
        event.date = form.date.data
        event.time = time_obj
        event.stress_level = form.stress_level.data
        event.category = form.category.data
        event.location = form.location.data
        event.triggers = form.triggers.data
        event.symptoms = form.symptoms.data
        event.coping_strategies = form.coping_strategies.data
        
        db.session.commit()
        flash('Wydarzenie zostało zaktualizowane pomyślnie!', 'success')
        return redirect(url_for('events.view_event', event_id=event.id))
    
    return render_template('edit_event.html', form=form, event=event)

@events.route('/delete/<int:event_id>', methods=['POST'])
@login_required
def delete_event(event_id):
    """Delete a specific stress event."""
    user = get_current_user()
    event = StressEvent.query.filter_by(id=event_id, user_id=user.id).first_or_404()
    db.session.delete(event)
    db.session.commit()
    flash('Wydarzenie zostało usunięte pomyślnie!', 'success')
    return redirect(url_for('events.list_events'))
