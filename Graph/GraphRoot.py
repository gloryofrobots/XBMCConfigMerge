__author__ = 'human88998999877'
from Error.ErrorHandler import  ErrorHandler

class GraphRoot:
    def __init__(self, path):
        self.path = path
        pass

    def __repr__(self):
        className = str(self.__class__)
        return "GraphDocument %s  on   %s " % (className,self.path)
        pass

    def initialise(self):
        if self._onInitialise() is False:
            ErrorHandler.error(" Parser initialise`s failure on  %s" % self.__repr__())
            return False
            pass

        return True
        pass

    def finalise(self):
        if self._onFinalise() is False:
            ErrorHandler.error("Parser finalise`s failure on  %s", self.__repr__())
            return False
            pass

        return True
        pass

    def _onFinalise(self):
        raise BaseException("Abstract")
        pass

    def _onInitialise(self):
        raise BaseException("Abstract")
        pass
    pass