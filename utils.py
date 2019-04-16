from functools import wraps


def cache(func):
    cache_dict = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ in cache_dict:
            return cache_dict.get(func.__name__)
        else:
            cache_dict[func.__name__] = func(*args, **kwargs)
            return cache_dict.get(func.__name__)
    return wrapper
