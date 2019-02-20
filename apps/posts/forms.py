from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField

class PostUpdte(FlaskForm):
    title = StringField('Titulo del post')
    content = TextAreaField()
    submit = SubmitField('Actualizar')