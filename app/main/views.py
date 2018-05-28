# -*- coding: utf-8 -*-
# !/usr/bin/env python
# 路由视图

import uuid
from flask import url_for, request, render_template, redirect, session, flash
# 导入蓝本
from . import main
from .service import userlogin
from .forms.form import *
from .models.model import *
from app import db

# 首页
@main.route('/', methods=['GET', 'POST'])
def index():
    if 'username' in session:
        # 存在缓存
        #return 'Logged in as %s' % escape(session['username'])
        return render_template('index.html', name_index_display=session['username'])
    return render_template('index.html')

# 跳转注册
@main.route("/to_regist")
def to_regist():
    return render_template('regist.html')

# 注册
@main.route('/regist', methods=['GET', 'POST'])
def regist():
    form = Register_Form(request.form)
    if form is None:
        flash('Should input username and password')
    elif form.submit():
        name = form.username.data
        userinfo = Account(username=name,account=form.account.data,password=form.password.data)
        try:
            db.session.add(userinfo)
            db.session.commit()
            session['username'] = name
            return redirect(url_for('main.index'))
        except:
            db.session.rollback()
            return render_template('regist.html', error='注册失败')

# 跳转登陆
@main.route("/to_login")
def to_login():
    return render_template('login.html')

# 登录
@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form = Login_Form(request.form)
        if form is None:
            flash('Should input username and password')
        elif form.submit():
            form_account = form.account.data
            account = Account.query.filter_by(account=form_account, password=form.password.data).first()
            if account is not None:
                session['username'] = account.username
                print('[%s]用户%s登录'%(account.account,account.username))
            else:
                flash('无效用户名或密码.')
                #return render_template('login.html',form=form)
    return redirect(url_for('main.index'))

# 登出
@main.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('main.index'))

# 测试
@main.route("/test")
def test():
    return render_template('base.html')

