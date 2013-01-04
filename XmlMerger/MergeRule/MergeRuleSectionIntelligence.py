__author__ = 'human88998999877'
from MergeRule import MergeRule
from Error.ErrorHandler import ErrorHandler

class MergeRuleSectionIntelligence(MergeRule):
    def _onRun( self ):
        self.merge(self.firstXmlInput, self.secondXmlInput)
        return True
        pass

    def _onParams( self, params ):
        blackList = params.pop("BlackList", None)
        self.blackList = []
        
        if blackList is None:
            return
            pass
        
        for query in blackList:
            result = query.execute(self.secondXmlInput)
            if result is None:
                ErrorHandler.warning("init black list error. graph query doesn`t work %s" % query)
                continue
                pass
            
            self.blackList.extend(result)
            pass
        pass

    def getSingles(self, section):
        singles = {}
        for tagName,nodes in section.items():
            if len(nodes) > 1:
                continue
                pass
            
            singles[tagName] = nodes[0]
            pass

        return singles
        pass

    def merge(self, node1, node2):
        #TODO VERY SLOW, IMPROVE SPEED
        isParent1 = node1.hasChildren()
        isParent2 = node2.hasChildren()

        if  isParent1 != isParent2:
            ErrorHandler.warning("MergeRuleSectionIntelligence:: nodes in different tree has different structure with same tagName new %s, old %s" % (node1,node2) )
            return
            pass

        if isParent1 is True:
            self._mergeSection(node1, node2)
            pass
        else:
            self._mergeNodes(node1, node2)
            pass
        pass

    def _isInBlackList(self, node):
        if self.blackList is None:
            return False
            pass

        for blackNode in self.blackList:
            if blackNode.isSameXmlNode(node) is True:
                return True
                pass
            pass

        return False
        pass
    
    def _mergeSection(self, node1, node2):
        section1 = node1.getChildrenGroups()
        section2 = node2.getChildrenGroups()
        
        section1Singles = self.getSingles(section1)
        section2Singles = self.getSingles(section2)

        for tagName2,node2 in section2Singles.items():
            if tagName2 not in section1Singles:
                continue
                pass

            if self._isInBlackList(node2) is True:
                continue
                pass

            node1 = section1Singles[tagName2]

            self.merge(node1, node2)
            pass
        pass

    def _mergeNodes(self, node1, node2):
        data2 = node2.getData()
        node1.setData(data2)
        pass
    pass