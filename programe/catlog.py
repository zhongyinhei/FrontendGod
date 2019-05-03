# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request

from database.sqllite_operate import JinMi

catlog = Blueprint('catlog', __name__)


@catlog.route('/')
def index():
    result = JinMi.query.order_by('-like').limit(10).all()
    html = []
    for num, i in enumerate(result):
        title = i.title
        like = i.like
        num = num + 1
        unique_pid = i.unique_pid
        html.append("""
                <td class="hot-posts-{}">{}</td>
                <td style="color:#00a67c;padding-left:20px" onclick='window.open("../article/{}")' onmouseover="mOver(this)" onmouseout="mOut(this)" title="{}">{}</td>
                <td style="text-align: right;color:#f78585">{}热度</td>
            """.format(num, num, unique_pid, title, title, like))
    nickname = '"{}"'.format(dict(request.args).get('nickname', ''))
    return render_template('catlog.html', contents=html, nickname=nickname)
