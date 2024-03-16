from datetime import datetime

def decorator_func(func):
    def wrapper(*args, **kwargs):
        print(f"function execution time: {datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')}")
        return func(*args, **kwargs)
    return wrapper

@decorator_func
def add_num(*args):
    print(sum(list(args)))

def multiply_num(a, b):
    return a * b

add_num(2, 3)