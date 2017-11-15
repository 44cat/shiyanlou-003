#-*-coding:utf-8-*-
"""
rmon.model
该模块实现了所有model类以及相应的序列化类
"""
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from redis import StrictRedis,RedisError
from rmon.common.rest import RestException

db = SQLAlchemy()


class Server(db.Model):
    """
    Redis 服务器模型
    """
    __tablename__ = 'redis_server'
    id = db.Column(db.Integer,primary_key=True)
    
    name = db.Column(db.String(64),unique=True)
    description = db.Column(db.String(512))
    host = db.Column(db.String(15))
    port = db.Column(db.Integer,default=6379)
    password = db.Column(db.String())
    updated_at = db.Column(db.DateTime,default=datetime.utcnow)
    created_at = db.Column(db.DateTime,default=datetime.utcnow)
    
    def __repr__(self):
        return '<Server(name=%s)>'%self.name
        
    def save(self):
        """
        保存到数据库
        """
        db.session.add(self)
        db.session.commit()
        
    def delete(self):
        """
        从数据库中删除
        """
        db.session.delete(self)
        db.session.commit()
    
    """
    下面两个方法都需要使用 Redis服务器客户端 链接到 Redis服务器，
    在Python 中访问Redis服务器可以用 redis-py软件包。
    所以在下面添加一个 redis属性 代表对应的客户端。(在上面导入相应模块)
    """
    @property
    def redis(self):
        return StrictRedis(host=self.host,port=self.port,password=self.password)

    def ping(self):
        """
        检查 Redis 服务器是否可以正常链接访问
        """
        try:
            return self.redis.ping()
        except RedisError:
            raise RestException(400,'redis server %s can not connected'%self.host)


    def get_metrics(self):
        """
        获取 Redis 服务器监控信息
        通过Redis 服务器指令 INFO 返回监控信息,参考https://redis.io/commands/INFO
        """
        try:
            return self.redis.info()
        except RedisError:
            raise RestException(400,'redis server %s can connected'%self.host)





