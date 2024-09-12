#flask con f minuscula es la extension, Flask es la clase que nos permite crear instancias de flask
from flask import request, make_response, redirect, render_template, session, url_for, flash, abort, redirect
import unittest

from app import create_app
from app.forms import loginForm
from app.firestore_service import get_users, get_todos
#crear una nueva instancia de flask declaramos una variable llamada app y mandar llamar la clase flask para crear una nueva instancia

app = create_app()




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

@app.route("/hello", methods=['GET'])
def hello():
    #creamos una bariable user_ip que va a tener el valor de la ip que detectamos en el request, 
    #request tiene una propiedad llamdaa request addr que es igual a la ip del usuario
    user_ip = session.get("user_ip")
    username = session.get('username')
    context = {
        "user_ip":user_ip,
        "todos": get_todos(user_id=username),
        'username': username
    }
    
    users = get_users()

    for user in users:
        print(user.id)
        print(user.to_dict()['password'])

    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(port=8080)