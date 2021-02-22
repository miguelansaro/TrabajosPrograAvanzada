from flask import Flask, request, url_for, redirect, render_template, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import simplejson
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///productos.db'
app.config['SECRET_KEY'] = "123"
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
db = SQLAlchemy(app)

class producto(db.Model):
    id = db.Column("producto_id", db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(100))
    producto_valor = db.Column(db.Integer)
    producto_cantidad = db.Column(db.Integer)
    
    def __init__(self, datos):
        self.producto_nombre = datos["nombre"]
        self.producto_valor = datos["valor"]
        self.producto_cantidad = datos["cantidad"]


@app.route("/")
@cross_origin()
def principal():
    data = producto.query.all()
    lista = {}
    for i in data:
        datos = {
            "id": i.id,
            "nombre": i.producto_nombre,
            "cantidad": i.producto_cantidad,
            "valor": i.producto_valor
        }
        lista[i.id] = datos
    return jsonify(lista)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/agregar")
def agregar():
    return render_template("agregar.html")

@app.route("/agregar/<nombre>/<int:valor>/<int:cantidad>")
def agregarp(nombre, valor, cantidad):
    datos = {"nombre": nombre, 
             "cantidad": cantidad,
             "valor": valor
    }

    p = producto(datos)
    db.session.add(p)
    db.session.commit()
    return principal()
    
@app.route("/agregarc/<int:id>/<int:cantidad>")
def agregarc(id, cantidad):
    p = producto.query.filter_by(id=id).first()
    if cantidad < 0 :
        return principal()
    else:
        p.producto_cantidad = p.producto_cantidad + cantidad
        db.session.commit()
        return principal()

@app.route("/agregarv/<int:id>/<int:valor>")
def agregarv(id, valor):
    p = producto.query.filter_by(id=id).first()
    if valor < 0 :
        return principal()
    else:
        p.producto_valor = p.producto_valor + valor
        db.session.commit()
        return principal()

@app.route("/sacarc/<int:id>/<int:cantidad>")
def sacarc(id, cantidad):
    p = producto.query.filter_by(id=id).first()
    if p.producto_cantidad < cantidad:
        return principal()
    else:
        p.producto_cantidad = p.producto_cantidad - cantidad
        db.session.commit()
        return principal()

@app.route("/sacarv/<int:id>/<int:valor>")
def sacarv(id, valor):
    p = producto.query.filter_by(id=id).first()
    if p.producto_valor < valor:
        return principal()
    else:
        p.producto_valor = p.producto_valor - valor
        db.session.commit()
        return principal()

@app.route("/resetv/<int:id>")
def resetv(id):
    p = producto.query.filter_by(id=id).first()
    p.producto_valor = p.producto_valor - p.producto_valor
    db.session.commit()
    return principal()

@app.route("/resetc/<int:id>")
def resetc(id):
    p = producto.query.filter_by(id=id).first()
    p.producto_cantidad = p.producto_cantidad - p.producto_cantidad
    db.session.commit()
    return principal()

@app.route("/vaciar")
def vaciar():
    p = producto.query.filter().delete()
    db.session.commit()
    return principal()

@app.route("/eliminar/<int:id>")
def eliminar(id):
    p = producto.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return  principal()

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
