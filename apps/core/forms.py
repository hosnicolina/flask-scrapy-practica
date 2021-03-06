from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class UlrForm(FlaskForm):

    url = StringField('Url de la web a revisar', validators=[DataRequired(), URL()])
    submit = SubmitField('Revisar la web')