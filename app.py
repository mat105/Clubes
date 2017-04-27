import flask
import csv

from appconfig import app
from models import Club

#barrios = None

CLUBES_POR_PAGINA = 15

@app.route('/clubes', methods=["GET"])
def listado_clubes():
    nombre = flask.request.args.get("nombre")
    actividades = flask.request.args.get("actividades")
    barrio = flask.request.args.get("barrio")
    pagina = flask.request.args.get("p")
    ipagina = 0
    

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

    cant_pags = clubs.count()//CLUBES_POR_PAGINA

    if pagina != None and len(pagina) > 0:
        ipagina = int(pagina)
        #cant_pags = clubs.count()//20
        if ipagina < 0 or ipagina > cant_pags:
            flask.abort(404)
        
        idpag = CLUBES_POR_PAGINA * ipagina
        clubs = clubs.filter(Club.id > idpag)
    #else:
        #cant_pags = clubs.count()//20

    
    clubs = clubs.limit(CLUBES_POR_PAGINA).all()
    querystr = "nombre={}&actividades={}&barrio={}".format(nombre,actividades,barrio)
    return flask.render_template("listado.html", clubes=clubs, nombre=nombre, actividades=actividades, barrio=barrio, opbarrios=barrios, querystring=querystr, quepagina=ipagina, paginas=cant_pags)

@app.route('/clubes/<int:id>', methods=["GET"])
def info_club(id):
    club = Club.query.get(id)

    return flask.render_template("infoclub.html", club=club)

@app.route('/', methods=["GET"])
def home():
    #cincoclubes = Club.query.filter(Club.actividades.contains("hockey")).group_by(Club.nombre).limit(3).all()

    return flask.render_template("index.html")

if __name__ == '__main__':
    global barrios

    barrios = Club.query.group_by(Club.barrio).all()
    barrios = [barr.barrio for barr in barrios]

    app.run(debug=True)