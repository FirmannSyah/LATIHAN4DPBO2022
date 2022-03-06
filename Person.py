class Person:

    __NIK = ""
    __name = ""
    __gender = ""
    
    # konstruktor
    def __init__(self):
        self.__NIK = ""
        self.__name = ""
        self.__gender = ""
    
    # set untuk semua variable
    def setNIK(self, NIK):
        self.__NIK = NIK

    def setName(self, name):
        self.__name = name

    def setGender(self, gender):
        self.__gender = gender
    
    # get untuk semua variable
    def getNIK(self):
        return self.__NIK

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    # metode untuk sleep()
    def sleep(self):
            print(f"{self.getName()} is sleeping.")
    
    # tampilan untuk person
    def printPerson(self):
        print(" NIK           : " + self.getNIK())
        print(" Nama          : " + self.getName())
        print(" Gender        : " + self.getGender())