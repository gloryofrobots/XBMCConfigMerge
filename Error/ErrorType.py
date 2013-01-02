__author__ = 'human88998999877'

class ErrorType:
    class Error:
        def __init__(self, message, isPrinted, isLogged, isFatal, isRaiseException):
            self.isPrinted = isPrinted
            self.isLogged = isLogged
            self.isFatal = isFatal
            self.isRaiseException = isRaiseException
            self.message = message
            pass

        def getMessage(self):
            return self.message
            pass
        pass

    def __init__(self, isPrinted = False, isLogged = True, isFatal = False, isRaiseException = False):
        self.isPrinted = isPrinted
        self.isLogged = isLogged
        self.isFatal = isFatal
        self.isRaiseException = isRaiseException
        pass

    def getError(self, message):
        error = ErrorType.Error(message, self.isPrinted, self.isLogged, self.isFatal, self.isRaiseException)
        return error
        pass
    pass