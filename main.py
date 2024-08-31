#flask con f minuscula es la extension, Flask es la clase que nos permite crear instancias de flask
from flask import Flask, request, make_response, redirect, render_template

#crear una nueva instancia de flask declaramos una variable llamada app y mandar llamar la clase flask para crear una nueva instancia
app = Flask(__name__)
app.debug = "true"
todos = ["Comprar chaqueta", "Sonic Frontiers", "Mando xbox"]

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