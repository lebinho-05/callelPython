class FilesException(BaseException):...

base = FilesException

class FailureFunctionOrClass(base):...

FFOC = FailureFunctionOrClass

def failure(f):
    def wrapper(*args, **kwargs):
        raise FailureFunctionOrClass(f"{f.__name__} is a flawed function or class")
    return wrapper

errors_list = {"FailureFunctionOrClass":FFOC}