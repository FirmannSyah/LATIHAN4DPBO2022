from Vehicle import Vehicle
# sama sepertik kelas airplane
# kelas ship juga merupakan child dari vehicle
class Ship(Vehicle):
    
    __age = ""                  
    __type = ""
    __countryOfManufacture = ""

    # konstruktor
    def __init__(self):
        super().__init__()
        self.__age = ""
        self.__type = ""
        self.__countryOfManufacture = ""
    
    # set untuk semua variable
    def setAge(self, age):
        self.__age = age

    def setType(self, type):
        self.__type = type

    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture
    
    # get untuk semua variable
    def getAge(self):
        return self.__age

    def getType(self):
        return self.__type

    def getCountryOfManufacture(self):
        return self.__countryOfManufacture
    
    # tampilan untuk ship
    def printShip(self):
        self.printVehicle()
        print(" Age                    : " + str(self.getAge()) + " Y")
        print(" Type                   : " + self.getType())
        print(" Country Of Manufacture : " + self.getCountryOfManufacture())
        self.move()