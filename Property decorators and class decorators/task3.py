#Task3

#Write a class TypeDecorators which has several methods for converting results of functions to a specified type (if it's possible):

#methods:

#to_int

#to_str

#to_bool

#to_float

 
from functools import wraps

class TypeDecorators:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return int(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return str(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return bool(func(*args, **kwargs))

        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return float(func(*args, **kwargs))

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
