__author__ = 'human88998999877'
from UsageException import UsageException

class ConsoleApp(object):
    def __init__(self):
        super(ConsoleApp,self).__init__()
        self.arguments = []
        self._specialInfo = "" 
        pass

    def addArgument(self,argument):
        self.arguments.append(argument)
        pass

    def parse(self, args):
        for argument in self.arguments:
            if argument.getData(args) is False:
                return False
                pass
            pass

        return True
        pass

    def getVal(self, argName):
        for argument in self.arguments:
            if argument.check(argName) is True:
                return argument.getValue()
                pass
            pass
        
        raise ValueError(argName)
        pass

    def help(self):
        info = self._specialInfo + "\n\n"

        for argument in self.arguments:
            info += argument.getInfo() + "\n\n"
            pass

        info += "--help - this message\n\n"
        print info
        pass


    def _onInitialise(self):
        raise BaseException("ABSTRACT")
        pass

    def initialise(self):
        self._onInitialise()
        pass

    def _onRun(self):
        raise BaseException("ABSTRACT")
        pass
        
    def run(self, *args):
        if len(args) == 1:
            if args[0] == "--help":
                self.help()
                return
                pass
            pass

        if self.parse(args) is False:
            raise UsageException( "Command line arguments error!" )
            return -1
            pass

        self._onRun()
        pass
    pass



    


    
