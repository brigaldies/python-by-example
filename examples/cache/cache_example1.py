"""
Redis usage 1:
- Connect
- Run INFO keyspace
- Delete all keys
- Run set and get
- Run hset, hget, and hgetall
- Retrieve existing keys
"""

import argparse
import logging

import redis

from examples.cache.redis_utils import REDIS_HOST, REDIS_PORT, redis_connect

LOG = logging.getLogger("examples")


def cache_example1(args: argparse.Namespace) -> None:
    """
    Run Redis usage example 1.
    :param args: Command-line args.
    :return: None.
    """
    redis_db_number = 0
    redis_client = cache_connect()

    assert cache_select(redis_client, redis_db_number)

    assert delete_all_keys(redis_client, redis_db_number)

    # Set and get a key-value
    cache_set_get(redis_client)

    # Hset and hget a dictionary
    cache_hset_hget(redis_client)

    # Retrieve the keys (do not do this in a Production system!)
    keys = redis_client.keys()
    assert len(keys) > 0
    for key in keys:
        LOG.info("key: %s", key)


def cache_connect() -> redis.Redis:
    """
    Connect to Redis and return a redis client instance.
    :return: Redis client instance.
    """
    LOG.info("Connecting to Redis at host=%s, port=%d", REDIS_HOST, REDIS_PORT)
    redis_client: redis.Redis = redis_connect(host=REDIS_HOST, port=REDIS_PORT)
    assert redis_client is not None

    LOG.info("Retrieving the Redis keyspace information...")
    keyspace = redis_client.info("keyspace")
    LOG.info("Keyspace: %s", str(keyspace))

    return redis_client


def cache_select(redis_client: redis.Redis, redis_db_number: int) -> bool:
    """
    Select a cache.
    :param redis_client: Redis client instance
    :param redis_db_number: Redis database number
    :return: True if success, False, otherwise.
    """
    # Select database 0 (default)
    LOG.info("Selecting database %d...", redis_db_number)
    select = redis_client.select(redis_db_number)
    LOG.info("Database selection: %s", str(select))
    assert select
    return select


def delete_all_keys(redis_client: redis.Redis, redis_db_number: int) -> bool:
    """
    Delte all keys in a Redis db
    :param redis_db_number:
    :param redis_client:
    :return:
    """
    assert redis_client.select(redis_db_number)
    assert redis_client.flushdb(asynchronous=False)
    return True


def cache_set_get(redis_client: redis.Redis) -> None:
    """
    Example of a set and get
    :param redis_client: Redis client
    :return: None
    """
    # Set a key-value
    # Good key design practice: Use of prefix to denote different namespaces
    # Note: Redis functions within a flat namespace which mean that all keys share a single global namespace
    user_key = "user:231:name"
    return_value = redis_client.set(user_key, "Bertrand")
    LOG.info("Set returned value: %s", str(return_value))
    assert redis_client.exists(user_key)
    assert "Bertrand" == redis_client.get(user_key)


def cache_hset_hget(redis_client: redis.Redis) -> None:
    """
    Example of hset and hget to store and retrieve dictionaries
    :param redis_client: Redis client.
    :return: None.
    """
    # With hset, with allows the storing of dictionaries, and retrieval of individual dict keys
    return_value = redis_client.hset('user:231', mapping={
        'name': 'John',
        "surname": 'Smith',
        "company": 'Redis',
        "age": 29
    })
    LOG.info("Hset returned value: %s", str(return_value))
    # Return value is the number hashed fields ???
    # assert 4 == return_value
    name = redis_client.hget('user:231', 'name')
    assert 'John' == name, f"Unexpected hget-retrieved name {name}"
    surname = redis_client.hget('user:231', 'surname')
    assert 'Smith' == surname, f"Unexpected hget-retrieved surname {surname}"

    # Retrieved all hashed fields
    return_value = redis_client.hgetall('user:231')
    LOG.info("hgetcall returned value: %s", return_value)
    assert isinstance(return_value, dict)

    assert 'name' in return_value.keys()
    assert 'John' == return_value['name']

    assert 'surname' in return_value.keys()
    assert 'Smith' == return_value['surname']

    assert 'company' in return_value.keys()
    assert 'Redis' == return_value['company']

    assert 'age' in return_value.keys()
    assert isinstance(return_value['age'], str)
    assert 29 == int(return_value['age'])
