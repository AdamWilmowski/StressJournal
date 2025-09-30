"""
Authentication routes for the Stress Diary application.
"""

from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from ..models import User
from ..forms import LoginForm
from ..utils import get_current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """Handle user login."""
    if 'user_id' in session:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Logowanie pomyślne!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Nieprawidłowa nazwa użytkownika lub hasło', 'error')
    
    return render_template('login.html', form=form)

@auth.route('/logout')
def logout():
    """Handle user logout."""
    session.clear()
    flash('Zostałeś wylogowany', 'info')
    return redirect(url_for('auth.login'))
