__author__ = 'human88998999877'
from Error.ErrorHandler import ErrorHandler

class GraphQuery(object):
    def __init__(self, path, Arg = None, Content = None, BackStep = 0):
        self.node = None
        self.path = path
        self.arg = Arg
        self.content = Content
        self.backStep = BackStep
        pass

    def length(self):
        return len(self.path)
        pass

    def isWell(self, node):

        if self.arg is not None:
            if node.hasAttribute(self.arg[0]) is False:
                return False
                pass

            if node.getAttribute(self.arg[0]) != str(self.arg[1]):
                return False
                pass
            pass

        if self.content is not None:
            if node.hasChildren() is True:
                return False
                pass
            
            if node.getData() != self.content:
                return False
                pass
            pass

        return True
        pass

    def prepareResult(self, result):
        children = result
        for i in range(self.backStep):
            parents = []
            for child in children:
                if child.hasParent() is False:
                    ErrorHandler.error("GrapQuery error backStep is incorrect. %i", self.backStep)
                    pass
                
                parent = child.getParent()
                parents.append(parent)
                pass
            children = parents
            pass

        return children
        pass
    
    def execute(self, node):
        tagName = self.path[0]
        children = node.getElementsByTagName(tagName)
        
        result = []
        
        if self.length() == 1:
            for child in children:
                if self.isWell(child) is False:
                    continue
                    pass

                result.append(child)
                pass
            pass
        else:
            for child in children:
                newPath = self.path[1:len(self.path)]
                query = GraphQuery(newPath, Arg = self.arg, Content = self.content, BackStep = self.backStep)
                inner = query.execute(child)

                if inner is None:
                    continue
                    pass
                
                inner = self.prepareResult(inner)
                result.extend(inner)
                pass
            pass

        if len(result) == 0:
            return None
            pass
        
        return result
        pass
    
    def __repr__(self):
        str = "GraphQuery :: "
        for part in self.path:
            str += part +", "
            pass

        return str[0:len(str) - 1]
        pass
    pass