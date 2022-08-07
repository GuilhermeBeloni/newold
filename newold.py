from crypt import methods
from turtle import title
from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')



@app.route('/cad/usuario')
def usuario():
    return render_template('usuario.html', titulo='Cadastro de Usuário')



@app.route('/cad/caduser', methods=['POST'])
def caduser():
    return request.form


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