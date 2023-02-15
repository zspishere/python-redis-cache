from pickle import dumps, loads
from redis import StrictRedis
from redis_cache import RedisCache

REDIS_URI='redis://iipharma:NZvMh7iNTT9@r-2zeitxtlflpfmgamhipdtt.redis.rds.aliyuncs.com:9999/11'
client = StrictRedis.from_url(REDIS_URI)
cache = RedisCache(redis_client=client, prefix='shu', serializer=dumps, deserializer=loads)


@cache.cache(ttl=30)
def my_func(arg1, arg2):
    result = {'xxss': f'{arg1}-{arg2}'}
    return result

# Use the function
my_func(1, 2)

# Call it again with the same arguments and it will use cache
my_func(1, 2)


# Use the function
my_func(2, 3)

res = cache.mget(*[
    {"fn": my_func, "args": [1,2]},
    {"fn": my_func, "args": [2,4]},
    {"fn": my_func, "args": [2,3]}
])
print(res)

key = my_func.get_key([1,2], {})
value = my_func.get_value([1,2], {})
ttl = my_func.get_ttl([1,2], {})
print('key', key)
print('value', value)
print('ttl', ttl)

# Invalidate a single value
# my_func.invalidate(1, 2)
# my_func.invalidate(2, 3)

# # Invalidate all values for function
# my_func.invalidate_all()