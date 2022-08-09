from crypt import methods
from turtle import title
from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request
import tkinter as tk
from tkinter import ttk
from flask_sqlalchemy import SQLAlchemy
from flask import redirect
from flask import url_for



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rootuser:120893guiTD!@localhost:3306/schema_mapOrm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column('usu_id', db.Integer, primary_key=True)
    nome = db.Column('usu_nome', db.String(256))
    email = db.Column('usu_email', db.String(256))
    senha = db.Column('usu_senha', db.String(256))
    end = db.Column('usu_end', db.String(256))

    def __init__(self, nome, email, senha, end):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.end = end

@app.route("/")
def index():
    return render_template('index.html')



@app.route('/cad/usuario')
def cadusuario():
    return render_template('usuario.html', titulo='Cadastro de Usuário')



@app.route('/cad/caduser', methods=['POST'])
def caduser():
    usuario = Usuario(request.form.get('user'), request.form.get('email'),request.form.get('passwd'),request.form.get('end'))
    db.session.add(usuario)
    db.session.commit()
    return render_template('index.html')


@app.route('/cad/anuncio')
def anuncio():
    return render_template('anuncio.html')



@app.route('/anuncios/perguntas')
def pergunta():
    return render_template('pergunta.html')


@app.route('/anuncio/pergunta', methods=['POST'])
def anunciopergunta():
    return request.form



@app.route('/anuncios/compra')
def compra():
    print ('Comprado')
    return ''



@app.route('/anuncio/favorito')
def favorito():
    print('Favorito Inserido')
    return render_template('favorito.html')


@app.route('/config/categoria')
def categoria():
    return render_template('categoria.html', titulo='Categoria dos produtos')



@app.route('/relatorios/vendas')
def relVendas():
    return render_template('relVendas.html', titulo='Seu relatório de vendas')



@app.route('/relatarios/compras')
def relCompras():
    return render_template('relCompras.html', titulo='Seu histórico de compras')


if __name__ == 'newold':
    db.create_all()