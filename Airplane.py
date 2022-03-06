from Vehicle import Vehicle
#kelas airplane merupakan child dari vehicle
class Airplane(Vehicle):

    __age = ""         
    __type = ""
    __wingsLength = ""

    # konstruktor
    def __init__(self):
        super().__init__()
        self.__age = ""
        self.__type = ""
        self.__wingsLength = ""
    
    # set untuk semua variable
    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength
    
    # get untuk semua variable
    def getAge(self):
        return self.__age

    def getType(self):
        return self.__type

    def getWingsLength(self):
        return self.__wingsLength
    
    # tampilan untuk airplane
    def printAirplane(self):
        self.printVehicle()
        print(" Age                    : " + str(self.getAge()) + " Y")
        print(" Type                   : " + self.getType())
        print(" Wings Length           : " + str(self.getWingsLength()) + " M")
        self.move()