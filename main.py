from flask import Flask, render_template, request, Response
import forms
from flask import flash
from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import redirect
from config import DevelopmentConfig
from models import db
from models import Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf=CSRFProtect()

app.secret_key='esta es la clave secreta'

@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'),404


@app.route("/index")
def index():
    g.nombre = 'Daniel'
    escuela = "UTL"
    alumnos = ["Mario", "Pedro", "Luis", "Dario"]

    return render_template("index.html", escuela=escuela, alumnos=alumnos)

@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    nom = ''
    apa = ''
    ama = ''
    alum_form = forms.UsersForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data
        edad = alum_form.edad.data
        mensaje='Bienvenido {}'.format(nom)
        flash(mensaje)

        print("Nombre: {}".format(nom))
        print("Apaterno: {}".format(apa))
        print("Amaterno: {}".format(ama))

    return render_template("alumnos.html", form=alum_form, nom=nom, apa=apa, ama=ama)

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()
