#flask con f minuscula es la extension, Flask es la clase que nos permite crear instancias de flask
from flask import Flask, request, make_response, redirect, render_template, abort
from flask_bootstrap import Bootstrap5

#crear una nueva instancia de flask declaramos una variable llamada app y mandar llamar la clase flask para crear una nueva instancia
app = Flask(__name__)
#de esta forma se inicializa bootstrap
Bootstrap = Bootstrap5(app)
app.debug = "true"
todos = ["Comprar chaqueta", "Sonic Frontiers", "Mando xbox"]

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
    response.set_cookie("user_ip", user_ip)

    return response

@app.route("/hello")
def hello():
    #creamos una bariable user_ip que va a tener el valor de la ip que detectamos en el request, 
    #request tiene una propiedad llamdaa request addr que es igual a la ip del usuario
    user_ip = request.cookies.get("user_ip")
    context = {
        "user_ip":user_ip,
        "todos": todos,
    }

    return render_template("index.html", **context)

if __name__ == "__main__":
    app.run(port=8080)