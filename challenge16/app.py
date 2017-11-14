# -*- coding:utf-8 -*-
"""
  rmon.app
  该模块主要实现了 app 创建函数
"""
import os
from flask import Flask
import json

def create_app():
    """
    创建并初始化 Flask app
    """
    app = Flask('rmon')
    
    # 根据环境变量加载开发环境或生产环境配置
    env_file = os.environ.get('RMON_CONFIG')
    #file_path = './test.json'
    file_content = ''
    with open(env_file) as f:
        for i in f:
            i = i.strip()
            # 过滤 注释
            if i.startswith('#'):
                continue
            else:
                file_content += i
   
    JsonContent = json.loads(file_content)
    for key in JsonContent:
        print(key)
        app.config[key.upper()] = JsonContent.get(key)   
    return app
    
if __name__ == "__main__":
    create_app()
        
    
