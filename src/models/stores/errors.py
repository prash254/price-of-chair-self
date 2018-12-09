__author__ = 'sp'


class StoreException(Exception):
    def __iter__(self, message):
        self.message = message


class StoreNotFoundException(StoreException):
    pass
