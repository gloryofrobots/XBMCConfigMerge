__author__ = 'human88998999877'
from MergeRule.MergeRuleFactory import MergeRuleFactory

from Error.ErrorListener import ErrorListener
from Error.ErrorHandler import ErrorHandler
from Logger import Logger
from Graph.GraphRootXmlDom import GraphRootXmlDom

QUERY_POLICY_BOTH = 1
QUERY_POLICY_ONLY_NEW = 2

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

    def addAction(self, ruleName, query, Policy = QUERY_POLICY_BOTH, **params):
        action = dict( Query = query, RuleName = ruleName, Params = params, Policy = Policy  )
        self.actions.append(action)
        pass

    def save(self, path):
        return self.firstXml.save(path)
        pass


    def _initActionBoth(self, action, query, firstDomRoot, secondDomRoot ):
        firstResult = query.execute(firstDomRoot)
        if firstResult is None:
            ErrorHandler.warning( "xml query failed %s  on %s" % (query, self.firstXml) )
            return False
            pass

        secondResult = query.execute(secondDomRoot)
        if secondResult is None:
            ErrorHandler.warning( "xml query failed %s  on %s" % (query, self.secondXml) )
            return False
            pass

        if len(secondResult) != len(firstResult):
            ErrorHandler.warning( "xml query %s results have incompatible length  %i != %i"
            % (query,  len(secondResult),len(firstResult) ) )
            return False
            pass

        if len(secondResult) != 1:
            ErrorHandler.warning( "xml query %s only single row result supported , you got %i"
            % (query,  len(secondResult) ) )
            return False
            pass

        action["Params"]["FirstXmlInput"] = firstResult[0]
        action["Params"]["SecondXmlInput"] = secondResult[0]
        return True
        pass

    def _initActionFirst(self, action, query, firstDomRoot ):
        firstResult = query.execute(firstDomRoot)
        if firstResult is None:
            ErrorHandler.warning( "xml query failed %s  on %s" % (query, self.firstXml) )
            return False
            pass

        if len(firstResult) != 1:
            ErrorHandler.warning( "xml query %s only single row result supported , you got %i"
            % (query,  len(firstResult) ) )
            return False
            pass

        action["Params"]["FirstXmlInput"] = firstResult[0]
        return True
        pass
    
    def merge(self):
        firstDomRoot = self.firstXml.getRootNode()
        secondDomRoot = self.secondXml.getRootNode()

        for action in self.actions:
            query = action["Query"]

            if action["Policy"] == QUERY_POLICY_BOTH:
                if self._initActionBoth(action, query, firstDomRoot, secondDomRoot) is False:
                    continue
                    pass
                pass
            elif action["Policy"] == QUERY_POLICY_ONLY_NEW:
                if self._initActionFirst(action, query, firstDomRoot) is False:
                    continue
                    pass
                pass
            else:
                ErrorHandler.error("Merge Query Policy not Support %s" % str(action["Policy"]) )
                continue
                pass

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

