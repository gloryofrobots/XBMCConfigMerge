__author__ = 'human88998999877'
from MergeRule.MergeRuleFactory import MergeRuleFactory

from Error.ErrorListener import ErrorListener
from Error.ErrorHandler import ErrorHandler
from Logger import Logger
from Graph.GraphRootXmlDom import GraphRootXmlDom

class XmlMerger(object):
    def __init__(self):
        super(XmlMerger,self).__init__()
        self.actions = []
        self.errorListener = ErrorListener()
        self.firstXml = None
        self.secondXml = None
        pass

    def initialise(self, firstXmlPath, secondXmlPath):
        self.firstXml = GraphRootXmlDom(firstXmlPath)
        if self.firstXml.initialise() is False:
            return False
            pass

        self.secondXml = GraphRootXmlDom(secondXmlPath)
        if self.secondXml.initialise() is False:
            return False
            pass

        return True
        pass

    def initErrorReporting(self, errorReporting):
        ErrorHandler.addListener(self.errorListener)
        ErrorHandler.setErrorReporting(errorReporting)

        return True
        pass

    def initLogging(self, logDir):
        logger = Logger()
        logger.initialise(logDir)

        ErrorHandler.importantMessage("Log created  %s" % logger.getFileName() )
        self.errorListener.setLogger(logger)

        return True
        pass

    def addAction(self, ruleName, query, **params):
        action = dict( Query = query, RuleName = ruleName, Params = params )
        self.actions.append(action)
        pass

    def save(self, path):
        return self.firstXml.save(path)
        pass

    def merge(self):
        firstDomRoot = self.firstXml.getRootNode()
        secondDomRoot = self.secondXml.getRootNode()

        for action in self.actions:
            query = action["Query"]

            firstResult = query.execute(firstDomRoot)
            if firstResult is None:
                ErrorHandler.warning( "xml query failed %s  on %s" % (query, self.firstXml) )
                continue
                pass
            
            secondResult = query.execute(secondDomRoot)
            if secondResult is None:
                ErrorHandler.warning( "xml query failed %s  on %s" % (query, self.secondXml) )
                continue
                pass

            if len(secondResult) != len(firstResult):
                ErrorHandler.warning( "xml query %s results have incompatible length  %i != %i"
                % (query,  len(secondResult),len(firstResult) ) )
                continue
                pass
            
            if len(secondResult) != 1:
                ErrorHandler.warning( "xml query %s only single row result supported , you got %i"
                % (query,  len(secondResult) ) )
                continue
                pass

            action["Params"]["FirstXmlInput"] = firstResult[0]
            action["Params"]["SecondXmlInput"] = secondResult[0]

            rule = MergeRuleFactory.getRule( action["RuleName"],  action["Params"] )
            if rule is None:
                ErrorHandler.warning( "Merge rule %s  don`t exist" % action["RuleName"])
                continue
                pass

            if rule.run() is False:
                ErrorHandler.warning( "Merge rule return False %s %s" % (action["RuleName"], query) )
                pass
            pass
        pass
    pass

