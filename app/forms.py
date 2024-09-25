from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import data_required

class loginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[data_required()])
    password = PasswordField('Password', [data_required()])
    submit = SubmitField('Enviar')

class TodoForm(FlaskForm):
    description = StringField('Descripcion', validators=[data_required()])
    Submit = SubmitField('Crear')

class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Borrar')

class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualizar')