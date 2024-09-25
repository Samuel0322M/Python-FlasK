#flask con f minuscula es la extension, Flask es la clase que nos permite crear instancias de flask
from flask import request, make_response, redirect, render_template, session, url_for, flash, abort, redirect
from flask_login import login_required, current_user
import unittest

from app import create_app
from app.forms import TodoForm, DeleteTodoForm, UpdateTodoForm
from app.firestore_service import update_todo, get_todos, put_todo, delete_todo
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

@app.route("/hello", methods=['GET', 'POST'])
@login_required
def hello():
    #creamos una bariable user_ip que va a tener el valor de la ip que detectamos en el request, 
    #request tiene una propiedad llamdaa request addr que es igual a la ip del usuario
    user_ip = session.get("user_ip")
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoForm()
    update_form = UpdateTodoForm()
    context = {
        "user_ip":user_ip,
        "todos": get_todos(user_id=username),
        'username': username,
        'todo_form': todo_form,
        "delete_form": delete_form,
        "update_form": update_form
    }
    
    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)

        flash('Tu tarea se creo con exito!')
        return redirect(url_for('hello'))

    return render_template("index.html", **context)


@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))


@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id

    update_todo(user_id=user_id, todo_id=todo_id, done=done)
    
    return redirect(url_for('hello'))

if __name__ == "__main__":
    app.run(port=8080)