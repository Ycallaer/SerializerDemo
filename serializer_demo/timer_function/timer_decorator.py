from functools import wraps
from time import time


def timing(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        print('Function {}, Elapsed time: {}'.format(f.__name__,end-start))
        return result
    return wrapper