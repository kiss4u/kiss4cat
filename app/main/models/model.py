# -*- coding: utf-8 -*-
# !/usr/bin/env python

from app import db

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.BIGINT, primary_key=True)
    account = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __repr__(self):
        return '<Account %r>' % self.username
