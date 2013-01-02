from FileSystem import FileSystem
from Error.Error import XBMConfigMergeError
import datetime

class Logger:
    def __init__(self):
        self.file = None
        self.fileName = None
        pass

    def getFileName(self):
        return self.fileName
        pass

    def initialise(self, pathToLogs):
        try:
            t = datetime.datetime.today()
            name = t.strftime("%Y_%m_%d_%H_%M")
            fileName = name + ".txt"
            filePath = FileSystem.joinPath(pathToLogs, fileName)

            self.file = open(filePath,'w+')
            self.fileName = fileName
            pass
        except BaseException as e:
            raise XBMConfigMergeError(e)
            pass
        pass

    def write(self,data):
        self.file.write(data+"\n")
        self.file.flush()
        pass
        
    def finalise(self):
        if self.file == None:
            return
            pass

        self.file.close()
        pass
    pass
