from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired, URL

class WpForm(FlaskForm):
    url = StringField('Url de la web', validators=[DataRequired(message="Este campo es requerido"), URL(require_tld=False, message="url invalida")])
    username = StringField('Usuario', validators=[DataRequired(message="Este campo es requerido")])
    password = StringField('Password', validators=[DataRequired(message="Este campo es requerido")])
    submit = SubmitField('Guardar')
