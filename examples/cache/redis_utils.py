"""
Redis utils
"""
import redis

REDIS_HOST = "localhost"
REDIS_PORT = 6379


def redis_connect(host: str, port: int) -> redis.Redis:
    """
    Connect to Redis.
    :param host: Redis host
    :param port: Redis port
    :return: Redis client
    """
    return redis.Redis(host=host, port=port, decode_responses=True)
