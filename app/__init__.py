# -*- coding: utf-8 -*-
# !/usr/bin/env python
# 初始化服务，加载相关配置

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config
import pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):
    # 默认静态路径
    app = Flask(__name__, static_url_path='')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)

    # attach routes and custom error pages here
    # 注册蓝图
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app

