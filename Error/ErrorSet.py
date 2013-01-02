__author__ = 'human88998999877'
from ErrorType import ErrorType

FATAL_ERROR = -1
ERROR = 1
WARNING = 2
MESSAGE = 3
IMPORTANT_MESSAGE = 4


ERROR_SET_DEFAULT = {
                FATAL_ERROR : ErrorType(isPrinted = True, isLogged = True, isFatal = True, isRaiseException = False)
                ,ERROR : ErrorType(isPrinted = True, isLogged = True, isFatal = False, isRaiseException = True)
                ,WARNING : ErrorType(isPrinted = True, isLogged = True, isFatal = False, isRaiseException = False)
                ,IMPORTANT_MESSAGE: ErrorType(isPrinted = True, isLogged = True, isFatal = False, isRaiseException = False)
                ,MESSAGE: ErrorType(isPrinted = False, isLogged = False, isFatal = False, isRaiseException = False)
                }

ERROR_SET_SILENT = {
            FATAL_ERROR : ErrorType(isPrinted = False, isLogged = True, isFatal = True, isRaiseException = False)
            ,ERROR : ErrorType(isPrinted = False, isLogged = True, isFatal = False, isRaiseException = True)
            ,WARNING : ErrorType(isPrinted = False, isLogged = True, isFatal = False, isRaiseException = False)
            ,IMPORTANT_MESSAGE: ErrorType(isPrinted = False, isLogged = True, isFatal = False, isRaiseException = False)
            ,MESSAGE: ErrorType(isPrinted = False, isLogged = False, isFatal = False, isRaiseException = False)
            }

ERROR_SET_VERBOSE = {
            FATAL_ERROR : ErrorType(isPrinted = True, isLogged = True, isFatal = True, isRaiseException = False)
            ,ERROR : ErrorType(isPrinted = True, isLogged = True, isFatal = False, isRaiseException = True)
            ,WARNING : ErrorType(isPrinted = True, isLogged = True, isFatal = False, isRaiseException = False)
            ,IMPORTANT_MESSAGE: ErrorType(isPrinted = True, isLogged = True, isFatal = False, isRaiseException = False)
            ,MESSAGE: ErrorType(isPrinted = True, isLogged = True, isFatal = False, isRaiseException = False)
            }
