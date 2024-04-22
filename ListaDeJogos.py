from flask import Flask, render_template, request, redirect
from flask import session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

# Novo objeto sendo instanciado
app = Flask(__name__)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
csrf = CSRFProtect(app)
bcrypt = Bcrypt(app)

from views_game import *
from views_user import *

if __name__ == '__main__':
        #Rodar a aplicação
        app.run(debug=True)