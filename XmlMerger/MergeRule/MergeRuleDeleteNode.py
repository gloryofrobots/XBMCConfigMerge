__author__ = 'human88998999877'
from MergeRule import MergeRule

class MergeRuleDeleteNode(MergeRule):
    def _onRun( self ):
        return self.firstXmlInput.removeFromParent()
        pass
    pass