from flask import render_template, redirect, flash, url_for, session

from . import auth
from app.forms import loginForm

@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = loginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('El usuario ' + username + ' se ha registrado con exito')
        return redirect(url_for('index'))
    
    return render_template('login.html', **context)
