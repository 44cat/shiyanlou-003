import json
import redis
from functools import wraps

class RedisCache:
    def __init__(self,redis_client):
        self._redis = redis_client
        
    def cache(self,timeout=0):
        def decorator(f):
            @wraps(f)
            def wrapped(*args,**kwargs):
                if timeout == 0:
                    return f(*args,**kwargs)
                key = f.__name__
                raw = self._redis.get(key)
                if not raw:
                    value = f(*args,**kwargs)
                    self._redis.setex(key,timeout,json.dumps(value))
                    return value
                else:
                    return json.loads(raw)
            return wrapped
        return decorator

if __name__ == "__main__":
    cli = redis.StrictRedis(host='127.0.0.1')
    cache = RedisCache(cli)
    
    @cache.cache(timeout=10)
    def excute():
        return 'hello world'
    result = excute()
    cache_result = json.loads(cli.get(excute.__name__).decode())
    print('cache result',cache_result)
    print('ttl of cache',cli.ttl(excute.__name__))
    assert cache_result == result
