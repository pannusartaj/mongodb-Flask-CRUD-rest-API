class BaseException(Exception):
    """ Redefine the BaseException class """
    status_code = 469

    def __init__(self, message, status_code=None):
        """ Init the BaseException class """
        super(BaseException, self).__init__(message)
        self.message = message
        if status_code is not None:
            self.status_code = status_code

class UnsupportedRequestError(BaseException):
    """ Set the 400 status code to the exceptions """
    status_code = 400
