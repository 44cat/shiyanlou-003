from rmon.models import Server

class TestServer:
    """
    Test Server's releated ability
    """
    def test_save(self,db):
        """
        Test Server.save the way of saving Server
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
        Test Server.delete
        """
        assert Server.query.count() == 1
        server.delete()
        
        assert Server.query.count() == 0
