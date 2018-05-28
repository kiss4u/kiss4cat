# -*- coding: utf-8 -*-
# !/usr/bin/env python

from wtforms import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

#登录表单
class Login_Form(Form):
    account = StringField('account', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('login')


#注册表单
class Register_Form(Form):
    account = StringField('account', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('regist')