__author__ = 'human88998999877'
from XBMCConfigMergeConsoleApp import XBMCConfigMergeConsoleApp
from ConsoleApp.UsageException import UsageException
from Error.Error import XBMConfigMergeError
#TODO ERRORS !!!!!!!
import sys

def main(argv = None):
    app = XBMCConfigMergeConsoleApp()
    app.initialise()

    if argv is None:
        argv = sys.argv
        pass
    result = app.run( *argv[1:] )
    return result

#    try:
#        result = app.run( *argv[1:] )
#        return result
#        pass
#    except Exception, err:
#        raise err
#        print >>sys.stderr, err
#        app.help()
#        return 2
#        pass

if __name__ == "__main__":
    sys.exit(main())
    pass