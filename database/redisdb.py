import redis
from decouple import config

redis_client = redis.StrictRedis(host=config('REDIS_HOST'), port=6379, db=0)

