__author__ = 'human88998999877'
from Argument import Argument

class ArgumentMulti(Argument):
    def __init__(self, argName, description, possibleValues):
        super(ArgumentMulti,self).__init__(argName, description)
        self.possibleValues = possibleValues
        
        pass
    
    def _getData(self, args, index):
        val = args[index]
        for possiblePair in self.possibleValues:
            check = possiblePair[0]
            if check == val:
                self.value = possiblePair[1]
                return True
                pass
            pass

        return False
        pass
    pass