from flask import request,g
from rmon.common.rest import Server,ServerSchema

class ServerList(RestView):
    """
    """
    def get(self):
        """
        """
        servers = Server.query.all()
        return ServerSchema().dump(servers,many=True).data
    
    def post(self):
        """
        """
        data = request.get_json()
        server,errors = ServerSchema().load(data)
        if errors:
            return errors,400
        server.ping()
        server.save()
        return {'ok':True},201
