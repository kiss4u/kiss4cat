# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
from app import create_app, db

app = create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__ == '__main__':
    app.run()