from .files.errors import failure
from .files import errors

class Code:
    def __init__(self):
        global PersonalizeException

        class ErrorsException(BaseException):...
        class PersonalizeException(BaseException):...

        errors.base = ErrorsException

        self.r = errors.errors_list

    def __getitem__(self, __name):
        return self.r[__name]
    
    def __setitem__(self, __name, cls):
        self.r[__name] = cls

ers = Code()
