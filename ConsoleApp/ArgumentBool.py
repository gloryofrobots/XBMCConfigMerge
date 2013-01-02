__author__ = 'human88998999877'
from Argument import Argument

class ArgumentBool(Argument):
    def _getInfo(self):
        return "Possible values : disable or enable"
        pass

    def _getDefault(self):
        return False
        pass

    def _getData(self, args, index):
        val = args[index]
        if val == "enable":
            self.value = True
            return True
            pass
        elif val == "disable":
            return True
            pass
        
        return False
        pass
    pass