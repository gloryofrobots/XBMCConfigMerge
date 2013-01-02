class Argument(object):
    def __init__(self, argName, description, important = True):
        self.description = description
        self.argName = argName
        self.value = self._getDefault()
        self.important = important
        pass

    def _getDefault(self):
        return None
        pass
    
    def getInfo(self):
        template = "%s - %s"
        info =  template % (self.argName, self.description)

        argInfo = self._getInfo()
        if len(argInfo) > 0:
            info += ". " + argInfo
            pass
        
        return info
        pass

    def _getInfo(self):
        return ""
        pass

    def check(self, argName):
        if argName == self.argName:
            return True
            pass

        return False
        pass

    def getData(self, args):
        for i in range(len(args)):
            arg = args[i]
            
            if arg != self.argName:
                continue
                pass

            index = i + 1
            if index >= len(args):
                print (index,arg)
                return False
                pass

            if self._getData(args, index) is False:
                print( "error in argument %s" % arg)
                return False
                pass
            else:
                return True
                pass
            pass

        if self.important is True:
            print ("Can`t find argument %s" % self.argName)
            return False
            pass
        else:
            return True
            pass
        pass

    def _getData(self, args, index):
        raise BaseException("Abstract must be derived")
        pass
    
    def getValue(self):
        return self.value
        pass
    pass