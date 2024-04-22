from ListaDeJogos import app
from flask import render_template, request, redirect, session, flash, url_for, send_from_directory
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

#Tela de Login
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()

    return render_template('login.html', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)

    # Consulta um usuário pelo nickname fornecido no formulário
    usuario = Usuarios.query.filter_by(nickname=form.nickname.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data)

    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        flash(usuario.nickname + ' Logado com SUCESSO!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)

    else:
        flash('Usuário não logado')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # Deslogar da Sessão
    session['usuario_logado'] = None
    flash('Logout efetuado com Sucesso!')
    return redirect(url_for('index'))