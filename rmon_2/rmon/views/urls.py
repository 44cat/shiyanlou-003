# -*- conding:utf-8 -*-
"""
rmon.viewx.urls
定义了所有API对应的URL
"""
from flask import Blueprint
from rmon.views.index import IndexView
from rmon.views.server import ServerList

api = Blueprint('api',__name__)

api.add_url_rule('/',view_func=IndexView.as_view('index'))

api.add_url_rule('/servers/',view_func=ServerList.as_view('server_list'))

