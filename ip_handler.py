#-*- coding:utf-8 -*-
import re
import os
from wechatpy.messages import TextMessage
from wechatpy import create_reply
from qqwry import QQwry

class CommandHandler:
    command = ''

    def check_match(self,message):
        if not isinstance(message,TextMessage):
            return False
        if not message.content.strip().lower().startswith(self.command):
            return False
        return True

class IPLocationHandler(CommandHandler):
    command = 'ip'

    def __init__(self):
        #file =
        self.q = QQwry()
        self.q.load_file('./qqwry.dat')


    def handle(self,message):
        if not self.check_match(message):
            return 
        xiaoxi = message.content.strip().split()
        #print(xiaoxi)
        if len(xiaoxi) == 1 or len(xiaoxi) > 2:
            return create_reply('IP地址无效',message)
        ip = xiaoxi[1]
        pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
        if not re.match(pattern,ip):
            return create_reply('IP地址无效',message)

        r = self.q.lookup(ip)
        if r is None:
            return create_reply('未找到这个IP的地址归属地',message)
        else:
            return create_reply(r[0],message)

