from Graph.GraphNode import GraphNode
from xml.dom.minidom import Node

class GraphNodeXmlDom(GraphNode):
    def __init__(self, nodeXmlDom):
        super(GraphNode, self).__init__()
        self.nodeDom = nodeXmlDom
        pass

    def getXmlDomElement(self):
        return self.nodeDom
        pass

    def isSameXmlNode(self, node2):
        nodeDom2 = node2.getXmlDomElement()
        if nodeDom2 == self.nodeDom:
            return True
            pass

        return False
        pass

    def getParent(self):
        return GraphNodeXmlDom(self.nodeDom.parentNode)
        pass

    def getChildren(self):
        #return  [ GraphNodeXmlDom(child) for child in self.nodeDom.childNodes if "tagName" in child.__dict__ ]
        #CAREFUL WITH THAT AXE EUGENE ->  if child.nodeType == Node.ELEMENT_NODE
        return  [ GraphNodeXmlDom(child) for child in self.nodeDom.childNodes if child.nodeType == Node.ELEMENT_NODE ]
        pass

    def getChildrenGroups(self):
        children = {}
        for child in self.nodeDom.childNodes:
            if child.nodeType != Node.ELEMENT_NODE:
                continue
                pass

            node = GraphNodeXmlDom(child)
            tagName = node.getTagName()
            if tagName is None:
                continue
                pass

            if tagName not in children:
                children[tagName] = []
                pass

            children[tagName].append( node )
            pass
        
        return children
        pass

    #VERY SLOW FUCK MOTHERFUCK
    def hasChildren(self):
        return len(self.getChildren()) != 0
        #return self.nodeDom.hasChildNodes()
        pass

    def getTagName(self):
        if "tagName" not in self.nodeDom.__dict__:
            return None
            pass
        
        return self.nodeDom.tagName
        pass

    def getElementsByTagName(self, tagName):
        return  [ GraphNodeXmlDom(child) for child in self.nodeDom.getElementsByTagName(tagName) ]
        pass

    def getAttribute(self, attrName):
        return self.nodeDom.getAttribute(attrName)
        pass

    def hasAttribute(self, attrName):
        return self.nodeDom.hasAttribute(attrName)
        pass

    def removeAttribute(self, attrName):
        self.nodeDom.removeAttribute(attrName)
        pass

    def setAttribute(self, attrName, val):
        self.nodeDom.setAttribute(attrName, val)
        pass

    def hasParent(self):
        if self.nodeDom.parentNode is None:
            return False
            pass

        return True
        pass
        
    def removeFromParent( self ):
        if self.hasParent() is False:
            return False
            pass
        
        self.nodeDom.parentNode.removeChild(self.nodeDom)
        return True
        pass

    def getData(self):
        try:
            if self.nodeDom.firstChild.nodeType != Node.TEXT_NODE:
                return None
                pass

            return self.nodeDom.firstChild.data
            pass
        except Exception,e:
            return None
            pass
        pass

    def setData(self, data):
        try:
            if self.nodeDom.firstChild.nodeType != Node.TEXT_NODE:
                return False
                pass

            self.nodeDom.firstChild.data = data
            return True
            pass
        except Exception,e:
            return False
            pass
        pass

    def __repr__(self):
        return "%s :: Tag %s" % (str(self.__class__) ,self.getTagName())
        pass
    pass
