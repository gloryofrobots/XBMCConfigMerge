__author__ = 'human88998999877'

from Error import XBMConfigMergeError
import os

class ErrorListener(object):
    def __init__(self):
        self.logger = None
        pass

    def setLogger(self, logger):
        self.logger = logger
        pass
    
    def onError(self, error):
        message = error.getMessage()

        if error.isPrinted is True:
            print (message)
            pass

        if error.isLogged is True and self.logger is not None:
            self.logger.write(message)
            pass
        
        if error.isRaiseException is True:
            raise XBMConfigMergeError(message)
            pass

        if error.isFatal is True:
            os._exit(-1)
            pass
        pass
    pass
