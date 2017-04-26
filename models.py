from appconfig import app, db
import sys

class Club(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(96))
    direccion = db.Column(db.String(64))
    email = db.Column(db.String(64))
    actividades = db.Column(db.Text)
    instalaciones = db.Column(db.Text)
    telefono = db.Column(db.String(24))
    web = db.Column(db.String(32))
    barrio = db.Column(db.String(32))
    pos_x = db.Column(db.Float)
    pos_y = db.Column(db.Float)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __init__(self, nombre, direccion, email, actividades, instalaciones, telefono, web, barrio, pos_x, pos_y):
        self.nombre = nombre
        self.direccion = direccion
        self.email = email
        self.actividades = actividades
        self.instalaciones = instalaciones
        self.telefono = telefono
        self.web = web
        self.barrio = barrio
        self.pos_x = pos_x
        self.pos_y = pos_y


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if "create" in sys.argv:
            db.create_all()
            db.session.commit()

