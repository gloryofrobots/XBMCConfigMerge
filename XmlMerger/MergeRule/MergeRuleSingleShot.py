__author__ = 'human88998999877'
from MergeRule import MergeRule

class MergeRuleSingleShot(MergeRule):
    def _onRun( self ):
        oldData =  self.secondXmlInput.getData()

        result = self.firstXmlInput.setData(oldData)
        return result
        pass
    pass