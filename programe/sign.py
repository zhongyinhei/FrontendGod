# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, redirect
from flask_login import login_user

from database.sqllite_operate import Users, db
from utils.tool import enPassWord

sign = Blueprint('sign', __name__)


@sign.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')


@sign.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')

@sign.route('/login',methods=['POST'])
@sign.route('/register', methods=['POST'])
def register():
    form = dict(request.form)
    nickname = form.get('nickname', '')
    password = form.get('password', '')
    result = Users.query.filter_by(nickname=nickname).first()
    if not result:
        password_hash = enPassWord(password)
        User = Users(nickname=nickname, password=password, password_hash=password_hash)
        db.session.add(User)
        db.session.commit()
        result = Users.query.filter_by(nickname=nickname).first()
        login_user(result, remember=True)
        return redirect('../catlog?nickname={}'.format(nickname))
    else:
        return redirect('../sign/sign_in')
