from vehicle import Vehicle
class Ship(Vehicle):
    def __init__(self):
        self.age = 0
        self.type = ""
        self.country = ""
        self.name = ""
    def setShip(self, fueltype, maxpasengger, age, type, country, name):
        self.setVehicle(fueltype, maxpasengger)
        self.setBoolean(1)
        self.age = age
        self.type = type
        self.country = country
        self.name = name
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getType(self):
        return self.type
    def getCountry(self):
        return self.country
    def printShip(self):
        print("----------------------")
        print("|        Ship        |")
        print("----------------------")
        
        self.printVehicle()
        self.move(self.name)
        print("Ship Name               :" + str(self.name))
        print("Ship Type               :" + str(self.type))
        print("Ship Age                : " + str(self.age))
        print("Ship Country Manufacture: " + str(self.country))
        print("-----------------------")
        