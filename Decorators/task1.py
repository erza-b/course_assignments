#Task 1

#Write a decorator that prints a function with arguments passed to it.

#NOTE! It should print the function, not the result of its execution!

def logger(func):
    def wrapper(*args, **kwargs):
        arg_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f'{key}={repr(value)}' for key, value in kwargs.items()])
        all_args = ', '.join(filter(None, [arg_str, kwargs_str]))
        print(f"{func.__name__} called with {all_args}")
        return func(*args, **kwargs)
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]
