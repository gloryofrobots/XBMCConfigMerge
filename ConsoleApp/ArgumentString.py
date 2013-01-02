__author__ = 'human88998999877'
from Argument import Argument

class ArgumentString(Argument):
    def _getData(self, args, index):
        self.value = args[index]
        return True
        pass
    pass