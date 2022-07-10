from redis_conf import redis
from redis_om import HashModel

class Post(HashModel):
    title: str
    content: str
    user_id: str

    class Meta:
        database = redis
