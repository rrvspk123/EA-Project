from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm, \
    ResetPasswordRequestForm, ResetPasswordForm, WebForm, WebRelateForm, NewForm, ProForm
from app.models import User, Post, Website, Website_relate, newest_info, promote
import psycopg2

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html.j2')


@app.route('/wbase')
def wbase():
    website = Website.query.all()
    w_relate = Website_relate.query.all()
    new_data = db.session.query(newest_info).all()
    return render_template("wbase.html.j2",website=website,w_relate=w_relate,new_data=new_data)

@app.route('/addweb', methods=['GET', 'POST'])
def addweb():
    form = WebForm()
    if form.validate_on_submit():
        webdata = Website(author=form.author.data, link_p=form.link_p.data, title=form.title.data, middle_data=form.middle_data.data)
        db.session.add(webdata)
        db.session.commit()
        return redirect(url_for('addweb'))
    return render_template('addweb.html.j2', form=form)

@app.route('/addweb_r', methods=['GET', 'POST'])
def addweb_r():
    form = WebRelateForm()
    if form.validate_on_submit():
        web_r_data = Website_relate(link=form.link.data, title_r=form.title_r.data,)
        db.session.add(web_r_data)
        db.session.commit()
        return redirect(url_for('addweb_r'))
    return render_template('addweb_r.html.j2', form=form)

@app.route('/wbase/<int:id>')
def page(id):
    # 建立数据库连接
    conn = psycopg2.connect(
        host="postgresdb",
        database="postgres",
        user="postgres",
        password="postgres"
    )

    # 查询数据
    cur = conn.cursor()
    cur.execute(f"SELECT TITLE, LINK_P, AUTHOR, MIDDLE_DATA FROM website WHERE ID={id}")
    result = cur.fetchone()
    cur.execute(f"SELECT TITLE_R, LINK FROM website_relate")
    result_r = cur.fetchone()




    # 关闭连接
    cur.close()
    conn.close()
    new_data = db.session.query(newest_info).all()
    web_relate = db.session.query(Website_relate).all()
    website = db.session.query(Website).all()
    # 渲染模板
    return render_template('wbase.html.j2', title=result[0], link_p=result[1],author=result[2],middle_data=result[3],title_r=result_r[0],link=result_r[1],new_data=new_data,web_relate=web_relate,website=website)

@app.route('/addweb_n', methods=['GET', 'POST'])
def addweb_n():
    form = NewForm()
    if form.validate_on_submit():
        new_data = newest_info(link_n=form.link_n.data, title_n=form.title_n.data,)
        db.session.add(new_data)
        db.session.commit()
        return redirect(url_for('addweb_n'))
    return render_template('addweb_n.html.j2', form=form)

@app.route('/addweb_pro', methods=['GET', 'POST'])
def addweb_pro():
    form = ProForm()
    if form.validate_on_submit():
        pro_data = promote(link_pro=form.link_pro.data, title_pro=form.title_pro.data,)
        db.session.add(pro_data)
        db.session.commit()
        return redirect(url_for('addweb_pro'))
    return render_template('addweb_pro.html.j2', form=form)


@app.route("/testing")
def testing():
    new_data = db.session.query(newest_info).all()
    return render_template("testing.html.j2", new_data=new_data)

if __name__ == '__main__':
    app.run(debug=True)
 







