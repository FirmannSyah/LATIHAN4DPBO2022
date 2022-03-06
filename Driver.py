from Job import Job
from Person import Person

# kelas Driver menggunakan multipe inheritance
# karena kelas ini mempunyai parent dari kelas Person dan Job

class Driver(Job, Person):
    
    __licenseID = ""
    __activeUntil = ""
    __vehicleType = ""

    # konstruktor
    def __init__(self):
        super().__init__()
        self.__licenseID = ""
        self.__activeUntil = ""
        self.__vehicleType = ""

    # set untuk semua variable
    def setLicenseID(self, licenseId):
        self.__licenseID = licenseId

    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType
        
    # get untuk semua variable
    def getLicenseID(self):
        return self.__licenseID

    def getActiveUntil(self):
        return self.__activeUntil

    def getVehicleType(self):
        return self.__vehicleType

    # print data
    def printDriver(self):
        self.printPerson()
        self.printJob()
        print(" Lisense ID    : " + self.getLicenseID())
        print(" Active Untill : " + self.getActiveUntil())
        print(" Vehicle Type  : " + self.getVehicleType())
        self.sleep()