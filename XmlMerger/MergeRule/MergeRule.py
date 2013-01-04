__author__ = 'human88998999877'
from Error.ErrorHandler import ErrorHandler

class MergeRule(object):
    def __init__( self ):
        super( MergeRule, self ).__init__()
        self._success = False
        pass

    def onParams( self, params ):
        self.name = params.pop( "Name", None )
        self.firstXmlInput = params.pop( "FirstXmlInput", None )
        self.secondXmlInput = params.pop( "SecondXmlInput", None )
        
        self._onParams( params )
        pass

    def run( self ):
        ErrorHandler.message( "%s is running" % str(self) )
        self._success =  self._onRun()
        return self._success
        pass

    def _onRun( self ):
        raise BaseException( "Abstract Must Be Derived" )
        pass

    def _onParams( self, params ):
        pass

    def isSuccess( self ):
        return self._success
        pass

    def getInfo(self):
        info = self._getInfo()
        return "<%s> :: %s" % ( self.__class__.__name__, info )
        pass

    def _getInfo(self):
        return ""
        pass

    def __repr__( self ):
        return self.getInfo()
        pass
    pass

