# -*- coding: utf-8 -*-
import datetime

from flask import Blueprint, render_template

from database.sqllite_operate import JinMi

article = Blueprint('article', __name__)


@article.route('/<int:unique_pid>')
def index(unique_pid):
    result = JinMi.query.filter_by(unique_pid=unique_pid).all()[0]
    title = result.title
    one_label = result.one_label
    two_label = result.two_label
    author = result.author
    visiting = result.visiting
    discuss = result.discuss
    publish_date = result.publish_date
    content = result.content
    tupian = result.tupian
    breadcrumbs = """
     <small>&gt;</small>
            <a href="../catloglist?one_label={}">{}</a>
            <small>&gt;</small>
            <a href="../catloglist?two_label={}">{}</a>
            <small>&gt;</small>
            <span class="muted" style="color: #999">{}</span>
    """.format(one_label, one_label, two_label, two_label, title)
    date_time = ''
    year = datetime.datetime.now().year - eval(publish_date[:4])
    if year > 0:
        date_time = '{}年前 ({})'.format(year, publish_date)
    elif year == 0:
        print(type(publish_date[5:7]))
        month = abs(int(datetime.datetime.now().month - int(publish_date[5:7])))
        if month > 0:
            date_time = '{}月前 ({})'.format(month, publish_date)
        elif month == 0:
            day = abs(int(datetime.datetime.now().day - int(publish_date[-2:])))
            date_time = '{}天前 ({})'.format(day, publish_date)
    meta = """
       <span id="mute-category" class="muted"><i class="fa fa-list-alt"></i><a
                        href="../catloglist?two_label={}"> {}</a></span> <span class="muted"><i
                    class="fa fa-user"></i> {}</span>
                <time class="muted"><i class="fa fa-clock-o"></i> {}</time>
                <span class="muted"><i class="fa fa-eye"></i> {}浏览</span>
                <span class="muted"><i class="fa fa-comments-o"></i> {}评论</span>
            </div>
    """.format(two_label, two_label, author, date_time, visiting, discuss)
    contents = content.split('\n')
    article_content = ''
    for i in contents:
        a = "<p>{}</p>".format(i.replace('\r', ''))
        article_content += a
    article_content = '"{}"'.format(article_content)
    tupian = repr(
        '<img src="/static/images/{}.jpg" style="float: left;width: 440px;height:261px;padding:10px">'.format(tupian))
    return render_template('article.html', breadcrumbs=breadcrumbs, meta=meta, title=title,
                           article_content=article_content, tupian=tupian)
