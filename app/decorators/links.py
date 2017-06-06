from flask import url_for
from functools import wraps

def permalink(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        endpoint, parameter = function(*args, **kwargs)
        return url_for(endpoint,parameter)
    return wrapper