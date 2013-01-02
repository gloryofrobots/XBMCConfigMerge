__author__ = 'human88998999877'
from ConsoleApp.ConsoleApp import ConsoleApp
from ConsoleApp.ArgumentString import ArgumentString
from ConsoleApp.ArgumentBool import ArgumentBool
from ConsoleApp.ArgumentMulti import ArgumentMulti
from Error.ErrorHandler import ERROR_REPORTING_DEFAULT,ERROR_REPORTING_SILENT,ERROR_REPORTING_VERBOSE

from Merge import merge

class XBMCConfigMergeConsoleApp(ConsoleApp):
    def __init__(self):
        super(XBMCConfigMergeConsoleApp, self).__init__()
        self._specialInfo = "XBMC Config merge command line tool. Usage  Python XBMCConfigMerge.py --arg1 val1 --arg2 val2"
        pass

    def _onRun(self):
        merge( self.getVal("--new_config")
               , self.getVal("--old_config")
               , self.getVal("--destination_config")
               , self.getVal("--rules_python_script")
               , self.getVal("--write_logs")
               , self.getVal("--log_dir")
               , self.getVal("--error_reporting")
               , self.getVal("--write_backup")
               )
        pass
    
    def _onInitialise(self):
        self.addArgument( ArgumentString("--new_config", "Path to new xbmc config file in xml format.") )
        self.addArgument( ArgumentString("--old_config", "Path to old xbmc config file in xml format.") )
        self.addArgument( ArgumentString("--destination_config", "Path to destination xbmc config file. In common case it will be xml tree from new config merged with xml tree of old config ") )
        self.addArgument( ArgumentString("--rules_python_script", "python script contains merging rules. see rulesExample.py") )
        self.addArgument( ArgumentBool("--write_logs","Logging  ") )
        self.addArgument( ArgumentBool("--write_backup","--old_config.bak.xml will be written", important = False) )
        self.addArgument( ArgumentString("--log_dir","Directory for writing log. if not specified and -write_logs is set current directory path is used ", important = False) )
        self.addArgument( ArgumentMulti("--error_reporting", "Error reporting mode. Possible values :\n" +
                                                    "    default - logged and printed errors, warnings and important messages. \n"
                                                    + "    silent - nothing printed. \n"
                                                    + "    verbose - all printed and logged\n",
            [ ("default", ERROR_REPORTING_DEFAULT ),
                ("silent", ERROR_REPORTING_SILENT ),
                ("verbose", ERROR_REPORTING_VERBOSE )]  ) )

        pass
    pass