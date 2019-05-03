# -*- coding: utf-8 -*-
from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/xh/Documents/GitHub/FrontendGod/sqljinmi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class JinMi(db.Model):
    __tablename__ = 'essay'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    one_label = db.Column(db.String(30))
    two_label = db.Column(db.String(30))
    author = db.Column(db.String(20))
    visiting = db.Column(db.String(20))
    discuss = db.Column(db.String(20))
    like = db.Column(db.String(20))
    tupian = db.Column(db.String(100))
    content = db.Column(db.String)
    publish_date = db.Column(db.String(20))
    unique_pid = db.Column(db.String(40))



class Users(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), unique=True)  # 设置为不可重复
    password = db.Column(db.String(20))
    password_hash = db.Column(db.String)


db.create_all()
