# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import LoginManager
from database.sqllite_operate import Users
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
login_manager = LoginManager()
login_manager.login_view = 'sign.sign_in'
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))
from programe.article import article
from programe.catlog import catlog
from programe.sign import sign
app.register_blueprint(catlog, url_prefix='/catlog')

app.register_blueprint(article, url_prefix='/article')

app.register_blueprint(sign, url_prefix='/sign')

if __name__ == '__main__':
    app.run(debug=True)
