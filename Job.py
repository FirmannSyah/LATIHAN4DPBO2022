class Job:
    
    __NIP = ""
    __companyName = ""
    __position = ""

    #konstruktor
    def __init__(self):
        self.__NIP = ""
        self.__companyName = ""
        self.__position = ""
    
    # set untuk semua variable
    def setNIP(self, NIP):
        self.__NIP = NIP

    def setCompanyName(self, companyName):
        self.__companyName = companyName

    def setPosition(self,position):
        self.__position = position

    # get untuk semua variable 
    def getNIP(self):
        return self.__NIP

    def getCompanyName(self):
        return self.__companyName

    def getPosition(self):
        return self.__position

    # tampilan untuk job
    def printJob(self):
        print(" NIP           : " + self.getNIP())
        print(" Company Name  : " + self.getCompanyName())
        print(" Position      : " + self.getPosition())