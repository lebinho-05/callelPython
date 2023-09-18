from .files.errors import failure
from .files import errors

class Code:
    def __init__(self):
        global PersonalizeException

        class ErrorsException(BaseException):...
        class PersonalizeException(BaseException):...

        errors.base = ErrorsException

        self.r = errors.errors_list

    @staticmethod
    def __getitem__(key):
        key = ((key.replace("(", " ")).replace(")", "")).split()
        if key[0] in errors.errors_list:
            e = errors.errors_list[key[0]]
            raise e(key[1])
    
    @staticmethod
    def __setitem__(key, cls):
        errors.errors_list[key] = cls

ers = Code()