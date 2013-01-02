__author__ = 'human88998999877'
from Argument import Argument

class ArgumentInt(Argument):
    def _getData(self, args, index):
        try:
            self.value = int(args[index])
            pass
        except BaseException as e:
            return False
            pass

        return True
        pass
    pass