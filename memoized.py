#-*-encoding=utf-8-*-
"""
Universal Memoization Decorator module
"""
import functools
import pickle


def memoize_all(func):
    cache = {}

    @functools.wraps(func)
    def cached(*args, **kwargs):
        arg_names = func.func_code.co_varnames
        arg_dict = dict(zip(arg_names, args), **kwargs)
        key = pickle.dumps(arg_dict)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return cached
