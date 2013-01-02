__author__ = 'human88998999877'


class GraphQuery(object):
    def __init__(self, path, Arg = None):
        self.node = None
        self.path = path
        self.arg = Arg
        pass

    def isEmpty(self):
        if len(self.path) == 0:
            return True
            pass
        
        return False
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

        return True
        pass
    
    def execute(self, node):
        self.node = node
        tagName = self.path[0]

        children = self.node.getElementsByTagName(tagName)
        
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
                query = GraphQuery(newPath, Arg = self.arg)
                inner = query.execute(child)

                if inner is None:
                    continue
                    pass
                
                result.extend(inner)
                pass
            pass

        if len(result) == 0:
            return None
            pass
        
        return result
        pass
    pass