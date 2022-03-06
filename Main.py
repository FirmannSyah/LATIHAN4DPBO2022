from Driver import Driver
from Ship import Ship
from Airplane import Airplane


driver = [Driver() for i in range(5)]

NIK = ["100", "101", "102", "103", "104"]
NAME = ["Anto", "Andi", "Arya", "Astra", "Andi"]
GENDER = ['M', 'M', 'M', 'F', 'M' ]

for i in range(5):
    driver[i].setNIK(NIK[i])
    driver[i].setName(NAME[i])
    driver[i].setGender(GENDER[i])

print("======= PERSON =======")
for i in range(5):
        print("\nPerson ", (i+1))
        driver[i].printPerson()
        driver[i].sleep()


NIP = ["10", "20", "30", "40", "50"]
COMPANYNAME = ["SHOPEE", "GRAB", "GOJEK", "UBER", "SHOPEE"]
POSITION = ["Manager", "Driver", "CEO", "Driver", "Driver"]

for i in range(5):
    driver[i].setNIP(NIP[i])
    driver[i].setCompanyName(COMPANYNAME[i])
    driver[i].setPosition(POSITION[i])

print("\n======= JOB =======")
for i in range(5):
        print("\nJob ", (i+1))
        driver[i].printJob()


liSENCEID = ["1000", "1020", "1030", "1040", "1050"]
ACTIVEUNTIL= ["2077", "2077", "2077", "2077", "2077"]
VEHICLETYPE = ["Car", "Motorcycle", "Bicycle", "Car", "Truck"]

for i in range(5):
    driver[i].setLicenseID(liSENCEID[i])
    driver[i].setActiveUntil(ACTIVEUNTIL[i])
    driver[i].setVehicleType(VEHICLETYPE[i])

print("\n======= DRIVER =======")
for i in range(5):
        print("\nDriver ", (i+1))
        driver[i].printDriver()


NAME_S = ["Vehicle 1", "Vehicle 2", "Vehicle 3", "Vehicle 4", "Vehicle 5"]
FUELTYPE_S = ["Gasoline", "Oil", "Diesel", "Diesel", "Oil"]
MAXPASS_S = ["300", "150", "400", "500", "150"]

vehicle_S = [Ship() for i in range(5)]
for i in range(5):
    vehicle_S[i].setName(NAME_S[i])
    vehicle_S[i].setFuelType(FUELTYPE_S[i])
    vehicle_S[i].setMaxPassanger(MAXPASS_S[i])

print("\n======= VEHICLE =======")
for i in range(5):
        print("\nVehicle ", (i+1))
        vehicle_S[i].printVehicle()


TYPE_S = ["SHIP1000", "SHIP1001", "SHIP1002", "SHIP1003", "SHIP1004"]
AGE_S = ["10", "15", "12", "8", "5"]
COUNTRY_S = ["Indonesia", "Malaysia", "Japan", "US", "German" ]

for i in range(5):
    vehicle_S[i].setType(TYPE_S[i])
    vehicle_S[i].setAge(AGE_S[i])
    vehicle_S[i].setCountryOfManufacture(COUNTRY_S[i])

print("\n======= SHIP =======")
for i in range(5):
        print("\nShip ", (i+1))
        vehicle_S[i].printShip()


vehicle_A = [Airplane() for i in range(5)]
for i in range(5):
    vehicle_A[i].setName(NAME_S[i])
    vehicle_A[i].setFuelType(FUELTYPE_S[i])
    vehicle_A[i].setMaxPassanger(MAXPASS_S[i])

print("\n======= VEHICLE =======")
for i in range(5):
        print("\nVehicle ", (i+1))
        vehicle_A[i].printVehicle()


TYPE_S = ["PLANE1000", "PLANE1001", "PLANE1002", "PLANE1003", "PLANE1004"]
AGE_S = ["12", "8", "5", "7", "10"]
WINGSL_S = ["20.1", "30.3", "25.6", "31.8", "23.7" ]

for i in range(5):
    vehicle_A[i].setType(TYPE_S[i])
    vehicle_A[i].setAge(AGE_S[i])
    vehicle_A[i].setWingsLength(WINGSL_S[i])

print("\n======= AIRPLANE =======")
for i in range(5):
        print("\nAirplane ", (i+1))
        vehicle_A[i].printAirplane()





