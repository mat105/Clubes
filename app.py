import flask
import csv

from appconfig import app
from models import Club

#barrios = None

@app.route('/clubes', methods=["GET"])
def listado_clubes():
    nombre = flask.request.args.get("nombre")
    actividades = flask.request.args.get("actividades")
    barrio = flask.request.args.get("barrio")
    pagina = flask.request.args.get("p")
    

    clubs = Club.query

    if nombre != None and len(nombre) > 0:
        clubs = clubs.filter(Club.nombre.contains(nombre))
    else:
        nombre = ""

    if actividades != None and len(actividades) > 0:
        clubs = clubs.filter(Club.actividades.contains(actividades))
    else:
        actividades = ""

    if barrio != None and len(barrio) > 0:
        clubs = clubs.filter(Club.barrio.contains(barrio))
    else:
        barrio = ""


    if pagina != None and len(pagina) > 0:
        ipagina = int(pagina)
        cant_pags = clubs.count()//20
        if ipagina < 0 or ipagina > cant_pags:
            flask.abort(404)
        else:
            ipagina = 20 * ipagina
        clubs = clubs.filter(Club.id > ipagina)
    else:
        cant_pags = clubs.count()//20

    clubs = clubs.limit(20).all()
    querystr = "nombre={}&actividades={}&barrio={}".format(nombre,actividades,barrio)
    return flask.render_template("listado.html", clubes=clubs, nombre=nombre, actividades=actividades, barrio=barrio, opbarrios=barrios, querystring=querystr, paginas=cant_pags)

@app.route('/clubes/<int:id>', methods=["GET"])
def info_club(id):
    club = Club.query.get(id)

    return club.nombre

@app.route('/', methods=["GET"])
def home():
    #cincoclubes = Club.query.filter(Club.actividades.contains("hockey")).group_by(Club.nombre).limit(3).all()

    return flask.render_template("index.html")

if __name__ == '__main__':
    global barrios

    barrios = Club.query.group_by(Club.barrio).all()
    barrios = [barr.barrio for barr in barrios]

    app.run(debug=True)