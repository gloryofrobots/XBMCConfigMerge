__author__ = 'human88998999877'
from XmlMerger.XmlMerger import XmlMerger
from FileSystem import FileSystem
from Error.ErrorHandler import ErrorHandler

from XmlMerger.MergeRule.MergeRuleFactory import MergeRuleFactory
from XmlMerger.MergeRule.MergeRuleSingleShot import MergeRuleSingleShot
from XmlMerger.MergeRule.MergeRuleSectionIntelligence import MergeRuleSectionIntelligence

from Graph.GraphQuery import GraphQuery


def merge(newConfigPath, oldConfigPath, destinationConfigPath, rulesPythonScript, isLogging, logDir, errorReporting, writeBackup):
    #register rules
    MergeRuleFactory.initialise()
    MergeRuleFactory.registerRule("CopyValue", MergeRuleSingleShot)
    MergeRuleFactory.registerRule("CopySection", MergeRuleSectionIntelligence)

    #register XmlMerger
    merger = XmlMerger()

    if merger.initErrorReporting(errorReporting) is False:
        print "Can`t init error reporting"
        return False
        pass

    if isLogging is True:
        if logDir is None:
            logDir = FileSystem.getCurrentDirectory()
            pass

        if FileSystem.isDirectory(logDir) is False:
            ErrorHandler.error("Directory for logs not exist %s " % logDir)
            return False
            pass

        if merger.initLogging(logDir) is False:
            ErrorHandler.error("can `t init Logger  ")
            return False
            pass
        
    if merger.initialise(newConfigPath, oldConfigPath) is False:
        ErrorHandler.error("can `t initialise")
        return False
        pass

    #add actions
    #BE CAREFUL TUPLE WITH ONE ELEMENT = (element,)  not (element) because in that case we shall have sequence (e,l,e,m,e,n,t) :-)
    #merger.addAction( "SingleShot", GraphQuery(("general","systemtotaluptime")) )
    #merger.addAction( "SectionIntelligence", GraphQuery(("myvideos",)) )
    #merger.addAction( "SectionIntelligence", GraphQuery(("mymusic",)), BlackList = ["scanning"] )
    #merger.addAction( "SectionIntelligence", GraphQuery(("viewstates",)) )
    content = FileSystem.fileGetContents(rulesPythonScript)

    execfile( rulesPythonScript, dict(merger = merger, GraphQuery = GraphQuery) )
    merger.merge()

    if writeBackup is True:
        backupPath = FileSystem.setFileExtension(oldConfigPath,"bak.xml")
        FileSystem.copyFile(oldConfigPath, backupPath)
        pass
    
    if merger.save(destinationConfigPath) is False:
        ErrorHandler.error("Error saving result %s. Please check  directory write permissions." % destinationConfigPath)
        return False
        pass

    return True
    pass
