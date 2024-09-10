from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import data_required

class loginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[data_required()])
    password = PasswordField('Password', [data_required()])
    submit = SubmitField('Enviar')
