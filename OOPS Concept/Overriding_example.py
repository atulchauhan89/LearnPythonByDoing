class Version(object):
    def __init__(self): #initializing values
      self.__version = 22 #private variable defined
    def getVersion(self): #prtinting the version
      print(self.__version)
    def setVersion(self, version): #changing the value 
      self.__version = version
obj = Version() #object defined
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print(obj.__version) ##returns error as accessed outside the class,private variable throws argument error