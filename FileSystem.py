import os
import os.path
import shutil
import distutils.dir_util 
import filecmp

class FileSystem:
    @staticmethod
    def absolutePath(path):
        abspath = os.path.abspath(path)
        return abspath
        pass

    @staticmethod
    def openFile(path,mode):
        file = open(path,mode)
        return file
        pass

    @staticmethod
    def getFileExtension(path):
        pathData = os.path.splitext(path)
        if len(pathData)!=2:
            return None
            pass

        ext = pathData[1]
        ext = ext[1:len(ext)]
        return ext.lower()
        pass

    @staticmethod
    def setFileExtension(path, newExt):
        pathData = os.path.splitext(path)
        if len(pathData) != 2:
            return None
            pass
        
        basePart =  pathData[0]
        return  basePart + "." + newExt
        pass

    @staticmethod
    def splitByExtension(path):
        pathData = os.path.splitext(path)
        return pathData
        pass

    @staticmethod
    def removeFile(path):
        os.remove(path)
        pass
    
    @staticmethod
    def normalisePath(path):
        normpath = os.path.normpath(path)
        return normpath
        pass

    @staticmethod
    def getPathDifference(pathLarge, pathSmall):
        pathLargeN = FileSystem.normalisePath(pathLarge)
        pathSmallN = FileSystem.normalisePath(pathSmall)
        pathLargeN.replace(pathSmallN)
        pass

    @staticmethod
    def pathStepBackWard(path, countSteps):
        result = FileSystem.normalisePath(path)

        while True:
            if countSteps <= 0:
                break
                pass

            countSteps -= 1
            result = FileSystem.getDirname(result)
            pass
        
        return result
        pass

    @staticmethod
    def joinPath(path1,path2):
        path = os.path.join(path1,path2)
        return path
        pass
        
    @staticmethod
    def joinAndNormalisePath(path1,path2):
        path = os.path.join(path1,path2)
        path = FileSystem.normalisePath(path)
        return path
        pass
    
    @staticmethod
    def getDirname(path):
        dirname = os.path.dirname(path)
        return dirname
        pass
    
    @staticmethod
    def getBasename(path):
        basename = os.path.basename(path)
        return basename
        pass

    @staticmethod
    def splitPath(path):
        parts =  os.path.split(path)
        return parts
        pass

    @staticmethod
    def isDirectory(path):
        isDir = os.path.isdir(path)
        return  isDir
        pass
        
    @staticmethod
    def isFile(path):
        state = os.path.isfile(path)
        return  state
        pass

    @staticmethod
    def filePutContents(filename, content, mode = "wb"):
        try:
            file = open(filename,mode)
            file.write(content)
            file.close()
            return True
            pass
        except Exception:
            return False
            pass
        pass

    @staticmethod
    def fileGetContents(filename):
        file = open(filename,"r")
        content = file.read()
        file.close()
        return content
        pass

    @staticmethod
    def makeDirsRecursiveIfNotExist(path):
        if len(path) == 0:
            return
            pass

        if FileSystem.isDirectory(path) is True:
            return
            pass

        FileSystem.makeDirsRecursive(path)
        pass

    @staticmethod
    def makeDirsRecursive(path):
        os.makedirs(path)
        pass
        
    @staticmethod
    def makeDir(path):
        os.mkdir(path)
        pass

    @staticmethod
    def isSameFiles(path1,path2):
        state = os.path.samefile(path1,path2)
        return state
        pass

    @staticmethod
    def isEmptyDir(path):
        if len(os.listdir(path)) > 0:
            state = False
        else :
            state = True
        return state
        pass

    @staticmethod
    def getCurrentDirectory():
        curDir = os.getcwd()
        return curDir
        pass

    @staticmethod
    def renameFile(old,new):
        os.rename(old,new)
        pass

    @staticmethod
    def copyFile(fileSource,fileDestiny):
        shutil.copy(fileSource,fileDestiny)
        pass
    
    @staticmethod
    def copytree(src, dst,copyFileFunction = None ,ignore = None):
        if FileSystem.isDirectory(dst) is False:
            os.makedirs(dst)

        names = os.listdir(src)

        if ignore is not None:
            ignored_names = ignore(src, names)
        else:
            ignored_names = set()

        errors = []
        for name in names:
            if name in ignored_names:
                continue
            srcname = FileSystem.joinPath(src, name)
            dstname = FileSystem.joinPath(dst, name)
            try:
                if FileSystem.isDirectory(srcname):
                    FileSystem.copytree(srcname, dstname,ignore)
                else:
                    FileSystem.copyFile(srcname, dstname)

                # XXX What about devices, sockets etc.?
            except (IOError, os.error) as why:
                errors.append((srcname, dstname, str(why)))
            # catch the Error from the recursive copytree so that we can
            # continue with other files
            except Error as err:
                errors.extend(err.args[0])

        if errors:
            raise Error(errors)

    @staticmethod
    def removeDirRecursive(path):
        distutils.dir_util.remove_tree(path)
        pass
    
    @staticmethod
    def copyDirRecursive(directorySource, directoryDestiny, copyFileFunction = None, ignorePatterns = None):
        if FileSystem.isDirectory(directoryDestiny) is False:
            os.makedirs(directoryDestiny)

        names = os.listdir(directorySource)

        if ignorePatterns is not None:
            ignore = shutil.ignore_patterns(ignorePatterns)
            ignored_names = ignore(directorySource, names)
        else:
            ignored_names = set()

        errors = []

        if copyFileFunction != None:
            chosenCopyFileFunction = copyFileFunction
        else :
            chosenCopyFileFunction = FileSystem.copyFile

        for name in names:
            if name in ignored_names:
                continue
            srcname = FileSystem.joinPath(directorySource, name)
            dstname = FileSystem.joinPath(directoryDestiny, name)
            try:
                if FileSystem.isDirectory(srcname):
                    FileSystem.copyDirRecursive(srcname, dstname ,copyFileFunction ,ignorePatterns)
                else:
                    chosenCopyFileFunction(srcname, dstname)

                # XXX What about devices, sockets etc.?
            except (IOError, os.error) as why:
                errors.append((srcname, dstname, str(why)))
            # catch the Error from the recursive copytree so that we can
            # continue with other files
            except shutil.Error as err:
                errors.extend(err.args[0])

        if errors:
            raise ValueError(errors)
        pass
    
    @staticmethod
    def printTreeDifference(path1,path2):
        checkTrees = filecmp.dircmp(path1,path2 )
        checkTrees.report_full_closure()
        pass
    pass

