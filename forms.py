from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import DataRequired

class SimpleMessage(FlaskForm):
    data = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')

