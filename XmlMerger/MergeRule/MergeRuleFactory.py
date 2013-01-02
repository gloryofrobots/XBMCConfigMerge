__author__ = 'human88998999877'
from Error.ErrorHandler import ErrorHandler

class MergeRuleFactory:
    rules = {}

    @staticmethod
    def initialise():
        MergeRuleFactory.rules = {}
        pass
    
    @staticmethod
    def registerRule(name, classType):
        if MergeRuleFactory.hasRule( name ):
            ErrorHandler.error("MergeRuleFactory registerRule already has %s" % name)
            pass

        MergeRuleFactory.rules[name] = classType
        pass

    @staticmethod
    def hasRule(name):
        if name not in MergeRuleFactory.rules:
            return False
            pass

        return True
        pass

    @staticmethod
    def createRule(name):
        ruleClass = MergeRuleFactory.rules[name]
        rule = ruleClass()
        return rule
        pass

    @staticmethod
    def getRule(name, params):
        if MergeRuleFactory.hasRule(name) is False:
            ErrorHandler.error("MergeRuleFactory getRule unknown rule %s" %name)
            return None
            pass

        rule = MergeRuleFactory.createRule(name)
        rule.onParams(params)
        return rule
        pass
    pass

  