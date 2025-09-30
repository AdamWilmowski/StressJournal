"""
Forms for the Stress Diary application.
"""

from datetime import date
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, DateField, PasswordField, validators

class LoginForm(FlaskForm):
    """Login form for user authentication."""
    username = StringField('Nazwa użytkownika', [validators.DataRequired(), validators.Length(min=3, max=80)])
    password = PasswordField('Hasło', [validators.DataRequired()])

class StressEventForm(FlaskForm):
    """Form for creating and editing stress events."""
    title = StringField('Tytuł', [validators.DataRequired(), validators.Length(min=1, max=200)])
    description = TextAreaField('Opis')
    date = DateField('Data', [validators.DataRequired()], default=date.today)
    time = StringField('Czas (GG:MM)')
    stress_level = SelectField('Poziom stresu (1-10)', 
                              choices=[(i, f'{i} - {"Niski" if i <= 3 else "Umiarkowany" if i <= 6 else "Wysoki" if i <= 8 else "Bardzo wysoki"}') 
                                      for i in range(1, 11)],
                              coerce=int)
    category = SelectField('Kategoria', 
                          choices=[('work', 'Praca'), ('relationships', 'Relacje'), 
                                 ('health', 'Zdrowie'), ('financial', 'Finanse'),
                                 ('family', 'Rodzina'), ('social', 'Społeczne'),
                                 ('other', 'Inne')])
    location = StringField('Lokalizacja')
    triggers = TextAreaField('Co wywołało ten stres?')
    symptoms = TextAreaField('Objawy fizyczne/emocjonalne')
    coping_strategies = TextAreaField('Jak sobie radziłeś?')
