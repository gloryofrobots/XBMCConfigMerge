
ERROR_REPORTING_SILENT = 1
ERROR_REPORTING_VERBOSE = 2
ERROR_REPORTING_DEFAULT = 3

from ErrorSet import FATAL_ERROR,ERROR,WARNING,MESSAGE,IMPORTANT_MESSAGE
from ErrorSet import ERROR_SET_DEFAULT,ERROR_SET_VERBOSE,ERROR_SET_SILENT

class ErrorHandler:

    errorLabels = {
                    FATAL_ERROR:"FATAL_ERROR ",
                    ERROR:"ERROR ",
                    WARNING:"WARNING ",
                    MESSAGE : "MESSAGE",
                    IMPORTANT_MESSAGE : "MESSAGE"
                   }

    errorSet = ERROR_SET_DEFAULT
    
    listeners = []

    @staticmethod
    def setErrorReporting(mode):
        if mode == ERROR_REPORTING_DEFAULT:
            ErrorHandler.errorSet = ERROR_SET_DEFAULT
            pass
        elif mode == ERROR_REPORTING_SILENT:
            ErrorHandler.errorSet = ERROR_SET_SILENT
            pass
        elif mode == ERROR_REPORTING_VERBOSE:
            ErrorHandler.errorSet = ERROR_SET_VERBOSE
            pass
        pass
    
    @staticmethod
    def addListener(listener):
        ErrorHandler.listeners.append(listener)
        pass

    @staticmethod
    def removeListener(listener):
        ErrorHandler.listeners.remove(listener)
        pass

    @staticmethod
    def setLoggedError(errorType,state):
        ErrorHandler.errorSet[errorType].isTraced = state
        pass

    @staticmethod
    def setPrintError(errorType,state):
        ErrorHandler.errorSet[errorType].isPrinted = state
        pass

    @staticmethod
    def setFatalError(errorType,state):
        ErrorHandler.errorSet[errorType].isFatal = state
        pass

    @staticmethod
    def error(message):
        errorType = ERROR
        ErrorHandler.__processError(errorType,message)
        pass

    @staticmethod
    def warning(message):
        errorType = WARNING
        ErrorHandler.__processError(errorType,message)
        pass

    @staticmethod
    def message(message):
        errorType = MESSAGE
        ErrorHandler.__processError(errorType,message)
        pass

    @staticmethod
    def abort(message):
        errorType = FATAL_ERROR
        ErrorHandler.__processError(errorType,message)
        pass

    @staticmethod
    def importantMessage(message):
        errorType = IMPORTANT_MESSAGE
        ErrorHandler.__processError(errorType,message)
        pass

    @staticmethod
    def __processError(errorType,message):
        messageStr = str(message)
        label = ErrorHandler.errorLabels[errorType]
        traceMessage  =  "%s %s" % (label, messageStr)

        Type = ErrorHandler.errorSet[errorType]
        error = Type.getError(traceMessage)

        for listener in ErrorHandler.listeners:
            listener.onError(error)
            pass
        pass
    pass