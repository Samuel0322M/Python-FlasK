#flask con f minuscula es la extension, Flask es la clase que nos permite crear instancias de flask
from flask import Flask, request, make_response, redirect, render_template, abort, session, url_for, flash, get_flashed_messages
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import data_required
import unittest
#crear una nueva instancia de flask declaramos una variable llamada app y mandar llamar la clase flask para crear una nueva instancia
app = Flask(__name__)
#de esta forma se inicializa bootstrap
Bootstrap = Bootstrap(app)
#se puede hacer el debug
app.debug = True

app.config['SECRET_KEY'] = 'SUPER SECRETO'

todos = ["Comprar chaqueta", "Sonic Frontiers", "Mando xbox"]

class loginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[data_required()])
    password = PasswordField('Password', [data_required()])
    submit = SubmitField('Enviar')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.route('/error')
def internal_error():
    abort(500)

@app.errorhandler(500)
def system_error(error):
    return render_template('error.html', error=error)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.route("/")
def index():
    user_ip = request.remote_addr
    
    response = make_response(redirect("/hello"))
    session['user_ip'] = user_ip
    #response.set_cookie("user_ip", user_ip)

    return response

@app.route("/hello", methods=['GET', 'POST'])
def hello():
    #creamos una bariable user_ip que va a tener el valor de la ip que detectamos en el request, 
    #request tiene una propiedad llamdaa request addr que es igual a la ip del usuario
    user_ip = session.get("user_ip")
    login_form = loginForm()
    username = session.get('username')
    context = {
        "user_ip":user_ip,
        "todos": todos,
        'login_form': login_form,
        'username': username
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('El usuario ' + username + ' se ha registrado con exito')
        return redirect(url_for('hello'))

    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(port=8080)