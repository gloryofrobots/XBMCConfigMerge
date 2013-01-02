from xml.dom.minidom import  parse
import xml.parsers.expat

from Error.ErrorHandler import  ErrorHandler

from Graph.GraphRoot import GraphRoot
from Graph.GraphNodeXmlDom import GraphNodeXmlDom
from FileSystem import FileSystem

class GraphRootXmlDom(GraphRoot):
    def _onInitialise(self):
        self.documentXmlDom = self.openDocument(self.path)

        if self.documentXmlDom is None:
            return False
            pass

        return True
        pass

    def openDocument(self, pathToXml):
        document = None

        try:
            document = parse(pathToXml)
            pass
        except IOError as e:
            message = "Parser.parseToDom IOError %s in %s " % ( str(e) ,self )
            ErrorHandler.warning(message)
            return None
            pass
        except xml.parsers.expat.ExpatError as e:
            message = "Parser.parseToDom xml.parsers.expat.ExpatError %s in %s " % (str(e) , self )
            ErrorHandler.warning(message)
            return None
            pass

        return document
        pass

    def _onFinalise(self):
        return True
        pass

    def getRootNode(self):
        rootElement = GraphNodeXmlDom(self.documentXmlDom.documentElement)
        return rootElement
        pass

    def save(self, path):
        root = self.documentXmlDom.documentElement
        xml = root.toprettyxml( encoding='UTF-8', indent="", newl="" )
        #xml = root.toxml( encoding='UTF-8')
        result = FileSystem.filePutContents( path, xml )
        return result
        pass

    #TODO CHECK WRITEXML and ENCODING in OPEN
    def save2(self, path):
        root = self.documentXmlDom.documentElement
        file = open(path,"wb")
        root.writexml(file)
        file.close()
        return True
        pass
    pass



  