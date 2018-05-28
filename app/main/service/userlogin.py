# -*- coding: utf-8 -*-
# !/usr/bin/env python

from app.main.tools import tmysql

def do_login(username, password):
    sql = 'select level from account where username = "%s" and password = "%s"' % (username, password)
    db = tmysql.Mysql()
    res_login = db.getOne(sql)

    if res_login:

        return True
    else:
        return False

if __name__ == '__main__':
    print(do_login("123","123"))