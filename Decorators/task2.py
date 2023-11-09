

#Write a decorator that takes a list of stop words and replaces them with * inside the decorated function


def stop_words(stop_words_list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for stop_word in stop_words_list:
                result = result.replace(stop_word, '*')
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
