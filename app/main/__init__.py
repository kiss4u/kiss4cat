# -*- coding: utf-8 -*-
# !/usr/bin/env python

from flask import Blueprint
# 实例化蓝本，取代app管理路由
main = Blueprint('main', __name__)
# 避免循环导入依赖
from . import views, errors
