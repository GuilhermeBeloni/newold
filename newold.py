from crypt import methods
from turtle import title
from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request
import tkinter as tk
from tkinter import ttk
from flask_sqlalchemy import SQLAlchemy
from flask import url_for
from flask import redirect




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://rootuser:120893guiTD!@localhost:3306/schema_mapOrm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


#OBJETOS

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

class Anuncio(db.Model):
    id = db.Column('anuncio_id', db.Integer, primary_key=True)
    nome = db.Column('anuncio_nome', db.String(256))
    desc = db.Column('anuncio_desc', db.String(256))
    qtd = db.Column('anuncio_qtd', db.Integer)
    preco = db.Column('anuncio_preco', db.Float)
    categoria_id = db.Column('categoria_id',db.Integer, db.ForeignKey("categoria.categoria_id"))
    usu_id = db.Column('usu_id',db.Integer, db.ForeignKey("usuario.usu_id"))


    def __init__(self, nome, desc, qtd, preco, categoria_id, usu_id):
        self.nome = nome
        self.desc = desc
        self.qtd = qtd
        self.preco = preco
        self.categoria = categoria_id
        self.usu_id = usu_id


class Categoria(db.Model):
    id = db.Column('categoria_id', db.Integer, primary_key=True)
    nome = db.Column('categoria_nome', db.String(256))
    desc = db.Column('categoria_desc', db.String(256))
    


    def __init__(self, nome, desc):
        self.nome = nome
        self.desc = desc
        

#ROTAS

@app.errorhandler(404)
def pagina404(error):
    return render_template('error404.html')



@app.route("/")
def index():
    return render_template('index.html')



#usuario

@app.route('/cad/usuario')
def usuario():
    return render_template('usuario.html', usuarios = Usuario.query.all(), titulo='Usuário')



@app.route('/usuario/criar', methods=['POST'])
def criarusuario():
    usuario = Usuario(request.form.get('user'), request.form.get('email'),request.form.get('passwd'),request.form.get('end'))
    db.session.add(usuario)
    db.session.commit()
    return redirect(url_for('usuario'))
    '''return render_template('index.html')'''


@app.route('/usuario/detalhar/<int:id>')
def buscarusuario(id):
    usuario = Usuario.query.get(id)
    return usuario.nome


@app.route('/usuario/editar/<int:id>', methods=['GET', 'POST'])
def editarusuario(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.nome = request.form.get('user')
        usuario.email = request.form.get('email')
        usuario.senha = request.form.get('passwd')
        usuario.end = request.form.get('end')

        db.session.add(usuario)
        db.session.commit()

        return redirect(url_for('usuario'))

    return render_template('editusuario.html', usuario = usuario, titulo='Usuario')   
    


@app.route('/usuario/deletar/<int:id>')
def deletarusuario(id):
    usuario = Usuario.query.get(id)
    db.session.delete(usuario)
    db.session.commit()
    return redirect(url_for('usuario'))





#anuncio

@app.route('/cad/anuncio')
def anuncio():
    return render_template('anuncio.html', anuncios = Anuncio.query.all(), categorias = Categoria.query.all(), titulo='Anúncios')


@app.route('/anuncio/criar', methods=['POST'])
def criaranuncio():
    anuncio = Anuncio(request.form.get('nome'), request.form.get('desc'), request.form.get('qtd'), request.form.get('preco'), request.form.get('categoria'), request.form.get('uso'))
    db.session.add(anuncio)
    db.session.commit()
    return redirect(url_for('anuncio'))



@app.route('/anuncios/perguntas')
def pergunta():
    return render_template('pergunta.html')


'''@app.route('/anuncio/pergunta', methods=['POST'])
def anunciopergunta():
    return render_template('pergunta.html')'''



@app.route('/anuncios/compra')
def compra():
    print ('Comprado')
    return ''



@app.route('/anuncio/favorito')
def favorito():
    print('Favorito Inserido')
    return render_template('favorito.html')





#categoria


@app.route('/cad/categoria')
def categoria():
    return render_template('categoria.html', categorias = Categoria.query.all(), titulo= 'Categoria dos produtos')


@app.route('/categoria/criar', methods=['POST'])
def criarcategoria():
    categoria = Categoria(request.form.get('nome'), request.form.get('desc'))
    db.session.add(categoria)
    db.session.commit()
    return redirect(url_for('categoria'))


@app.route('/categoria/deletar/<int:id>')
def deletarcategoria(id):
    categoria = Categoria.query.get(id)
    db.session.delete(categoria)
    db.session.commit()
    return redirect(url_for('categoria'))    







#relatorios

@app.route('/relatorios/vendas')
def relVendas():
    return render_template('relVendas.html', titulo='Seu relatório de vendas')



@app.route('/relatarios/compras')
def relCompras():
    return render_template('relCompras.html', titulo='Seu histórico de compras')


if __name__ == 'newold':
    db.create_all()