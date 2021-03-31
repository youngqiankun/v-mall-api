# -*- coding: utf-8 -*-
# @Time    : 2021/3/23 9:27 AM
# @Author  : yangyang
# @Email   : yangyang@ixiye.com
# @File    : db_register.py
# @Software: PyCharm


from flask_sqlalchemy import SQLAlchemy

from run import app

app.config.from_object('config')

db = SQLAlchemy(app)
