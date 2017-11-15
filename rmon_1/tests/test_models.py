#-*- coding:utf-8 -*-
from rmon.models import Server

class TestServer:
    """
    测试 Server's 相关功能
    """
    def test_save(self,db):
        """
        测试 Server.save 
        """
        # The Initial state.DataBase save nothing,so, Redis is 0 in database.
        assert Server.query.count() == 0
        server = Server(name='test',host='127.0.0.1')
        # Save redis to database
        server.save()
        # Now,database has one redis.
        assert Server.query.count() == 1
        # And,in the database,record is the record of perviously created.
        assert Server.query.first() == server
        
    def test_delete(self,db,server):
        """
        测试 Server.delete
        """
        assert Server.query.count() == 1
        server.delete()
        
        assert Server.query.count() == 0
        
    def test_ping_success(self,db,server):
        """
        测试 Server.ping 方法执行成功
        
        需要保证Redis 服务器监听在127.0.0.1地址
        """
        assert server.ping() is True
    
    def test_ping_success(self,db,server):
        """
        测试 Server.ping 方法执行失败
        
        Server.ping 方法执行失败时，会抛出 RestException 异常
        
        """
        # 没有 Redis服务器监听在127.0.0.1:6399 地址，所以将访问失败
        server = Server(name='test',host='127.0.0.1',port=6399)
        try:
            server.ping()
        except RestException as e:
            assert e.code == 400
            assert e.code == 'redis server %s can not connected'%server.host

        
        
