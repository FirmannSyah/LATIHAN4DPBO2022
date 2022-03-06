class Vehicle:
    
    __name = ""
    __fuelType = ""
    __maxPassenger = ""

    # konstruktor
    def __init__(self):
        self.__name = ""
        self.__fuelType = ""
        self.__maxPassenger = ""
    
    # set untuk semua variable
    def setName(self, name):
        self.__name = name

    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    def setMaxPassanger(self, maxPassenger):
        self.__maxPassenger = maxPassenger
    
    # get untuk semua variable
    def getName(self):
        return self.__name

    def getFuelType(self):
        return self.__fuelType

    def getMaxPassanger(self):
        return self.__maxPassenger

    def move(self):
        print(self.getName() + " is moving.")
    
    # print data
    def printVehicle(self):
        print(" Name                   : " + self.getName())
        print(" Fuel Type              : " + self.getFuelType())
        print(" Max Passanger          : " + str(self.getMaxPassanger()))