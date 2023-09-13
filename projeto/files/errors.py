class FailureFunctionOrClass(Exception):...

def failure(f):
    def wrapper(*args, **kwargs):
        raise FailureFunctionOrClass(f"{f.__name__} is a flawed function or class")
    return wrapper