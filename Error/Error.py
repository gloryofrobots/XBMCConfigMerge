class XBMConfigMergeError (BaseException):
    def __init__(self,msg):
        self.msg = str(msg)
        super(XBMConfigMergeError,self).__init__()
        pass

    def  __str__(self):
        return "XBMConfigMergeError:" + self.msg
        pass
    pass

  